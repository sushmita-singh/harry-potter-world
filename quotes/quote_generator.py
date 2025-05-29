import random
import os

def get_random_quote():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    quotes_path = os.path.join(script_dir, "quotes.txt")
    
    try:
        with open("quotes/quotes.txt", "r", encoding="utf-8") as f:
            quotes = f.readlines()
        quote = random.choice(quotes).strip()
        return quote
    except Exception as e:
        return f"Error loading quote: {e}"

if __name__ == "__main__":
    print(get_random_quote())