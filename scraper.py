import requests
from bs4 import BeautifulSoup

URL = "https://www.shekem-electric.co.il/catalogsearch/result/?q=macbook+air+m5"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def check_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    # זה הקוד שיחפש את המחיר
    price_tag = soup.find("span", {"data-price-type": "finalPrice"})
    if price_tag:
        return price_tag.get_text()
    return "לא נמצא מחיר"

print(f"המחיר שמצאתי: {check_price()}")
