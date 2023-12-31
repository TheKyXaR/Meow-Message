# Server

import keyboard
import socket
import sqlite3
import json

con = sqlite3.connect("db.db")
cur = con.cursor()

sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen()

def close_server () :
	sock.close()
keyboard.add_hotkey("ctrl+shift+c", close_server)

def insert (data) :
	cur.execute(f"INSERT INTO message (user, data) VALUES ('{data['nickname']}', '{data['data']}')")
	con.commit()

def insert (data) :
	cur.execute(f"INSERT INTO message (user, data) VALUES ('{data['nickname']}', '{data['message']}')")
	con.commit()

data = {
	"answer": ""
}

while True :
	user, addr = sock.accept()
	data = json.loads(user.recv(1024).decode("utf-8"))

	if data['command'] == "select" :
		res = cur.execute("SELECT user, data FROM message").fetchmany(150)

	elif data['command'] == "insert" :
		res = insert(data)

	user.send(json.dumps(res).encode("utf-8"))

	

	
	# 	# print(data)

	# user.send(json.dumps(res).encode("utf-8"))
	