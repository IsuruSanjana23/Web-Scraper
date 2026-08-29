# Entry point for the scraper project
from src.fetchers.books_to_scrape.parser import get_product
from src.fetchers.second_source.parser import get_content

product =  get_product()

product2 = get_content()

print(product)

