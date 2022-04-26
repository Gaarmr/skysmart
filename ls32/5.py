import requests
from bs4 import BeautifulSoup


r = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(r.text, 'html.parser')

book_list = []
price_list = []
stars_list = []
book_item = {}

for article in soup.find_all('article', class_="product_pod"):
    book_list.append(article.h3.a['title'])
    stars_list.append(article.p['class'])

for p in soup.find_all('p', class_="price_color"):
    price_list.append(p.text)

for book in range(len(book_list)):
    book_item[book_list[book]]=(price_list[book], stars_list[book])

for book, opt in book_item.items():
    print(book, opt)
    print()
