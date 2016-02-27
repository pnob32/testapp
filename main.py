#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__, static_url_path='')

books = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/book/<book_id>')
def get_book(book_id):
    b = {}
    for cur in books:
        if cur['id'] == int(book_id):
            b = cur 
    return jsonify(b) 

@app.route('/books', methods=['GET'])
def get_books():
    return json.dumps(books)

@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
