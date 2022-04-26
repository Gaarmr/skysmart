import requests
from bs4 import BeautifulSoup


with open('skysmart\ls31\simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')


print(soup.h2)