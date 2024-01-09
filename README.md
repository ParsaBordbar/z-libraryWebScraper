![Screenshot (408)](https://github.com/ParsaBordbar/z-libraryWebScraper/assets/124056966/6dcb2a6f-bd0a-4e32-b928-faaaf390ae1d)

# Z-library Project
The goal is to get data from Z-library website store them in a database and render them as a website.
The Project has two parts, getting the data(scraping it) and making a website with data.
we will go throw it in the above order.
This project is developed in Python3, in each section we will mention the technologies that are being used for each part.

## **The scraping Part**
**Modules used:**

 - requests
 - bs4 (BeautifulSoup)
 - os
 - json
 - re
 - threading 
 - time

**Functions & classes in this module:**

 - `make_directory(dir_name, dir_parent)`
 -  `class  JSONEncoder(json.JSONEncoder)`
 -  `def  get_categories(main_url, page_categories)`
 -  `def  load_file(cato, final_res)`
 -  `def  get_books(category)`
 - `def  file_name_validation(file_name)`
 - `def  img_downloader(img_link, _path)`
 - `def  parse_to_json(detail_dict, category_dir)`
 - `def  saved_books(books_detail_list, category_dir)`
 - `def  get(cat, path)`
 - `def  multy_threads()`

 
 This part is implemente  in `getDetails.py` .
 
***So how do we get data?***  
well at first we need to send a request to the URL of the website which is *z-library* in our case, we've done this using `requests` module in python, Then we parse the returned data using the `bs4` library, we parse HTML from our get request (our response to URL request ) and select the desired parts, for getting the data that we want from each page. we also implement the code in a way that it goes through each category, and each book's page and gets the sweet data, then we will make a `JSON` file out of the extracted data and couple it with cover of the book, and using the `os` module we created a directory for each category and each book and store the cover and `JSON` data we created, the `JSON` that then will be added into our database which is `MongoDB`, then in the backend of next part, it will be fetched and rendered.

## Creating Accounts for Login
**Modules used:**
 - requests
 
 **Functions & classes in this module:**

 - `def  register_user(_email, _password, _user_name):`
 -  `def  verify_action(_email):`
 
This section we write code that allows us to make a new account in the website,
we've accomplish this by sending a post request to the login api , and listening.
The problem in this part is, we have not found any free service or api that can handle the verifying emails  for us so that we can make a lot of accounts and just log in and start downloading the books.
This part is implemented in `create_account.py`.


## The website

The website, contains two parts (like any website), the Back-end side & the Front-end,
we will go through each one separately.

## The Backend 

**Modules:**

 - flask
 - flask_pymongo
 - bson
 - flask_cors

**Routes:** 

 - `@app.route('/')` => *Home*
 - `@app.route('/cato')` => *Categories*
 -  `@app.route('/cato/<menu>')` =>	*Dynamic route for each Category*
 - `@app.route('/search')` => *Search page*
 - `@app.route('/api/insert', methods=['POST'])` => *Post data*  	
 - `@app.route('/api/find', methods=['GET'])`  => *Get data*

For the Backend of things we used Flask, we implemented routes with it, templates for rendering the front end part and also we connect to our database which is Mongodb.
The JSON we extracted and created in the scraping part, goes into  a collection and each one will be saved in our data base, we also make an api for fetching data from our data base.   
## The Frontend

**What we used to make it:**
 - html5
 - css3
 - tailwindcss
 - JavaScript
For the Front-end side of the stuff we used basic html5 with tailwind library, the front part is mostly responsive, we used grid base system for it's css side, so it's mostly, responsive and also we implemented a navbar for navigation in routes, the rendered elements are created in JS and the search part is actually implimented using JS as well. 
