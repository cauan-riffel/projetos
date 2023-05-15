from socket import socket,create_connection
IP='10.0.19.85'
HOST=25554

def create_client(ip:str,host:int)->socket:
    print('connected on %s:%i'%(ip,host))
    return create_connection((ip,host))
