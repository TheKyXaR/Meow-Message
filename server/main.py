# Server

import keyboard
import socket
import json
import db

sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen()

def close_server () :
	sock.close()
keyboard.add_hotkey("ctrl+shift+c", close_server)

def send_message (user, data) :
	user.sendall(data)

while True :
	user, addr = sock.accept()

	data = user.recv(1024).decode("utf-8")
	data = json.loads(data)

	if data['command'] == "select" :
		res = db.select()

	elif data['command'] == "insert" :
		res = db.insert(data)
		# print(data)

	try:
		user.send(json.dumps(res).encode("utf-8"))
	except :
		user.send(str(res).encode("utf-8"))
	

	# try:
	# 	user.send(json.dumps(data).encode("utf-8"))
	# except :
	# 	user.send("False".encode("utf-8"))
	