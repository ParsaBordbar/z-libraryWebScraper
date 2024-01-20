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
    
if __name__ == '__main__':
    app.run(debug = True)
