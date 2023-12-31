import json
import socket

from json.decoder import JSONDecodeError

def create_config () :
	while True:
		try :
			with open("config.json", "r", encoding = "utf-8") as file :
				try :
					config = json.loads(file.read())
					break
				except JSONDecodeError :
					raise FileNotFoundError
				

		except FileNotFoundError :
			config = {
				"nickname": input("enter your nickname - "),
				"server": "5.tcp.eu.ngrok.io",
				"port": 12995
			}
			with open('config.json', 'w') as file :
				json.dump(config, file, separators = (',', ':') ,indent = 4, ensure_ascii = False)

	return config

def server (server, port, data) :
	if not data :
		return

	sock = socket.socket()
	sock.connect((server, port))

	sock.send(data.encode("utf-8"))

	result = sock.recv(1024)
	return result.decode("utf-8")
	sock.close()