#!flask/bin/python
from flask import Flask, jsonify
import json

app = Flask(__name__, static_url_path='')

users = [
    {
        'first_name': u'Patrick',
        'last_name': u'Noble',
        'age': 24 
    },
    {
        'first_name': u'Robyn',
        'last_name': u'Cromwell',
        'age': 28 
    }
]

@app.route('/user/<user_id>')
def get_user(user_id):
    b = 'user not found'
    for cur in users:
        if cur['id'] == int(user_id):
            #b = cur 
            b = json.dumps(cur)
    #return json.dumps(b) 
    return b

@app.route('/users', methods=['GET'])
def get_users():
    return json.dumps(users)

@app.route('/helloworld', methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)
