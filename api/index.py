from flask import Flask, jsonify
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
    global id
    id += 1
    message1 = {
        "id": fake.name(),
        "from": fake.email(),
        "subject": fake.sentence(),
        "body": fake.text(),
        "received": time.time()
    }
    message2 = {
        "id": str(id),
        "from": fake.email(),
        "subject": fake.sentence(),
        "body": fake.text(),
        "received": time.time()
    }

    messages = [message1, message2]
    response = {
        "status": "ok",
        "timestamp": time.time(),
        "messages": messages
    }

    return jsonify(response)
