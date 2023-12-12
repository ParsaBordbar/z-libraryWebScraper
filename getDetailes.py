import requests
from bs4 import BeautifulSoup
import json


book_details = {
    'title': ...,
    'author': ...,
    'desc': ...,
    'Categories': ...,
    'Year': ...,
    'Edition': ...,
    'Publisher': ...,
    'Language': ...,
    'Pages': ...,
    'ISBN 10': ...,
    'ISBN 13': ...,
    'Series': ...,
    'File': ...,
    'IPFS CID': ...,
    'IPFS CID blake2b': ...,
}

main_url = r'https://singlelogin.re'
page_categories = '/categories'

response = requests.get(main_url + page_categories)
soup = BeautifulSoup(response.text, 'html.parser')

categories = soup.select('.category-name a')
for category in categories:
    print(category.text, end='\n')


url_category01 = categories[0]['href']
print(url_category01)
response = requests.get(main_url + url_category01)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.select('h3 a')
for book in books:
    print(book.text)

url_book01 = books[0]['href']
print(url_book01)
response = requests.get(main_url + url_book01)
print(response.text)

