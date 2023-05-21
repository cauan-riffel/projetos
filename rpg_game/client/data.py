from socket import socket,create_connection
IP='10.0.0.143'
HOST=25555

def create_conn(ip:str,host:int)->socket:
	print('connected on %s:%i'%(ip,host))
	return create_connection((ip,host))
