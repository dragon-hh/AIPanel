from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = None
        print("Open pages:")
        for p0 in context.pages:
            print(" -", p0.url)
        for p0 in context.pages:
            if "aistudio.google.com" in (p0.url or ""):
                page = p0
                break
        if page is None:
            page = context.new_page()
            page.goto("https://aistudio.google.com/", wait_until="domcontentloaded")
        page.wait_for_timeout(2000)

        print("Page URL:", page.url)

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
                    const role = el.getAttribute('role') || '';
                    const key = JSON.stringify({ cls, dataKeys, role });
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

        input_candidates = page.evaluate(
            """() => {
                const nodes = Array.from(document.querySelectorAll('textarea, input, [contenteditable="true"], [role="textbox"]'));
                return nodes.map(el => ({
                    tag: el.tagName,
                    id: el.id || '',
                    cls: (el.className || '').toString(),
                    role: el.getAttribute('role') || '',
                    contenteditable: el.getAttribute('contenteditable') || '',
                    ariaLabel: el.getAttribute('aria-label') || '',
                    placeholder: el.getAttribute('placeholder') || '',
                    value: el.value ? el.value.slice(0, 160) : ''
                })).slice(0, 20);
            }"""
        )
        print("Input candidates:")
        for item in input_candidates:
            print(item)

        user_blocks = page.evaluate(
            """() => {
                const blocks = Array.from(document.querySelectorAll('.chat-turn-container.user'));
                return blocks.map(el => {
                    const chunk = el.querySelector('.cmark-node.user-chunk');
                    return {
                        cls: (el.className || '').toString(),
                        text: (chunk ? chunk.innerText : el.innerText || '').trim().slice(0, 160),
                        html: (el.outerHTML || '').trim().slice(0, 200)
                    };
                });
            }"""
        )
        print("User blocks:")
        for item in user_blocks:
            print(item)

        prompt_containers = page.evaluate(
            """() => {
                const blocks = Array.from(document.querySelectorAll('.virtual-scroll-container.user-prompt-container'));
                return blocks.map(el => {
                    const chunk = el.querySelector('.cmark-node.user-chunk');
                    const parent = el.closest('.chat-turn-container');
                    return {
                        cls: (el.className || '').toString(),
                        parentCls: parent ? (parent.className || '').toString() : '',
                        text: (chunk ? chunk.innerText : el.innerText || '').trim().slice(0, 160),
                        html: (el.innerHTML || '').trim().slice(0, 200)
                    };
                });
            }"""
        )
        print("Prompt containers:")
        for item in prompt_containers:
            print(item)

        turn_role_blocks = page.evaluate(
            """() => {
                const blocks = Array.from(document.querySelectorAll('[data-turn-role],[data-turnrole],[turnrole]'));
                return blocks.map(el => {
                    return {
                        tag: el.tagName,
                        cls: (el.className || '').toString(),
                        dataTurnRole: el.getAttribute('data-turn-role') || el.getAttribute('data-turnrole') || el.getAttribute('turnrole') || '',
                        text: (el.innerText || '').trim().slice(0, 160),
                        html: (el.innerHTML || '').trim().slice(0, 200)
                    };
                });
            }"""
        )
        print("Turn role blocks:")
        for item in turn_role_blocks:
            print(item)


if __name__ == "__main__":
    main()
