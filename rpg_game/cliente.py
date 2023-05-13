from socket import create_connection
from datas import local

server=create_connection(local)
server.send(str.encode('teste - aaaaaa'))
