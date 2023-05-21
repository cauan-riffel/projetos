import map_and_entities as m_e_e
import items
from data import create_server,IP,HOST
from _thread import start_new_thread
import socket
import json

def send(server:socket.socket, data):
	server.send(str.encode(json.dumps(data)))

def create_map(name:str)->m_e_e.Game_map:
	references:dict[str,m_e_e.Game_map]={
		'Wolf_cave':m_e_e.Wolf_cave,
		'Dark_forest':m_e_e.Dark_forest,
		'Haunted_house':m_e_e.Haunted_house,
		'Destroyed_village':m_e_e.Destroyed_village,
		'Holy_forges':m_e_e.Holy_forges,
		'Holy_temple':m_e_e.Holy_temple,
		'Witch_caves':m_e_e.Witch_caves,
		'Golem_ruin':m_e_e.Golem_ruin,
		'Angel_caves':m_e_e.Angel_caves,
		'Rotational_forge':m_e_e.Rotational_forge,
		'Short_sighted_cave':m_e_e.Short_sighted_cave
	}
	game_map:m_e_e.Game_map=references[name]()
	
	return game_map

def get_map_infos(map:m_e_e.Game_map,ip:int)->dict:
	map_info:dict={
		'description':map.show_local(),
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
	if map.gift!=None:
		map_info['gif']['achieved']=True
		map_info['gif']['name']=map.gift.name
		for i in user_inventory[ip]:
			if i==map.gift.name:
				map_info['gif']['repeated']=True
		if not map_info['gif']['repeated']:
			user_inventory[ip].append(map.gift.name)
	elif map.enemy!=None:
		map_info['enemy']['achieved']=True
		map_info['enemy']['name']=map.enemy.name
		map_info['enemy']['description']=map.enemy.description
	return map_info


def cliente(conn:socket.socket,client:tuple[int]):
	while True:
		data:bytes=conn.recv(1024)
		if not data:
			continue
		else:
			try:
				data:list=json.loads(json.loads(data))
			except:
				data:list=json.loads(data)
		action,datas=data[0],data[1:]
		if action=='GN':#?(funcionando)get names
			names:list[str]=[]
			for i in users:
				names.append(i.name)
			send(conn,names)

		elif action=='CC':#?(funcionando)create character
			character=m_e_e.Character(datas[0],items.Adaga(),create_map('Wolf_cave'))
			users.append(character)
			characters[client[1]]=character
			user_inventory[client[1]]=[character.used_equipment.name]

		if action=='GW':#?(funcionando)get weapons
			equips:list[str]=[]
			for i in user_inventory[client[1]]:
				equips.append(i)
			send(conn,equips)

		elif action=='US':#?(funcionando)use
			for i in users:
				if i.name==datas[0]:
					characters[client[1]]=i
					saved:bool=False
					for j in user_inventory.keys():
						if j==client:
							user_inventory[client[1]].append(j.used_equipment)
							saved=True
							break
					if not saved:
						user_inventory[client[1]]=[i.used_equipment]

		elif action=='MI':#?(funcionando)map infos
			map_moves=get_map_infos(characters[client[1]].map,client[1])
			send(conn,map_moves)

		elif action=='AT':#?{funcionando}attack
			character=characters[client[1]]
			enemy=character.map.enemy
			enemy_damage:int
			character_damage=character.attack()
			if not enemy.receive_attack(character_damage):
				enemy_damage=enemy.attack()
				if not character.receive_attack(enemy_damage):
					send(conn,'["ND",%i,%i]'%(character_damage,enemy_damage))
				else:
					send(conn,'["CD",%i,%i]'%(character_damage,enemy_damage))
			else:
				send(conn,'["ED",%i]'%character_damage)
				character.life=character.MAX_LIFE

		elif action=='MV':#move
			map_moves=characters[client[1]].map.move_possibilities
			send(conn,list(map_moves))
			try:
				local=json.loads(json.loads(conn.recv(1024)))
			except:
				local=json.loads(conn.recv(1024))
			translate={
				'floresta negra':'Dark_forest',
				'casa assombrada':'Haunted_house',
				'vila destruída':'Destroyed_village',
				'forjas sagradas':'Holy_forges',
				'templo sagrado':'Holy_temple',
				'caverna dos bruxos':'Witch_caves',
				'ruina dos golens':'Golem_ruin',
				'caverna dos anjos':'Angel_caves',
				'forja rotacional':'Rotational_forge',
				'caverna de visão curta':'Short_sighted_cave',
			}
			characters[client[1]].map=create_map(translate[local[0]])


		elif action=='UW':#?{funcionando}use weapon
			references={
				'adaga':items.Adaga,
				'Arco recurvo':items.Arco_recurvo,
				'espada de mão':items.Espada_de_mao,
				'espadão':items.Espadao,
				'arco longo':items.Arco_longo,
				'mosquete':items.Mosquete
			}
			characters[client[1]].used_equipment=references[datas[0]]()

		elif action=='GS':#?{funcionando}get status
			send(conn,characters[client[1]].show_status(user_inventory[client[1]]))

"""
* 3: mover-se pelo caminho
* 4: atacar inimigo
"""

users:list[m_e_e.Character]=[
	m_e_e.Character('Guest', items.Mosquete(), create_map('Wolf_cave'))
]
user_inventory:dict[int,list[str]]={}
locals:dict[int,m_e_e.Game_map]={}
characters:dict[int,m_e_e.Character]={}


server:socket.socket=create_server(IP,HOST)
threads=[]
try:
	while True:
		conn,client=server.accept()
		print(f'client connected on {client[0]}:{client[1]}')
		threads.append(start_new_thread(cliente,(conn,client)))
		
except KeyboardInterrupt:
	server.close()
