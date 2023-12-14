import requests
from bs4 import BeautifulSoup
import json

#Note: The get_books Func Will be updated to generate Dicts for each book. P.B.

#A Python Dictionary for a single books Details
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


main_url = r'https://singlelogin.re'
page_categories = '/categories'

def get_categories(main_url, page_categories):
    
    #Sending a Request 
    response = requests.get(main_url + page_categories)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Getting Categories
    categories = soup.select('.category-name a')
    return categories #Returns a List here be careful!

#Should Return a Dictionary 
def get_books (categories, category_num):
    
    url_category = categories[category_num]['href']
    index_of_cover_image = 1

    # print(url_category)
    response = requests.get(main_url + url_category)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.select('h3 a')
    for i, book in enumerate(books):
        if i >= 5:
            break
        print(book.text)
        url_book = book['href']

        # print(url_book)
        response = requests.get(main_url + url_book)
        
        #Getting Tittle of Book
        soup = BeautifulSoup(response.text, 'html.parser')
        book_title = soup.select('h1')[0].text.strip()
        print('Book Title: ' + book_title)

        #Getting Books Author
        soup = BeautifulSoup(response.text, 'html.parser')
        book_author = soup.select('.col-sm-9 .color1')[0].text.strip()
        print('Book author: ' + book_author)

        #Getting Books Description
        soup = BeautifulSoup(response.text, 'html.parser')
        book_desc = soup.select('#bookDescriptionBox')[0].text.strip()
        print('Book desc: ' + book_desc)

        #Getting Book Category
        book_cat = soup.select('.property_value a')[0].text
        print('Book Cate: ' + book_cat)

        #Getting Book Publisher (if There is one!)
        try:
            book_publisher = soup.select('.property_publisher .property_value')[0].text
            print('Book Publisher: ' + book_publisher)
        except:
            print('No publisher!')

        #Getting Book url for It's Picture
        soup = BeautifulSoup(response.text, 'html.parser')
        book_img = soup.select('img')[index_of_cover_image]['src']
        print('Book img: ' + book_img)
        print('_______________________________________________________________')

#The Dictionary From get_books will be parsed into To Json here!
def parse_to_json(detail_dic):
    json_object = json.dumps(detail_dic, indent=16)
    with open("details.json", "w") as outfile:
        outfile.write(json_object)

catagories = get_categories(main_url, page_categories)
get_books(catagories, 0)