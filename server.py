from flask import Flask, Response, request
import json
import random
import requests

app = Flask(__name__)

games = []

class Game:
    def __init__(self, id, number_of_players):
        self.id = id

        self.number_of_players = number_of_players
        self.players = []

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

def start_game(id):
    for player in games[int(id)].players:
        requests.put(player.address + "/start_game")

def shuffle(deck):
    return random.shuffle(deck)

def send_message(sender, message):
    for player in games[int(id)].players:
        request.post(player.address + "/messages", json={"sender": sender, "message": message})

@app.route("/games", methods=["GET"])
def get_games():
    return Response(status=200)

@app.route("/games", methods=["POST"])
def create_game():
    game_settings = request.json

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
    player_info = request.json

    if int(id) >= len(games) or int(id) < 0:
        return Response(status=406)

    games[int(id)].players.append(Player(player_info["name"], player_info["address"]))
    
    if len(games[int(id)].players) == games[int(id)].number_of_players:
        start_game(id)

    return Response(status=200)