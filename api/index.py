from flask import Flask, jsonify
from faker import Faker
from datetime import datetime
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
    current_datetime = datetime.now()

    if len(messages) >= 100:
        messages.pop(0)

    new_message = {
        "id": fake.name(),
        "from": fake.email(),
        "subject": fake.sentence(),
        "body": fake.text(),
        "received": current_datetime
    }
    
    messages.append(new_message)

    response = {
        "status": "ok",
        "timestamp": current_datetime,
        "messages": messages
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
