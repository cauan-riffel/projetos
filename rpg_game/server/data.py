import socket
IP='10.0.0.143'
HOST=25554

def create_server(ip:str,host:int)->socket.socket:
	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((ip,host))
	server.listen(5)
	print('server connected on %s:%d'%(ip,host))
	return server
