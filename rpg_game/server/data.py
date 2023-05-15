from socket import socket,AF_INET,SOCK_STREAM,create_connection
IP='10.0.19.85'
HOST=25554

"""
* 0: criar personagem
* 1: acessar personagem
* 2: mover-se pelo caminho
* 3: atacar inimigo
"""


def create_server(ip:str,host:int)->socket:
    local=(ip,host)

    server=socket(AF_INET,SOCK_STREAM)
    server.bind(local)
    server.listen(5)

    print('server connected on %s:%d'%local)
    return server
