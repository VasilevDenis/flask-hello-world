from flask import Flask, jsonify
from faker import Faker
import time
from flask_cors import CORS

fake = Faker()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

messages = []

@app.route('/')
def home():
    return 'Hello!'

@app.route('/messages/unread')
def about():
    global messages

    if len(messages) >= 10:
        messages.pop(0)  # Remove the oldest message if the list is larger than 10

    new_message = {
        "id": fake.name(),
        "from": fake.email(),
        "subject": fake.sentence(),
        "body": fake.text(),
        "received": time.time()
    }
    
    messages.append(new_message)

    response = {
        "status": "ok",
        "timestamp": time.time(),
        "messages": messages
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
