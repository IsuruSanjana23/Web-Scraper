from bs4 import BeautifulSoup
from fetcher import get_content

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

html = get_content(url)

soup = BeautifulSoup(html, "html.parser")

element = soup.select_one("h1").get_text(strip=True)
price_element = soup.select_one("p.price_color").get_text(strip=True)
book_name = soup.select_one("li.active").get_text(strip=True)
availability = soup.select_one("p.instock.availability").get_text(strip=True)
rating = soup.select_one("p.star-rating").get("class")[1]


price_value = float(price_element[1:])
currency = price_element[0]
print(availability)

def  availability_checker(availability):
    if "in stock" in availability.lower():
        return True
    
print(availability_checker(availability))