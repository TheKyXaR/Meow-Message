#User

import socket
import json
import time
import functions
import keyboard
from os import system as sys

config = functions.create_config()

data = {
	"command": "select",
	"nickname": config["nickname"],
	"message": ""
}

def input_message () :
	global data

	message = input()
	data["command"] = "insert"
	data["message"] = message
	res = json.dumps(data)
	functions.server(config['server'], config['port'], res)

keyboard.add_hotkey("enter", input_message)

while True :
	time.sleep(1)

	data["command"] = "select"

	inp = functions.server(config['server'], config['port'], json.dumps(data))
	inp = json.loads(inp)

	sys('cls')
	print("\n".join([" >>>   ".join(x) for x in inp]))



# with open('config.json', 'w') as file :
# 	pass