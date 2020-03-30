from flask import Flask, Response, request
import json
import random

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

def shuffle(deck):
    return random.shuffle(deck)

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

    if id >= len(games) or id < 0:
        return Response(status=406)

    games[id].players.append(Player(player_info["name"], player_info["address"]))
    
    return Response(status=200)