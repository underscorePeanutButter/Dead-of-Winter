from flask import Flask, Response, request
import json
import random
import requests
import threading
import time

app = Flask(__name__)

games = []
message_queue = []

class Game:
    def __init__(self, id, number_of_players):
        self.id = id

        self.number_of_players = number_of_players
        self.players = []
        self.locations = []

class Player:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.leader = None
        self.following = []
        self.hand = []

class Location:
    def __init__(self, name):
        self.name = name
        
        self.survivors = []
        self.items = []
        self.entrances = []

class Entrance:
    def __init__(self, size):
        self.size = size
        
        self.zombies = 0

def add_message(id, sender, message):
    message_info = {"id": id, "sender": sender, "message": message}
    message_queue.append(message_info)

def handle_messages():
    while True:
        if len(message_queue) > 0:
            send_message(message_queue[0])
            message_queue.pop(0)
        else:
            time.sleep(1)

def send_message(message_info):
    for player in games[int(message_info["id"])].players:        
        requests.post(player.address + "/messages", json=json.dumps(message_info))

@app.route("/games", methods=["GET"])
def get_games():
    return Response(status=200)

@app.route("/games", methods=["POST"])
def create_game():
    game_settings = json.loads(request.json)

    if game_settings["number_of_players"] < 6 and game_settings["number_of_players"] > 1:
        games.append(Game(str(len(games)), game_settings["number_of_players"]))

        response_data = {"id": games[-1].id}
        return Response(response=json.dumps(response_data), status=201, mimetype="application/json")
    
    return Response(status=406)

@app.route("/games/<id>", methods=["GET"])
def get_game_info(id):
    return Response(status=200)

@app.route("/games/<id>", methods=["POST"])
def update_game_info(id):
    return Response(status=200)

@app.route("/games/<id>", methods=["PUT"])
def join_game(id):
    player_info = json.loads(request.json)

    if int(id) >= len(games) or int(id) < 0:
        return Response(status=406)

    games[int(id)].players.append(Player(player_info["name"], player_info["address"]))
    
    add_message(id, "Server", games[int(id)].players[-1].name + " has joined.")

    if len(games[int(id)].players) == games[int(id)].number_of_players:
        start_game(id)

    return Response(status=200)

message_thread = threading.Thread(target=handle_messages)
message_thread.start()