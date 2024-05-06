from flask import Flask, jsonify
import json
import time
from faker import Faker
from apscheduler.schedulers.background import BackgroundScheduler
from flask_cors import CORS

fake = Faker()
app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

json_objects = []

def generate_new_object():
    new_json_object = {
        "id": fake.name(),
        "from": fake.email(),
        "subject": fake.sentence(),
        "body": fake.text(),
        "received": time.time()
    }
    if len(json_objects) >= 10:
        json_objects.pop(0)  # Remove the oldest object if the list is larger than 10
    json_objects.append(new_json_object)

generate_new_object()  # Generate the initial JSON object

scheduler = BackgroundScheduler()
scheduler.add_job(generate_new_object, 'interval', seconds=1)
scheduler.start()

@app.route('/')
def home():
    return 'Hello!'

@app.route('/messages/unread')
def about():
    response = {
        "status": "ok",
        "timestamp": time.time(),
        "messages": json_objects
    }

    return jsonify(response)
