from flask import Flask, jsonify
from faker import Faker
from datetime import datetime
from flask_cors import CORS
import threading

fake = Faker()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

messages = []
is_running = True

def add_message():
    global messages, is_running

    while is_running:
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
        time.sleep(1)  # Add a 1-second delay before adding the next message

# Start a new thread to continuously add messages
message_thread = threading.Thread(target=add_message)
message_thread.start()

@app.route('/')
def home():
    return 'Hello!'

@app.route('/messages/unread')
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run()
