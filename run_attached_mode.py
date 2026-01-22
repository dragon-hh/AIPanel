from playwright.sync_api import sync_playwright
import os
import time

def run_attached_mode():


    with sync_playwright() as p:
        print("正在尝试连接到已打开的 Chrome (端口 9222)...")
        try:
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
        except Exception as e:
            print(f"❌ 连接失败！请检查 Chrome 是否启动。\n错误详情: {e}")
            return
        context = browser.contexts[0]
        if len(context.pages) > 0:
            page = context.pages[0]
        else:
            page = context.new_page()
        print("✅ 连接成功！开始批量处理...")

if __name__ == "__main__":
    run_attached_mode()