import json

import mysql.connector


class Book_db:
    def __init__(self):
        try:
            self.db_conn = mysql.connector.connect(user="root", password="1234",
                                                   host="localhost", database="Books")
            self.cursor = self.db_conn.cursor()
            print("vasle !!?")
        except  Exception as e:
            print('nashod: ', e)

    def create_db(self):
        self.db_conn = mysql.connector.connect(user="root", password="1234",
                                               host="localhost")

    def add_book(self, book):

        try:
            query = """INSERT INTO books (title, imgLink, author, _desc, Categories, _Year, Edition, Publisher, 
            _Language, Pages, ISBN_10, ISBN_13, File, IPFS_CID, IPFS_CID_blake2b, Series) VALUES (%s,%s,%s,%s,%s
            ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            self.cursor.execute(query, book)
            self.db_conn.commit()
            print("ezafe shod !!?")
        except  Exception as e:
            print('add nashod: ', e)

    def get_all_books(self):
        try:
            query = "SELECT * FROM books"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            result = []
            for row in rows:
                d = {}
                for i, col in enumerate(self.cursor.description):
                    d[col[0]] = row[i]
                result.append(d)

            # Convert the list of dictionaries to JSON
            json_result = json.dumps(result)
            return json_result
        except  Exception as e:
            print('nashod: ', e)

    def close(self):
        try:
            self.cursor.close()
            self.db_conn.close()
            print('tamam')
        except  Exception as e:
            print('nashod: ', e)
