from duckduckgo_search import DDGS

def ask_the_internet():
    print("Agent is searching the web for MacBook Air M3 prices...")
    try:
        with DDGS() as ddgs:
            # אנחנו שואלים את מנוע החיפוש ישירות
            results = ddgs.text("macbook air m3 price israel ksp ivory", max_results=5)
            
            if results:
                print("--- AGENT FOUND DATA ---")
                for i, res in enumerate(results):
                    print(f"{i+1}. {res['title']}")
                    print(f"   Link: {res['href']}")
                    print(f"   Snippet: {res['body']}\n")
                return "Data retrieved successfully!"
            else:
                return "No results found."
    except Exception as e:
        return f"Agent Error: {e}"

if __name__ == "__main__":
    report = ask_the_internet()
    print(report)
