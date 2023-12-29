import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('7.tcp.eu.ngrok.io', 12304)) # Подключаемся к нашему серверу.

while True :
	data = s.recv(1024)
	print(data.decode("utf-8"))

	# s.sendall('Hello, Habr!'.encode('utf-8')) # Отправляем фразу.
	# data = s.recv(1024) #Получаем данные из сокета.
s.close()