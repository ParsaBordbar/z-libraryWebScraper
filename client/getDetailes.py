from bs4 import BeautifulSoup
import requests
import json
import os 
import re
import logging
from bs4 import BeautifulSoup

# flask 
from flask import Flask , render_template 
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
# Configure the Flask app with the MongoDB URI
app.config['MONGO_URI'] = 'mongodb://localhost:27017/zDataBase'
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')


# Now you can use the 'mongo' object to interact with your MongoDB database
@app.route('/api/insert', methods=['POST'])
def insert_document(new_book):
    users = mongo.db.books
    result = users.count_documents(new_book)
    print('ubeuwbgtbwb744744',result)
    # Check if the result exists
    if result > 0:
        print("The JSON file is already in the database.")
    else:
        print("The JSON file is not in the database.")
        result = users.insert_one(new_book)
        return str(result)


@app.route('/api/find', methods=['GET'])
def get_all_data():
        collection = mongo.db.books
        data = list(collection.find({}))  # Retrieve all documents from the collection
        # Convert ObjectId to string using json_util
        json_data = json_util.dumps(data)
        return json_data, 200






main_url = r'https://singlelogin.re'
page_categories = '/categories'
books_detail_list = []

#Makes a Costume Json Encoder (Ellipsis objects can't be parsed to json) 
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj is Ellipsis: 
            return 'detail_dict'
        return super().default(obj)

#Make Directories for Categories and books
def make_directory(dir_name, dir_parent):    
    path = os.path.join(dir_parent, file_name_validation(dir_name))
    try:
        os.mkdir(path)
    except:
        print('Such directory exists.')
    return path

def get_categories(main_url, page_categories):
    #Sending a Request 
    response = requests.get(main_url + page_categories)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Getting Categories
    categories = soup.select('.category-name a')
    return categories #Returns a List here be careful!

def load_file(cato , final_res):
    with open("{}\{}.json".format(cato, final_res)) as outfile:
        json_data = json.load(outfile)
    insert_document(json_data)

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
            book_desc = None
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
            book_edition = None

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
        try:
            book_pages = soup.select('.property_pages .property_value')[0].text
        except:
            book_pages = "No data"
        
        #Getting book ISBN 13
        try:
            book_isbn_13 = soup.select('.13 .property_value')[0].text
        except:
            book_isbn_13 = 'No ISBN13'
        
        #Getting book Series
        try:
          book_series = soup.select('.property_series .property_value')[0].text
        except:
          book_series = None

        #Getting book file
        book_file = soup.select('.property__file .property_value')[0].text
        
        #A Python Dictionary for a single books Details
        detail_dict = dict(
            title = book_title,
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
    #This characters are not Valid to be in a File name on Windows 
    if re.search(invalid_chars, file_name):
        valid_filename = re.sub(invalid_chars, '_', file_name)
        return valid_filename
        return False
    return file_name

#This will Download Book Covers!
def img_downloader(img_link, _path):
    with requests.get(img_link, stream=True) as r:
            with open(_path + ".jpg", 'wb') as f:
                for image in r.iter_content(chunk_size= 1024):
                    f.write(image)

#The Dictionaries from get_books will be parsed into To json files here!
def parse_to_json(detail_dict, category_dir):
    filename = detail_dict['title'] + '.json'
    titleBook = detail_dict['title'] 
    split = category_dir.split('\\')
    print('khvhkvopgpog ',split)
    final_res = split[len(split) - 1]
    print(split[len(split) - 1])
    print("{}\{}.json".format(category_dir, final_res))
    valid_file_name = file_name_validation(filename)
    data =  detail_dict
    print('ouoewguwegweg  ' + "{}\{}.json".format(category_dir, final_res))
    json_object = json.dumps(data, cls=JSONEncoder)

    with open(category_dir + "\\" + valid_file_name, "w") as outfile:
        outfile.write(json_object)
    # print(json_data)
    # print((detail_dict))
    # print(type(json_object))
    load_file(category_dir , final_res)
    new_user = json_object.title
    print(new_user)

def saved_books(books_detail_list, category_dir):
    for detail_dict in books_detail_list:
        filename = detail_dict['title'] 
        valid_file_name = file_name_validation(filename)
        book_dir = make_directory(valid_file_name, category_dir)
        parse_to_json(detail_dict, book_dir)
        path = book_dir + "\\" + valid_file_name
        img_downloader(detail_dict['imgLink'], path)
    
catagories = get_categories(main_url, page_categories)
details = get_books(catagories[1])
books_dir = make_directory("Books", ".")
category_dir = make_directory(catagories[1].text, books_dir)
saved_books(details, category_dir)

if __name__ == '__main__':
    app.run(debug = True)