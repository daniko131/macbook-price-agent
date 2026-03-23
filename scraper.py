import asyncio
from playwright.async_api import async_playwright

async def run_agent():
    async with async_playwright() as p:
        # פתיחת דפדפן עם הגדרות "אנושיות"
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # כתובת החיפוש ב-KSP למקבוק אייר
        url = "https://ksp.co.il/web/search?q=macbook+air"
        
        print(f"Agent is visiting: {url}")
        await page.goto(url, wait_until="domcontentloaded")
        
        # מחכים שהמוצרים יופיעו על המסך
        try:
            # ב-KSP המחיר בד"כ נמצא בתוך אלמנט עם טקסט של שקלים
            await page.wait_for_selector("text=₪", timeout=10000)
            
            # שליפת כל הטקסטים של המחירים בדף
            prices = await page.locator("text=₪").all_inner_texts()
            
            # ניקוי המחיר הראשון שנמצא (בד"כ המוצר הראשון בתוצאות)
            if prices:
                raw_price = prices[0].replace("₪", "").replace(",", "").strip()
                print(f"SUCCESS: Found price: ₪{raw_price}")
            else:
                print("FAILED: Could not find any price on the page.")
                
        except Exception as e:
            print(f"ERROR: Timeout or blocked by KSP. {e}")
            # במקרה של חסימה, נדפיס את הכותרת לראות מה האתר מראה לנו
            title = await page.title()
            print(f"Site title is: {title}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_agent())
