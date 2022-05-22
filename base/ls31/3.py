import requests
from bs4 import BeautifulSoup


with open('skysmart\ls31\simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

article = soup.find('div', class_='article')
print(article)

headline = article.h2.a.text
print(headline)

headline = article.p.text
print(headline)