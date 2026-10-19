import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 390, 'height': 844},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
            device_scale_factor=3,
            is_mobile=True,
            has_touch=True,
            record_video_dir="/tmp/playwright_video_refonte/"
        )
        page = await context.new_page()

        os.makedirs("/home/jules/verification/screenshots_final", exist_ok=True)

        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")
        await page.wait_for_timeout(1000)

        # 1. Gate Screen
        await page.screenshot(path="/home/jules/verification/screenshots_final/1_gate.png")

        # Select Omar or click user select button
        user_btn = page.locator("[data-user-select='Omar']")
        if await user_btn.count() > 0:
            await user_btn.click()
            await page.wait_for_timeout(500)

        # 2. Dashboard Screen
        await page.screenshot(path="/home/jules/verification/screenshots_final/2_dashboard.png")

        # 3. Suivi Tab
        await page.click("button[data-page='suivi']")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/screenshots_final/3_suivi_clients.png")

        # 4. FAB Quick Action
        await page.click("#fabBtn")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/screenshots_final/4_fab_sheet.png")

        # Close FAB by clicking backdrop
        await page.click("#quickActionModal")
        await page.wait_for_timeout(300)

        # 5. Menu Tab
        await page.click("button[data-page='menu']")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/home/jules/verification/screenshots_final/5_menu_profiles.png")

        await context.close()
        await browser.close()
        print("Playwright iPhone verification completed successfully!")

asyncio.run(run())
