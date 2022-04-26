import requests
from bs4 import BeautifulSoup

r = requests.get('https://habr.com/ru/all/')

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())
