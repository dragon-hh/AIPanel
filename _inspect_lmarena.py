from playwright.sync_api import sync_playwright

selectors = [
    '[data-testid="user"]',
    '.user',
    '.message-user',
    '[data-testid="user-message"]',
    '.chat-message-user',
    '[data-message-author-role="user"]',
    '[data-role="user"]',
    '[data-author="user"]',
    '[data-testid*="user"]',
    '.message.user',
    '.message-row.user',
    '.message-row .user',
    '.chat-message.user',
    '.user-message',
]


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = None
        for p0 in context.pages:
            if "lmarena.ai" in (p0.url or ""):
                page = p0
                break
        if page is None:
            page = context.new_page()
            page.goto("https://lmarena.ai/zh", wait_until="domcontentloaded")
        page.wait_for_timeout(2000)

        def count_in_frame(frame, selector):
            try:
                return frame.eval_on_selector_all(selector, "els => els.length")
            except Exception:
                return -1

        print("Page URL:", page.url)
        print("Frames:", len(page.frames))
        for i, frame in enumerate(page.frames):
            print("Frame", i, frame.url)
            for s in selectors:
                c = count_in_frame(frame, s)
                if c and c > 0:
                    print(" ", s, c)

        best = None
        best_count = 0
        for s in selectors:
            c = count_in_frame(page.main_frame, s)
            if c > best_count:
                best_count = c
                best = s
        print("Best selector in main frame:", best, best_count)
        if best_count > 0:
            texts = page.eval_on_selector_all(
                best, "els => els.map(e => e.innerText).filter(Boolean).slice(0,5)"
            )
            print("Sample texts:", texts)

        candidates = page.evaluate(
            """() => {
                const nodes = Array.from(document.querySelectorAll('*'));
                const buckets = new Map();
                const samples = new Map();
                const isCandidate = (el) => {
                    const cls = (el.className || '').toString();
                    const data = Object.keys(el.dataset || {}).join(' ');
                    const text = (el.innerText || '').trim();
                    if (!text || text.length < 2) return false;
                    const key = (cls + ' ' + data).toLowerCase();
                    return /(message|chat|bubble|turn|prompt|user|assistant|role)/.test(key);
                };
                nodes.forEach(el => {
                    if (!isCandidate(el)) return;
                    const cls = (el.className || '').toString().trim();
                    const dataKeys = Object.keys(el.dataset || {});
                    const key = JSON.stringify({ cls, dataKeys });
                    buckets.set(key, (buckets.get(key) || 0) + 1);
                    if (!samples.has(key)) {
                        samples.set(key, (el.innerText || '').trim().slice(0, 120));
                    }
                });
                const sorted = Array.from(buckets.entries()).sort((a,b) => b[1] - a[1]).slice(0, 20);
                return sorted.map(([key, count]) => ({ key, count, sample: samples.get(key) }));
            }"""
        )
        print("Candidate class buckets:")
        for item in candidates:
            print(item)

        tree = page.evaluate(
            """() => {
                const container = Array.from(document.querySelectorAll('div')).find(el => {
                    const cls = (el.className || '').toString();
                    return cls.includes('flex') && cls.includes('flex-col') && cls.includes('items-center') && cls.includes('px-[--chat-padding]');
                });
                if (!container) return { found: false };
                const children = Array.from(container.children).map(el => {
                    return {
                        tag: el.tagName,
                        cls: (el.className || '').toString(),
                        dataKeys: Object.keys(el.dataset || {}),
                        text: (el.innerText || '').trim().slice(0, 160)
                    };
                });
                const ol = container.querySelector('ol');
                const olChildren = ol ? Array.from(ol.children).map(el => ({
                    tag: el.tagName,
                    cls: (el.className || '').toString(),
                    dataKeys: Object.keys(el.dataset || {}),
                    text: (el.innerText || '').trim().slice(0, 120)
                })) : [];
                const blocks = Array.from((ol || container).querySelectorAll('div')).filter(el => {
                    const cls = (el.className || '').toString();
                    return cls.includes('self-end') && cls.includes('group') && cls.includes('flex-col');
                });
                return {
                    found: true,
                    children,
                    olChildren,
                    userBlockCount: blocks.length,
                    userBlockSamples: blocks.map(el => (el.innerText || '').trim().slice(0, 120)).slice(0, 5)
                };
            }"""
        )
        print("Container tree:", tree)


if __name__ == "__main__":
    main()
