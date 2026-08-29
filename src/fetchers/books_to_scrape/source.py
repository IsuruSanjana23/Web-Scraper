from src.fetchers.core.http_client import Fetcher
from src.fetchers.books_to_scrape.parser import parse

class BooksToScrapeSource():
    
    def get_product(self):
        source_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
        fetcher = Fetcher()
        html = fetcher.fetch(source_url)
        
        return parse(html,source_url)
        
        
        