from flask import Flask, Response, request
import zmq
import json
import random
import requests
import threading
import time
import survivors

app = Flask(__name__)
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

games = []
message_queue = []

survivor_deck = []

class Game:
    def __init__(self, id, number_of_players):
        self.id = id

        self.number_of_players = number_of_players
        self.players = []
        self.locations = []

class Player:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
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

def add_message(id, message_type, sender, recipient, message):
    message_info = {"id": id, "message_type": message_type, "sender": sender, "recipient": recipient, "message": message, "times_requested": 0}
    message_queue.append(message_info)

def handle_messages():
    while True:
        message_request = socket.recv()

        time.sleep(1)

        if len(message_queue) > 0:
            message_info = eval(message_request.decode("utf-8"))

            if message_info["id"] == message_queue[0]["id"]:
                if message_queue[0]["recipient"] == "all":
                    send_message(message_queue[0])

                    message_queue[0]["times_requested"] += 1
                    if message_queue[0]["times_requested"] >= len(games[int(message_queue[0]["id"])].players):
                        message_queue.pop(0)

                elif message_info["player_id"] == message_queue[0]["recipient"]:
                    send_message(message_queue[0])
                    message_queue.pop(0)
                else:
                    send_message("")

            else:
                send_message("")

        else:
            send_message("")

def send_message(message_info):
    socket.send(str(message_info).encode("utf-8"))

def start_game(id):
    add_message(id, "chat", "Server", "all", "All players have joined.")
    add_message(id, "chat", "Server", "all", "Preparing cards...")
    create_decks()
    add_message(id, "chat", "Server", "all", "Dealing starter survivors...")

    starter_survivors = []
    for i in range(len(games[int(id)].players)):
        for j in range(4):
            starter_survivors.append(survivor_deck[0].name.lower().replace(" ", "_"))
            survivor_deck.pop(0)

        add_message(id, "starter_survivors", "Server", i, starter_survivors)
        starter_survivors = []

def shuffle_deck(deck):
    random.shuffle(deck)

    return deck

def create_decks():
    global survivor_deck

    survivor_deck = shuffle_deck(survivors.characters)


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

    games[int(id)].players.append(Player(player_info["name"], len(games[int(id)].players), player_info["address"]))
    
    add_message(id, "chat", "Server", "all", games[int(id)].players[-1].name + " has joined.")

    if len(games[int(id)].players) == games[int(id)].number_of_players:
        start_game(id)

    response_data = {"id": games[int(id)].players[-1].id}

    return Response(response=json.dumps(response_data), status=200, mimetype="application/json")

message_thread = threading.Thread(target=handle_messages)
message_thread.start()