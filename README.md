**

# Z-library Project
The goal is to get data from Z-library website store them in a database and render them as a website.
The Project has two parts, getting the data(scraping it) and making a website with data.
we will go throw it in the above order.
This project is developed in Python3, in each section we will mention the technologies that are being used for each part.

## **The scraping Part**
**Modules:**

 - requests
 - bs4 (BeautifulSoup)
 - os
 - json
 - re
 - threading 
 - time
 
 This part is implemente  in `getDetails.py` .
*So how do we get data?*  
well at first we need to send a request to the URL of the website which is *z-library* in our case, we've done this using `requests` module in python, Then we parse the returned data using the `bs4` library, we parse HTML from our get request (our response to URL request ) and select the desired parts, for getting the data that we want from each page. we also implement the code in a way that it goes through each category, and each book's page and gets the sweet data, then we will make a `JSON` file out of the extracted data and couple it with cover of the book, and using the `os` module we created a directory for each category and each book and store the cover and `JSON` data we created, the `JSON` that then will be added into our database which is `MongoDB`, then in the backend of next part, it will be fetched and rendered.

## Creating Accounts for Login




## The website

The website, contains two parts (like any website), the Back-end side & the Front-end,
we will go through each one separately.

## The Backend 

**Modules:**

 - flask
 - flask_pymongo
 - bson
 - flask_cors

## The Frontend

**Technolagies**

 - html5
 - css3
 - tailwindcss
 - JavaScript
