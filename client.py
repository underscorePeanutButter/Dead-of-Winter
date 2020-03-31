from flask import Flask, Response, request
import json
import socket
import requests

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

@app.route("/messages", methods=["POST"])
def receive_message():
    message_info = json.loads(request.json)
    
    sender = message_info["sender"]
    message = message_info["message"]

    print(sender + ": " + message)

    return Response(status=200)

server_address = input("Server address? ")

while True:
    print("1. Create new game")
    print("2. Join existing game")
    choice = input("? ")

    if choice == "1":
        number_of_players = input("Number of players? ")

        game_info = {"number_of_players": int(number_of_players)}
        response = requests.post(server_address + "/games", json=json.dumps(game_info))

        game_info = response.json()
        status = response.status_code

        id = game_info["id"]

        if status == 201:
            print("Game successfully created!")
            print("Game id: " + str(id))
        else:
            print("Something went wrong... please try again.")
    elif choice == "2":
        id = input("Game id? ")
        name = input("Nickname? ")
        port = input("Port (defaults to 5000)? ")
        if port == "": 
            port = "5000"
        address = "http://" + socket.gethostbyname(socket.gethostname()) + ":" + port
        
        player_info = {"name": name, "address": address}
        response = requests.put(server_address + "/games/" + str(id), json=json.dumps(player_info))

        status = response.status_code

        if status == 200:
            print("Game joined successfully!")
            break
        else:
            print("Something went wrong... please try again.")