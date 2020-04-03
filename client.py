import zmq
import time
import json
import socket
import requests
import threading
import survivors

class Player:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

        self.leader = None
        self.following = []
        self.hand = []

def get_new_messages():
    while True:
        message_info = None

        socket.send(str({"id": id, "player_id": profile.id}).encode("utf-8"))

        message_info = socket.recv()

        if message_info:
            if message_info == b"":
                pass
            else:
                message_info = eval(message_info.decode("utf-8"))
                if message_info["message_type"] == "chat":
                    print(message_info["sender"] + ": " + message_info["message"])
                
                if message_info["message_type"] == "starter_survivors":
                    for i in range(len(message_info["message"])):
                        survivor_to_update = message_info["message"][i]
                        message_info["message"].pop(i)
                        message_info["message"].insert(i, eval("survivors." + survivor_to_update))
                    
                    print("You have been dealt the following survivors:")
                    for i in range(len(message_info["message"])):
                        print(str(i) + ". " + message_info["message"][i].name)
                    leader = input("Which survivor is your leader? ")
                    profile.leader = message_info["message"][int(leader)]
                    message_info["message"].pop(int(leader))

                    print("You still have the following survivors:")
                    for i in range(len(message_info["message"])):
                        print(str(i) + ". " + message_info["message"][i].name)
                    follower = input("Which survivor will you put in your following? ")
                    profile.following.append(message_info["message"][int(follower)])

                    requests.post(server_address + "/games/" + id, json=json.dumps({"id": id, "update_type": "starter_survivors", "player_id": profile.id, "cards": {"leader": profile.leader.name.lower().replace(" ", "_"), "follower": profile.following[0].name.lower().replace(" ", "_"), "unused": [survivor.name.lower().replace(" ", "_") for survivor in message_info["message"]]}}))

        else:
            time.sleep(1)

# server_address = input("Server address? ")
# mq_client = input("Message Queue address? ")
server_address = "http://localhost:5000"
mq_client = "tcp://localhost:5555"
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
            profile = Player(name, player_id, address)
            break
        else:
            print("Something went wrong... please try again.")

message_thread = threading.Thread(target=get_new_messages)
message_thread.start()