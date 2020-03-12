import sys
import socket

my_socket = socket.socket()
my_socket.bind(('192.168.2.36', 8080))
my_socket.listen(5)
mensaje='Hola'
while True:
	conexion, address = my_socket.accept()
	print('Nueva conexion establecida')
	print(address)

	conexion.send(mensaje.encode("utf-8"))
	conexion.close()