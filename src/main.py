# Entry point for the scraper project
from src.fetchers.books_to_scrape.fetcher import get_content


url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
content = get_content(url)
print(content[:200])

