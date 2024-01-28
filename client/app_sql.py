# flask 
from flask import Flask , render_template 
from flask_pymongo import PyMongo
from bson import json_util
from flask_cors import CORS
from sql_db import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
# Configure the Flask app with the MongoDB URI
app.config['MONGO_URI'] = 'mongodb://localhost:27017/zDataBase'
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cato')
def cato():
    return render_template('cato.html')

@app.route('/cato/<menu>')
def selfCato(menu):
    return render_template('selfCato.html')

@app.route('/search')
def search():
    return render_template('search.html')

# Now you can use the 'mongo' object to interact with your MongoDB database
@app.route('/api/insert', methods=['POST'])
def insert_document(new_book):
    db = Book_db()
    db.add_book(list(new_book.values()))
    db.close()

@app.route('/api/find', methods=['GET'])
def get_all_data():
    db = Book_db()
    json_data = db.get_all_books()
    db.close()
    return json_data, 200
    
if __name__ == '__main__':
    app.run(debug = True)
