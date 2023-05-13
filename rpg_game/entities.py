import random as r
import json
class Personagem:
	def __init__(self,nome:str,vida:int=100,dano:int=5,equipamentos:list[dict[str,int]]=[])->None:
		self.nome=nome
		self.vida=vida
		self.dano=dano
		if len(equipamentos)!=0:
			self.equip=equipamentos
		else:
			self.equip={
				'equipamentos': {
					'espada':{'dano':12,'alcance':1,'precisao':0.85},
					'arco':{'dano':15,'alcance':5,'precisao':0.35},
					'escudo':{'defesa':18,'precisao':0.9}
				}[r.choice(('espada','arco','escudo'))]
			}

	def encode(self):
		return json.dumps({
			'vida':self.vida,'dano':self.dano,'equipamentos':self.equip
		}).encode()
	





'''

abrir inventário
vender itens
comprari itens
inimigos
regiões #!protótipo de mapa

'''
