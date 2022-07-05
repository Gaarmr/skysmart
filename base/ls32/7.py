import requests
from bs4 import BeautifulSoup


# Get the page
source = requests.get('https://books.toscrape.com').text
soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())

# Finding useful information
for item in soup.find_all('article', class_='product_pod'):
    title = item.h3.a['title']
    price = item.find('p', class_='price_color').text[1:]
    rating = item.p['class'][-1]
    pic = item.div.a.img['src']
    print(title, price, f"Rating: {rating}", f'https://books.toscrape.com/{pic}', sep='\n', end='\n\n')