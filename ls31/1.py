from http.client import responses
import requests

 
r = requests.get('https://vk.com')

print(r.text) 