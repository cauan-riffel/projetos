from socket import socket, AF_INET, SOCK_STREAM
from datas import local

server=socket(AF_INET,SOCK_STREAM)

server.bind(local)
server.listen(5)
print('server connected on %s:%d'%local)
try:
	while True:
		conn,client=server.accept()
		print(f'client connected in port {client}')
		data=bytes.decode(conn.recv(1024))
except KeyboardInterrupt:
	server.close()
