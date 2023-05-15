from map import Game_map,create_map,move_possibilitys
from entities import Character
from items import Weapon,create_weapon
from data import create_server,IP,HOST
from _thread import start_new_thread
from socket import socket
import json


def cilente(conn:socket,client):
	while True:
			data:bytes=conn.recv(1024)
			if not data:
				continue
			else:
				print(data)
				data:list=json.loads(data)

			print(data)
			action,datas=data[0],data[1:]
			if action=='G':
				names:list[str]=[]
				for i in users:
					names.append(i.name)
				conn.send(str.encode(json.dumps(names)))

			elif action=='C':
				character=Character(datas[0],create_weapon('adaga'))
				users.append(character)
				characters[client[1]]=character
				user_inventory[client[1]]=[character.equipment]

			elif action=='U':
				for i in users:
					if i.name==datas[0]:
						characters[client[1]]=i

			elif action=='M':
				locals.update( (client[1],create_map(datas[0],datas[1])) )

				game_map=locals[client[1]]
				map_info={
					'description':game_map.show_local(),
					'gif':{
						'achieved':False,
						'repeated':False,
						'name':''
					},
					'enemy':{
						'achieved':False,
						'name':'',
						'description':''
					}
				}
				if game_map.gift!=None:
					map_info['gif']['achieved']=True
					map_info['gif']['name']=game_map.gift.name
					for i in user_inventory[client[1]]:
						if i==game_map.gif.name:
							map_info['gif']['repeated']=True
					if not map_info['gif']['repeated']:
						user_inventory[client[1]].append(game_map.gift.name)
				elif game_map.enemy!=None:
					map_info['enemy']['achived']=True
					map_info['enemy']['name']=game_map.enemy.name
					map_info['enemy']['description']=game_map.enemy.description
				client.send(str.encode(json.dumps(map_info)))






"""
// 0: criar personagem
// 1: acessar personagem
// 2: usar personagem
* 3: mover-se pelo caminho
* 4: atacar inimigo
"""

users:list[Character]=[
	Character('Guest',create_weapon('mosquete'))
]
user_inventory:dict[int,list[Weapon]]={}
locals:dict[int,Game_map]
characters:dict[int,Character]={}
server=create_server(IP,HOST)

threads=[]


try:
	while True:
		conn,client=server.accept()
		print(f'client connected on {client[0]}:{client[1]}')
		threads.append(start_new_thread(cilente,(conn,client)))
		
except KeyboardInterrupt:
	server.close()
