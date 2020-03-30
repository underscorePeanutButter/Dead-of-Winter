from flask import Flask, Response, request
import json
import socket
import requests

server_address = input("Server address? ")

while True:
    print("1. Create new game")
    print("2. Join existing game")
    choice = input("? ")

    if choice == "1":
        number_of_players = input("Number of players? ")
        address = socket.gethostbyname(socket.gethostname())

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
        
        response = requests.put(server_address + "/games/" + str(id))

        status = response.status_code

        if status == 200:
            print("Game joined successfully!")
        else:
            print("Something went wrong... please try again.")


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
