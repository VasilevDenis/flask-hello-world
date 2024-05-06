from flask import Flask, jsonify
from faker import Faker
import time
from flask_cors import CORS

fake = Faker()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return 'Hello!'

@app.route('/messages/unread')
def about():
    messages = [
        {
            "id": fake.name(),
            "from": fake.email(),
            "subject": fake.sentence(),
            "body": fake.text(),
            "received": time.time()
        }
        for _ in range(5)
    ]

    response = {
        "status": "ok",
        "timestamp": time.time(),
        "messages": messages
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
