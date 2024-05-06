from flask import Flask
from faker import Faker
import time


fake = Faker()
app = Flask(__name__)
id = 0

@app.route('/')
def home():
    return 'Hello!'

@app.route('/messages/unread')
def about():
    id +=1
    return f'''{
              "status": "ok",
              "timestamp": {time.time()},
              "messages": [
                {
                  "id": {fake.name()},
                  "from": {fake.email()},
                  "subject": {fake.sentence()},
                  "body": {fake.text()},
                  "received": {time.time()}
                }
                {
                  "id": {str(id)},
                  "from": {fake.email()},
                  "subject": {fake.sentence()},
                  "body": {fake.text()},
                  "received": {time.time()}
                },
                ...
              ]
            }'''
