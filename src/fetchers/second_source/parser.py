from bs4 import BeautifulSoup
from src.models.product import Product
from src.fetchers.core.http_client import Fetcher


def  get_content():
    
    source_url = "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
    
    fetcher = Fetcher()
    
    html = fetcher.fetch(source_url)
    
    return parse(html,source_url)


def availability_checker(text):
    return "in stock" in text.lower()

def parse(html,source_url):
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.select_one("h1")
    price_tag = soup.select_one("p.price_color")
    availability_tag = soup.select_one("p.instock.availability")
    rating_tag = soup.select_one("p.star-rating")

    if title_tag is None or price_tag is None or availability_tag is None or rating_tag is None:
        raise ValueError(f"Could not parse product data from {url}")

    title = title_tag.get_text(strip=True)
    price = float(price_tag.get_text(strip=True)[1:])
    currency = price_tag.get_text(strip=True)[0]
    available = availability_checker(availability_tag.get_text(strip=True))

    rating_classes = rating_tag.get("class", [])
    rating_name = None
    for item in rating_classes:
        if item.lower() in {"one", "two", "three", "four", "five"}:
            rating_name = item.title()
            break

    if rating_name is None:
        raise ValueError(f"Could not determine rating from {source_url}")

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }
    rating = rating_map[rating_name]

    return Product(
        title=title,
        price=price,
        currency=currency,
        available=available,
        rating=rating,
        source_url=source_url,
    )

