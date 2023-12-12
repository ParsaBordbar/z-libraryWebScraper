import requests
from bs4 import BeautifulSoup
import json


book_details = {
    'title': ...,
    'author': ...,
    'imgLink': ...,
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
index_of_cover_image = 1
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

soup = BeautifulSoup(response.text, 'html.parser')
book_title = soup.select('h1')[0].text.strip()
print('Book Title: ' + book_title)

soup = BeautifulSoup(response.text, 'html.parser')
book_author = soup.select('.col-sm-9 .color1')[0].text.strip()
print('Book author: ' + book_author)

soup = BeautifulSoup(response.text, 'html.parser')
book_desc = soup.select('#bookDescriptionBox')[0].text.strip()
print('Book desc: ' + book_desc)

soup = BeautifulSoup(response.text, 'html.parser')

book_img = soup.select('img')[index_of_cover_image]['src']
print('Book img: ' + book_img)
