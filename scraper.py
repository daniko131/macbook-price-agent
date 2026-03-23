import requests
from bs4 import BeautifulSoup

# הקישור הישיר למקבוק אייר (תוודא שזה הקישור המדויק מהדפדפן שלך)
URL = "https://www.shekem-electric.co.il/catalogsearch/result/?q=macbook+air+m5"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
}

def check_price():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # ניסיון למצוא את המחיר לפי כמה סימנים נפוצים באתר
        price_tag = soup.find("span", {"data-price-type": "finalPrice"})
        
        if not price_tag:
            # ניסיון נוסף אם הראשון נכשל (חיפוש קלאס אחר)
            price_tag = soup.select_one(".price-wrapper .price")

        if price_tag:
            price_text = price_tag.get_text().strip()
            # משאירים רק מספרים
            clean_price = "".join(filter(str.isdigit, price_text))
            return clean_price
            
        return "Price Element Not Found"
    except Exception as e:
        return f"Error: {e}"

print(f"--- AGENT REPORT ---")
print(f"Checking: {URL}")
print(f"Result: {check_price()}")
