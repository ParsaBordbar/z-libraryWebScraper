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
if __name__ == '__main__':
    app.run(debug = True)