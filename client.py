from flask import Flask, Response, request
import json

app = Flask(__name__)

class Player:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.leader = None
        self.following = []
        self.hand = []

@app.route("/start_game")
def start_game():
    print("starting game")

print("")