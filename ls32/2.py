import requests
from bs4 import BeautifulSoup


r = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(r.text, 'html.parser')

for article in soup.find_all('article', class_="product_pod"):
    book_name = article.h3.a.text
    print(book_name)
