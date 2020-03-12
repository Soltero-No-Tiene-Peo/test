import socket
print('Esperando conexion...')
mensaje='hola'
my_socket = socket.socket()
my_socket.connect(('192.168.2.36',8080))

my_socket.send(mensaje.encode("utf-8"))

respuesta = my_socket.recv(1024)

print (respuesta)
my_socket.close()