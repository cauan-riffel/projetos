import socket
import json
from signal import signal, SIGPIPE, SIG_DFL  
from porta import port


signal(SIGPIPE,SIG_DFL)

HOST = socket.gethostbyname(socket.gethostname())
PORT = port

local = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
server.bind(local)
server.listen()
print('servidor iniciado na porta %s'%(str(local[0])+':'+str(local[1])))
conection, endereco = server.accept()
print(f'conectado com {endereco}')
server.listen(5)
while True:
    data = json.loads(conection.recv(1024))
    if data[0] == 0:
        val = json.dumps(('dados do jogo', 'dano causado/ataque incorreto')).encode()
        server.sendall(val)
