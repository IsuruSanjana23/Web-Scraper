from bs4 import BeautifulSoup
#from src.models.product import Product
from fetcher import get_content

def parse(html):
    
    html = get_content(html)
    
    soup = BeautifulSoup(html, "html.parser")
    
    title = soup.select_one("li.active").get_text(strip=True)
    price = float(soup.select_one("p.price_color").get_text(strip=True)[1:])
    
    availability = soup.select_one("p.instock.availability").get_text(strip=True)
    
    def  availability_checker(availability):
        if "in stock" in availability.lower():
            return True
    
    availability = availability_checker(availability)
    rating  = soup.select_one("p.star-rating").get("class")[1]
    
    
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    
    
    rating =  rating_map[rating]
            
    print(rating)
    
    
parse("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
    
    
    
    