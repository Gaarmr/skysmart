import requests
from bs4 import BeautifulSoup


# r = requests.get('https://books.toscrape.com/')
# soup = BeautifulSoup(r.text, 'html.parser')

book_list = []
price_list = []
stars_list = []
book_item = {}

page = 1
r = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')

# page_count = soup.find('li', class_='current')
# print(page_count.text)

while r.status_code == 200:
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')
    soup = BeautifulSoup(r.text, 'html.parser')
    page += 1

    for article in soup.find_all('article', class_="product_pod"):
        book_list.append(article.h3.a['title'])
        stars_list.append(article.p['class'][-1])
        price_list.append(article.find('p', class_='price_color').text[1:])

    # for p in soup.find_all('p', class_="price_color"):
    #     price_list.append(p.text[1:])

    for book in range(len(book_list)):
        print(book_list[book], price_list[book], stars_list[book], sep='\n', end='\n\n')


    # for book, opt in book_item.items():
    #     print(book, opt)
    #     print()
