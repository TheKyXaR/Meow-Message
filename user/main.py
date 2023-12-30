# User

import socket
import json
import time
import keyboard
from os import system as sys

def server (message) :
	if not message :
		return

	sock = socket.socket()
	sock.connect(('127.0.0.1', 9090))

	sock.send(message.encode("utf-8"))

	data = sock.recv(1024)
	return data.decode("utf-8")
	sock.close()

data = {
	"command": "select",
	"data": ""
}

messages = ""

def input_message () :
	global data

	message = input()
	data["command"] = "insert"
	data["data"] = message
	res = json.dumps(data)
	server(res)

def main () :
	global data, messages

	keyboard.add_hotkey("enter", input_message)

	print("Hello, welcome to Meow Message")
	data['nickname'] = input("enter your nick name - ")

	check_message_time = time.time()

	while True :
		if time.time() - check_message_time > 0.5 :
			check_message_time = time.time()

			# sys("cls")
			data["command"] = "select"
			res = json.dumps(data)
			
			out_window = server(res)
			out_window = json.loads(out_window)

			sys("cls")

			for x in out_window :
				print(f"{x[0]} >>>   {x[1]}")


		

if __name__ == '__main__':
	main()


"""

{
	"command": "select",
	"sql": {
		"select": "*",
		"from" : "table",
		"where": "",
	}
	"data": {
		"login": input(),
		"password": input(),
	}
}

"""


# while True :
# 	sock = socket.socket()
# 	sock.connect(('127.0.0.1', 9090))

# 	message = input()
# 	if not message :
# 		message = "empty box"

# 	if message == "end connection" :
# 		break
# 	sock.send(message.encode("utf-8"))

# sock.close()