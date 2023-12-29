import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
s.listen(1) # Начинаем прослушивать входящие соединения.
 # Метод который принимает входящее соединение.

while True:
	conn, addr = s.accept()

	print("connect")
	conn.send("connect".encode("utf-8"))

	# data = conn.recv(1024) # Получаем данные из сокета.
	# if not data:
	# 	break
	# conn.sendall(data) # Отправляем данные в сокет.
	# print(f"{conn}\n{addr}\n{data.decode('utf-8')}")
conn.close()