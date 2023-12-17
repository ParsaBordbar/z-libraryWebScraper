import requests
from bs4 import BeautifulSoup
import json
import os 
import re
import logging

#Makes a Costume Json Encoder (Ellipsis objects can't be parsed to json) 
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj is Ellipsis:
            return 'detail_dict'
        return super().default(obj)


main_url = r'https://singlelogin.re'
page_categories = '/categories'
books_detail_list = []

def get_categories(main_url, page_categories):
    
    #Sending a Request 
    response = requests.get(main_url + page_categories)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Getting Categories
    categories = soup.select('.category-name a')
    return categories #Returns a List here be careful!

#Should Return a Dictionary 
def get_books (category):
    
    url_category = category['href']
    index_of_cover_image = 1

    response = requests.get(main_url + url_category)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.select('h3 a')
    for i, book in enumerate(books):
        if i >= 10:
            break
        url_book = book['href']

        response = requests.get(main_url + url_book)
        
        #Getting Tittle of Book
        soup = BeautifulSoup(response.text, 'html.parser')
        book_title = soup.select('h1')[0].text.strip()

        #Getting Books Author
        soup = BeautifulSoup(response.text, 'html.parser')
        book_author = soup.select('.col-sm-9 .color1')[0].text.strip()

        #Getting Books Description
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            book_desc = soup.select('#bookDescriptionBox')[0].text.strip()
        except:
            book_desc = 'No description!'
        #Getting Book Category
        book_cat = soup.select('.property_value a')[0].text

        #Getting Book Publisher (if There is one!)
        try:
            book_publisher = soup.select('.property_publisher .property_value')[0].text
        except:
            book_publisher = 'No publisher!'

        #Getting Book url for It's Picture
        soup = BeautifulSoup(response.text, 'html.parser')
        book_img = soup.select('img')[index_of_cover_image]['src']
        
        #Getting Book Edition
        try:
            book_edition = soup.select('.property_edition .property_value')[0].text
        except:
            book_edition = 'No Edition!'

        #Getting Book IPFS CID blake2b
        try:
            book_cid_blake = soup.select('.property_ipfs_blake2b_cid span ')[0].text
        except:
            book_cid_blake = 'No Book IPFS CID!'
        
        #Getting Book IPFS CID 
        try:
            book_cid = soup.select('.property_ipfs_cid span')[0].text
        except:
            book_cid = ' No Book IPFS CID!'

        #Getting Book ISBN 10 
        try:
            book_isbn_10 = soup.select(' .property_value .{10}')[0].text
        except:
            book_isbn_10 = 'No box ISBN10'
        
        #Getting Book Year
        book_year = soup.select('.property_year .property_value')[0].text

        #Getting book pages
        book_pages = soup.select('.property_pages .property_value')[0].text

        #Getting book ISBN 13
        try:
            book_isbn_13 = soup.select('.13 .property_value')[0].text
        except:
            book_isbn_13 = 'No ISBN13'
        
        #Getting book Series
        try:
          book_series = soup.select('.property_series .property_value')[0].text
        except:
          book_series = 'No Series!'

        #Getting book file
        book_file = soup.select('.property__file .property_value')[0].text
        
        #A Python Dictionary for a single books Details
        detail_dict = dict(
            title= book_title,
            imgLink= book_img,
            author= book_author,
            desc= book_desc,
            Categories= book_cat,
            Year= book_year,
            Edition= book_edition,
            Publisher= book_publisher,
            Language= ...,
            Pages= book_pages,
            ISBN_10= book_isbn_10,
            ISBN_13= book_isbn_13,
            Series= book_series,
            File= book_file,
            IPFS_CID= book_cid,
            IPFS_CID_blake2b= book_cid_blake,
                           )
        books_detail_list.append(detail_dict)
    return books_detail_list

#This Function cheeks if the File name is Valid or not if not, change it to be Valid.
def file_name_validation(file_name):
    
    invalid_chars = r'[\\/:\*\?"<>\|]'
    if re.search(invalid_chars, file_name):
        valid_filename = re.sub(invalid_chars, '_', file_name)
        return valid_filename
        return False
    else:
        return file_name



#The Dictionaries from get_books will be parsed into To json files here!
def parse_to_json(books_detail_list):
    print(*books_detail_list, sep='\n______________________________\n')
    i = 0
    for detail_dict in books_detail_list:
        i += 1
        filename = str(i) +"_" + detail_dict['title'] + '.json'
        valid_file_name = file_name_validation(filename)
        data = {valid_file_name: detail_dict}
        json_object = json.dumps(data, cls=JSONEncoder)
        with open("./books/" + valid_file_name, "w") as outfile:
            outfile.write(json_object)

catagories = get_categories(main_url, page_categories)
details = get_books(catagories[0])
parse_to_json(details)
