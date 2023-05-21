from data import create_conn,IP,HOST
from time import sleep
import json,socket

def get_type(palavra:str)->str:
	if palavra.split(' ')[0][-1]=='a':
		return 'a'
	else:
		return ''

def send(server:socket, data):
	server.send(str.encode(json.dumps(data)))

def change_map(game_vars:dict,values:dict[str:any]):
	print('\n\n'+values['description'])
	if values['gif']['achieved']:
		print('\n\nvocê não encontrou nenhum inimigo neste local')
		last:str=get_type(values['gif']['name'])
		print('você achou um%s %s'%(last,values['gif']['name']))
	elif values['enemy']['achieved']:
		game_vars['enemy']['achieved']=True
		game_vars['enemy']['name']=values['enemy']['name']
		game_vars['enemy']['description']=values['enemy']['description']

		conector:str='um'
		if game_vars['enemy']['name']=='Mazzutti':
			conector='o'
		print('você encontrou %s %s\ndescrição:%s'%(conector,game_vars['enemy']['name'],game_vars['enemy']['description']))
	else:
		print('Você não encontrou nada anormal aqui!')
	print('\n')
	return


try:
	map_infos={
		'enemy':{
			'achieved':False,
			'name':'',
			'description':''
		},
	}

	server=create_conn(IP,HOST)
	account=input('você possui conta? ')
	if account in 'simSIMYESyes':
		send(server,'["GN"]')
		nickname=input('qual seu nickname? ')
		nicknames=json.loads(server.recv(2048))

		while nickname not in nicknames:
			print('nickname incorreto!!!')
			nickname=input('qual seu nickname? ')
		send(server,'["US","%s"]'%nickname)
	else:
		nickname=input('digite o nome do seu personagem: ')
		send(server,'["CC","%s"]'%nickname)

	sleep(0.05)
	send(server,'["MI",""]')
	server_return=json.loads(server.recv(2048))
	print(server_return)
	change_map(map_infos,server_return)
	

	while True:
		data=input('qual ação deseja realizar? ')
		if map_infos['enemy']['achieved']==True:
			if data=='ajuda':
				print('atacar: ataca o inimigo que esta com você\ntrocar equipamento: permite que você troque de equipamento caso possua mais de 1')
			elif data=='atacar':
				send(server,'["AT",""]')
				infos=json.loads(json.loads(server.recv(1024)))
				print(type(infos))
				if infos[0]=='ED':
					print('você causou %i de dano e o derrotou!'%(infos[1]))
					map_infos['enemy']['achieved']=False
				elif infos[0]=='CD':
					if infos[1]==0:
						print('você errou o ataque!!!')
						print('o %s causou-lhe %i de dano e derrotou o jogador!')
						print('você foi derrotado!!!!')
						raise KeyboardInterrupt
					else:
						print('você causou %i de dano!!!'%infos[1])
						print('o %s causou-lhe %i de dano e derrotou o jogador!')
						print('você foi derrotado!!!!')
						raise KeyboardInterrupt
				else:
					if infos[2]!=0:
						print('você causou %i de dano no %s, que causou-lhe %i de dano!'%(infos[1],map_infos['enemy']['name'],infos[2]))
					else:
						print('você causou %i de dano no %s que errou seu ataque')

			elif data=='trocar equipamento':
				send(server,'["GW",""]')
				equipments:list[str]=json.loads(server.recv(1024))
				if len(equipments)!=1:
					print('equipamentos: ')
					for i in equipments:
						print(i)
					equipment:str
					while equipment not in equipments:
						equipment=input('qual o nome do equipamento que você quer usar? ')
						if equipment not in equipments:
							print('valor inserido incorreto!\n')
				else:
					print('você apenas possui uma Adaga')

			else:
				print('valor de entrada incorreto!!!\n')
		else:
			if data=='ajuda':
				print('trocar equipamento: permite que você troque de equipamento coso possua mais de 1.\nmovimentar: permite que você se movimente para qualquer lugar possivel no mapa',end='\n\n')
				continue
			elif data=='trocar equipamento':
				send(server,'["GW",""]')
				equipments=json.loads(server.recv(1024))
				if len(equipments)!=1:
					print('armas: ')
					for i in equipments:
						print(i, end='\n\t')
					name:str
					while name not in equipments:
						name=input('qual arma deseja usar? ')
					
				else:
					print('você apenas possui uma Adaga')
			elif data=='movimentar':
				continue

			else:
				print('entrada inválida!!!\n')
except KeyboardInterrupt:
	print('você está saindo do servidor')
	server.close()

print('você saiu do servidor!!!')
