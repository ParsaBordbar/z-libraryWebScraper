![Screenshot (408)](https://github.com/ParsaBordbar/z-libraryWebScraper/assets/124056966/6dcb2a6f-bd0a-4e32-b928-faaaf390ae1d)

# Z-Library Web Scraper Project

This project aims to extract data from the Z-library website, store it in a database, and display it on a custom website. The project is divided into two main parts: data scraping and website development. It is developed using Python3, and the technologies used in each section are detailed below.

## Data Scraping

The data scraping part of the project uses the following Python modules:

- requests
- bs4 (BeautifulSoup)
- os
- json
- re
- threading 
- time

The functions and classes implemented in this module include:

- `make_directory(dir_name, dir_parent)`
- `class JSONEncoder(json.JSONEncoder)`
- `get_categories(main_url, page_categories)`
- `load_file(cato, final_res)`
- `get_books(category)`
- `file_name_validation(file_name)`
- `img_downloader(img_link, _path)`
- `parse_to_json(detail_dict, category_dir)`
- `saved_books(books_detail_list, category_dir)`
- `get(cat, path)`
- `multy_threads()`

This part is implemented in `getDetails.py`.

The data scraping process begins by sending a request to the Z-library website using the `requests` module. The returned data is then parsed using the `bs4` library. The code is designed to navigate through each category and each book's page to extract the required data. This data is then converted into a JSON file and paired with the book's cover image. Using the `os` module, a directory is created for each category and each book, where the cover image and JSON data are stored. The JSON data is then added to our MongoDB database and fetched and rendered in the next part of the project.

## Account Creation

The account creation part of the project uses the `requests` module and includes the following functions:

- `register_user(_email, _password, _user_name)`
- `verify_action(_email)`

This part of the project allows us to create new accounts on the website by sending a POST request to the login API. However, we have not yet found a free service or API that can handle email verification for us, which would allow us to create multiple accounts, log in, and start downloading books. This part is implemented in `create_account.py`.

## Website Development

The website consists of two parts: the backend and the frontend.

### Backend

The backend uses the following modules:

- flask
- flask_pymongo
- bson
- flask_cors

The routes implemented in the backend include:

- `@app.route('/')` => Home
- `@app.route('/cato')` => Categories
- `@app.route('/cato/<menu>')` => Dynamic route for each Category
- `@app.route('/search')` => Search page
- `@app.route('/api/insert', methods=['POST'])` => Post data
- `@app.route('/api/find', methods=['GET'])` => Get data

The backend is developed using Flask. It includes routes, templates for rendering the frontend, and a connection to our MongoDB database. The JSON data extracted and created in the scraping part is added to a collection in the database. An API is also created for fetching data from the database.

### Frontend

The frontend is developed using:

- HTML5
- CSS3
- TailwindCSS
- JavaScript

The frontend is mostly responsive, thanks to the grid-based system used for its CSS. A navbar is implemented for navigation between routes, and the rendered elements are created in JavaScript. The search functionality is also implemented.
