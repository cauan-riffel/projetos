import socket
import json
from porta import port


HOST = "127.0.1.1"
PORT = port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))

print('conectado ao servidor!!!!')

valorDeEntrada = ''

status = {
    'vida': 100,
    'dano': 5,
    'equipamentos': {
        'espada': {
            'dano': 12,
            'alcance': 1,
            'precisão': 0.85
        },
        'arco': {
            'dano': 15,
            'alcance': 5,
            'precisão': 0.35
        },
        'escudo': {
            'defesa': 18,
            'precisão': 0.9
        },
        'armadura': {
            'vida': 25,
            'defesa': 8
        }
    }
}
equipamento = 'espada'

while valorDeEntrada == '':
    valorDeEntrada = input('digite sua ação(ajuda mostrará os comandos) ')
    if valorDeEntrada == 'ajuda':
        print('atacar: ataca um unimigo próximo\ndefender: se defende do proximo ataque\nmover: se move para direção determinada\ntrocar: irá trocar para o equipamento determinado!\n')
        valorDeEntrada = ''
        continue

    elif valorDeEntrada == 'atacar':
        jogada = input('digite qual direção você irá atacar(posições)!!!')
        server.sendall(json.dumps((0, status, jogada)).encode())
        resultado = server.recv(2048)
        print(f'-> {resultado} <-')
        resultado = json.loads(resultado)
        valorDeEntrada = ''
        continue

    elif valorDeEntrada == 'trocar':
        for i in status['equipamentos'].keys:
            print(i, end=', ')
        print('\r\r')
        equipamentoAUsar = input('qual equipamento deseja usar?')
        equipamento = equipamentoAUsar
        jogada = ''
        continue

    elif valorDeEntrada == 'defender':
        server.sendall((1, status))
        resultado = server.recv(1024)
        jogada = ''
        continue

    elif valorDeEntrada == 'sair':
        break

    else:
        print('valor inserido incorretamente!!!!')
        valorDeEntrada = ''
        continue
server.close()