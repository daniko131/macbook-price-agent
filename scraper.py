import requests

def run_agent():
    print("--- STARTING LIGHTWEIGHT AGENT ---")
    # חיפוש דרך מנוע חיפוש פשוט שלא חוסם בוטים בקלות
    url = "https://api.duckduckgo.com/?q=macbook+air+m3+price+israel&format=json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # אם יש תוצאה ישירה (Abstract)
        if data.get("AbstractText"):
            print(f"INFO FOUND: {data['AbstractText']}")
        else:
            # אם אין תוצאה ישירה, פשוט נדפיס שהסוכן מחובר לאינטרנט
            print("Connected to Internet. Agent is ready for data.")
            print(f"Related Topics found: {len(data.get('RelatedTopics', []))}")
            
        return "SUCCESS"
    except Exception as e:
        print(f"Error: {e}")
        return "FAILED"

if __name__ == "__main__":
    run_agent()
