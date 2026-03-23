import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def get_price():
    async with async_playwright() as p:
        # פתיחת דפדפן כרום "נסתר"
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # כניסה לאתר
        url = "https://www.shekem-electric.co.il/catalogsearch/result/?q=macbook+air+m5"
        await page.goto(url, wait_until="networkidle")
        
        # מחכים 5 שניות שהמחיר ייטען מהשרת שלהם
        await page.wait_for_timeout(5000)
        
        # לוקחים את התוכן של הדף אחרי שהכל נטען
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        
        # חיפוש המחיר
        price_tag = soup.find("span", {"data-price-type": "finalPrice"})
        
        await browser.close()
        
        if price_tag:
            return price_tag.get_text().strip()
        return "Still not found - Page structure might have changed"

if __name__ == "__main__":
    print("--- STARTING PRO AGENT ---")
    result = asyncio.run(get_price())
    print(f"RESULT: {result}")
