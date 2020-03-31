from flask import Flask, Response, request
import json
import requests

app = Flask(__name__)

message_queue = []

def handle_messages():
    while True:
        if len(message_queue) > 0:
            pass

@app.route("/", methods=["POST"])
def receive_message():
    message_info = json.loads()