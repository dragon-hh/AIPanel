from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        
        page = None
        for p0 in context.pages:
            if "aistudio.google.com" in (p0.url or ""):
                page = p0
                break
        
        if not page:
            print("AI Studio page not found")
            return

        print(f"Inspecting page: {page.url}")
        
        result = page.evaluate("""() => {
            const firstPanel = document.querySelector('mat-expansion-panel');
            if (!firstPanel) return "No expansion panel found";
            
            function getStructure(el, depth=0) {
                if (depth > 5) return '...';
                if (!el) return null;
                const children = Array.from(el.children).map(c => ({
                    tag: c.tagName,
                    cls: c.className,
                    text: c.innerText.slice(0, 50).replace(/\\n/g, ' '),
                    href: c.getAttribute('href'),
                    children: getStructure(c, depth + 1)
                }));
                return {
                    tag: el.tagName,
                    cls: el.className,
                    children: children
                };
            }
            
            return getStructure(firstPanel);
        }""")
        
        import json
        print("Inspection Result:", json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
