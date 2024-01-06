import time
import threading
import requests
import json
import os
import re
import logging
from bs4 import BeautifulSoup
from app import *

main_url = r'https://singlelogin.re'
page_categories = '/categories'
MAX_CATEGORY = 5
MAX_BOOK = 5


# Makes a Costume Json Encoder (Ellipsis objects can't be parsed to json)
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj is Ellipsis:
            return 'detail_dict'
        return super().default(obj)


# Make Directories for Categories and books
def make_directory(dir_name, dir_parent):
    path = os.path.join(dir_parent, file_name_validation(dir_name))
    try:
        os.mkdir(path)
    except:
        print('Such directory exists.')
    return path


def get_categories(main_url, page_categories):
    # Sending a Request
    response = requests.get(main_url + page_categories)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Getting Categories
    categories = soup.select('.category-name a')
    return categories  # Returns a List here be careful!


def load_file(cato, final_res):
    with open("{}\{}.json".format(cato, final_res)) as outfile:
        json_data = json.load(outfile)
    insert_document(json_data)


# Should Return a Dictionary
def get_books(category):
    books_detail_list = []
    url_category = category['href']
    index_of_cover_image = 1

    response = requests.get(main_url + url_category)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.select('h3 a')
    for count, book in enumerate(books):
        if count >= MAX_BOOK:
            break
        url_book = book['href']

        response = requests.get(main_url + url_book)

        # Getting Tittle of Book
        soup = BeautifulSoup(response.text, 'html.parser')
        book_title = soup.select('h1')[0].text.strip()

        # Getting Books Author
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            book_author = soup.select('.col-sm-9 .color1')[0].text.strip()
        except:
            book_author = None

        # Getting Books Description
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            book_desc = soup.select('#bookDescriptionBox')[0].text.strip()
        except:
            book_desc = None
        # Getting Book Category
        book_cat = soup.select('.property_value a')[0].text

        # Getting Book Publisher (if There is one!)
        try:
            book_publisher = soup.select('.property_publisher .property_value')[0].text
        except:
            book_publisher = None

        # Getting Book url for It's Picture
        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            book_img = soup.select('img')[index_of_cover_image]['src']
        except:
            book_img = None

        # Getting Book Edition
        try:
            book_edition = soup.select('.property_edition .property_value')[0].text
        except:
            book_edition = None

        # Getting Book IPFS CID blake2b
        try:
            book_cid_blake = soup.select('.property_ipfs_blake2b_cid span ')[0].text
        except:
            book_cid_blake = None

        # Getting Book IPFS CID
        try:
            book_cid = soup.select('.property_ipfs_cid span')[0].text
        except:
            book_cid = None

        # Getting Book ISBN 10
        try:
            book_isbn_10 = soup.select(' .property_value .{10}')[0].text
        except:
            book_isbn_10 = None

        # Getting Book Year
        book_year = soup.select('.property_year .property_value')[0].text

        # Getting book pages
        try:
            book_pages = soup.select('.property_pages .property_value')[0].text
        except:
            book_pages = None

        # Getting book ISBN 13
        try:
            book_isbn_13 = soup.select('.13 .property_value')[0].text
        except:
            book_isbn_13 = None

        # Getting book Series
        try:
            book_series = soup.select('.property_series .property_value')[0].text
        except:
            book_series = None

        # Getting book file
        book_file = soup.select('.property__file .property_value')[0].text

        # Getting the Book's Language
        try:
            book_language = soup.select('.text-capitalize')[0].text
        except:
            book_language = None

        # A Python Dictionary for a single books Details
        detail_dict = dict(
            title=book_title,
            imgLink=book_img,
            author=book_author,
            desc=book_desc,
            **({'Categories': book_cat} if book_cat else {}),
            **({'Year': book_year} if book_year else {}),
            **({'Edition': book_edition} if book_edition else {}),
            **({'Publisher': book_publisher} if book_publisher else {}),
            **({'Language': book_language} if book_language else {}),
            **({'Pages': book_pages} if book_pages else {}),
            **({'ISBN_10': book_isbn_10} if book_isbn_10 else {}),
            **({'ISBN_13': book_isbn_13} if book_isbn_13 else {}),
            **({'File': book_file} if book_file else {}),
            **({'IPFS_CID': book_cid} if book_cid else {}),
            **({'IPFS_CID_blake2b': book_cid_blake} if book_cid_blake else {}),
            **({'Series': book_series} if book_series else {}),
        )

        books_detail_list.append(detail_dict)
    return books_detail_list


# This Function cheeks if the File name is Valid or not if not, change it to be Valid.
def file_name_validation(file_name):
    invalid_chars = r'[\\/:\*\?"<>\|]'
    # These characters are not Valid to be in a File name on Windows
    if re.search(invalid_chars, file_name):
        valid_filename = re.sub(invalid_chars, '_', file_name)
        return valid_filename
    return file_name


# This will Download Book Covers!
def img_downloader(img_link, _path):
    try:
        with requests.get(img_link, stream=True) as r:
            with open(_path + ".jpg", 'wb') as f:
                for image in r.iter_content(chunk_size=1024):
                    f.write(image)
    except:
        pass


# The Dictionaries from get_books will be parsed into To json files here!
def parse_to_json(detail_dict, category_dir):
    try:
        filename = detail_dict['title'] + '.json'
        titleBook = detail_dict['title']
        split = category_dir.split('\\')
        final_res = split[len(split) - 1]
        print(split[len(split) - 1])
        print("{category_dir}\{final_res}.json")
        valid_file_name = file_name_validation(filename)
        data = detail_dict
        json_object = json.dumps(data, cls=JSONEncoder)
        with open(category_dir + "\\" + valid_file_name, "w") as outfile:
            outfile.write(json_object)
        load_file(category_dir, final_res)
        new_user = json_object.title
    except:
        pass


def saved_books(books_detail_list, category_dir):
    for detail_dict in books_detail_list:
        filename = detail_dict['title']
        valid_file_name = file_name_validation(filename)
        book_dir = make_directory(valid_file_name, category_dir)
        parse_to_json(detail_dict, book_dir)
        path = book_dir + "\\" + valid_file_name
        img_downloader(detail_dict['imgLink'], path)


def get(cat, path):
    details = get_books(cat)
    books_dir = make_directory(path, ".")
    category_dir = make_directory(cat.text, books_dir)
    saved_books(details, category_dir)

# injo single thraed hese
def single_thread():
    catagories = get_categories(main_url, page_categories)
    for count, cat in enumerate(catagories):
        if count == MAX_CATEGORY: break
        get(cat, "Books_single")

# vali injo na
def multy_threads():
    t_list = list()
    catagories = get_categories(main_url, page_categories)
    for count, cat in enumerate(catagories):
        if count == MAX_CATEGORY: break
        t_list.append(threading.Thread(target=get, args=(cat, "Books_multy",)))
        t_list[count].start()

    for thread in t_list:
        thread.join()


if __name__ == '__main__':
    time_multy = time.time()
    multy_threads()
    print(time_multy := time.time() - time_multy)
