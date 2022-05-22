import requests
from bs4 import BeautifulSoup


r = requests.get('https://books.toscrape.com/')
soup = BeautifulSoup(r.text, 'html.parser')

book_list = []
price_list = []
book_item = {}

for article in soup.find_all('article', class_="product_pod"):
    book_list.append(article.h3.a.text)
    price_list.append(article.find('p', class_='price_color').text[1:])


for book in range(len(book_list)):
    book_item[book_list[book]]=price_list[book]

for book, price in book_item.items():
    print(book, price)
    