import asyncio
from playwright.async_api import async_playwright

async def run_amazon_agent():
    async with async_playwright() as p:
        # פותחים דפדפן
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # כתובת חיפוש באמזון למקבוק אייר
        url = "https://www.amazon.com/s?k=macbook+air+m3"
        
        print(f"Agent is checking Amazon: {url}")
        
        # מגדירים User-Agent כדי להיראות כמו דפדפן רגיל
        await page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        })

        try:
            await page.goto(url, wait_until="load")
            
            # מחפשים את אלמנט המחיר (באמזון זה בד"כ קלאס שנקרא a-price-whole)
            await page.wait_for_selector(".a-price-whole", timeout=10000)
            
            price_whole = await page.locator(".a-price-whole").first.inner_text()
            price_fraction = await page.locator(".a-price-fraction").first.inner_text()
            
            full_price = f"{price_whole}.{price_fraction}"
            print(f"🎯 SUCCESS! Amazon Price: ${full_price}")
            
        except Exception as e:
            print(f"❌ Agent failed to find price: {e}")
            # אם נחסמנו, נראה מה הכותרת של הדף
            print(f"Page title: {await page.title()}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_amazon_agent())
