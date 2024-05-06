from flask import Flask, jsonify
from faker import Faker
from datetime import datetime
from flask_cors import CORS
import time

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
        "received": datetime.now().timestamp()
    }
    
    messages.append(new_message)

    response = {
        "status": "ok",
        "timestamp": datetime.now().timestamp(),
        "messages": messages
    }

    time.sleep(1)  # Add a 1-second delay before the next message is created

    return jsonify(response)

if __name__ == '__main__':
    app.run()
