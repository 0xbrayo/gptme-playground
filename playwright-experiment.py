#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10,<3.12"
# dependencies = [
#   "playwright>=1.40.0",
# ]
# [tool.uv]
# exclude-newer = "2024-01-01T00:00:00Z"
# ///

from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to Google
        await page.goto('https://www.google.com')

        # Accept cookies if the prompt appears
        try:
            accept_button = await page.wait_for_selector('button:has-text("I agree")', timeout=5000)
            await accept_button.click()
        except:
            pass  # If the prompt doesn't appear, continue

        # Enter search query and submit
        query = "Playwright Python"
        await page.fill('input[name="q"]', query)
        await page.press('input[name="q"]', 'Enter')

        # Wait for results to load
        await page.wait_for_selector('h3')

        # Extract and print titles of search results
        titles = await page.locator('h3').all_text_contents()
        for title in titles:
            print(title)

        await browser.close()

asyncio.run(main())
