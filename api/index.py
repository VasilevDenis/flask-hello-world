from flask import Flask, jsonify
from faker import Faker
import time

fake = Faker()
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello!'

@app.route('/messages/unread')
def about():
    

    # Using list comprehension to create a list of message dictionaries
    messages = [
        {
            "id": fake.name(),
            "from": fake.email(),
            "subject": fake.sentence(),
            "body": fake.text(),
            "received": time.time()
        }
        for _ in range(5)  # Number of messages to generate (2 in this case)
    ]

    response = {
        "status": "ok",
        "timestamp": time.time(),
        "messages": messages
    }

    return jsonify(response)
