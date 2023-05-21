import socket
IP='10.0.0.143'
HOST=25555

"""
* 0: criar personagem
* 1: acessar personagem
* 2: mover-se pelo caminho
* 3: atacar inimigo
"""


def create_server(ip:str,host:int)->socket.socket:

	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	server.bind((ip,host))
	server.listen(5)

	print('server connected on %s:%d'%(ip,host))
	return server
