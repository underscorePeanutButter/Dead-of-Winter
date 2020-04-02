import zmq
import time
import json
import socket
import requests
import threading
import survivors

class Player:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.leader = None
        self.following = []
        self.hand = []

def get_new_messages():
    while True:
        message_info = None

        socket.send(str({"id": id, "player_id": player_id}).encode("utf-8"))

        message_info = socket.recv()

        if message_info:
            if message_info == b"":
                pass
            else:
                message_info = eval(message_info.decode("utf-8"))
                if message_info["message_type"] == "chat":
                    print(message_info["sender"] + ": " + message_info["message"])
                
                if message_info["message_type"] == "starter_survivors":
                    pass

        else:
            time.sleep(1)

server_address = input("Server address? ")
mq_client = input("Message Queue address? ")
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(mq_client)

while True:
    print("1. Create new game")
    print("2. Join existing game")
    choice = input("? ")

    if choice == "1":
        number_of_players = input("Number of players? ")

        game_info = {"number_of_players": int(number_of_players)}
        response = requests.post(server_address + "/games", json=json.dumps(game_info))

        status = response.status_code

        if status == 201:
            game_info = response.json()
            id = game_info["id"]
            print("Game successfully created!")
            print("Game id: " + str(id))
        else:
            print("Something went wrong... please try again.")
            
    elif choice == "2":
        id = input("Game id? ")
        name = input("Nickname? ")
        address = ""

        player_info = {"name": name, "address": address}
        response = requests.put(server_address + "/games/" + str(id), json=json.dumps(player_info))

        status = response.status_code

        if status == 200:
            print("Game joined successfully!")
            player_id = response.json()["id"]
            break
        else:
            print("Something went wrong... please try again.")

message_thread = threading.Thread(target=get_new_messages)
message_thread.start()