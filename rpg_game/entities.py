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


enemy_names=('mercenario','esqueleto','elfo','mago','ogro','Mazzutti')

class Enemy:
	def _innit_(self, name:str, life:int, equipment:Weapon, description:str) -> None:
		self.name = name
		self.life = life
		self.equipment = equipment 
		self.description = description
        
	def attack(self):
		return self.equipment.attack()    


def create_enemy(name:str)->Enemy:
  if name=='mercenario':
    return Enemy(name,50, create_weapon('adaga'), 'Este mercenário esta disposto a tudo para pilhar aqueles no seu caminho')
  elif name=='esqueleto':
    return Enemy(name,50, create_weapon('espada de mão'), 'Um esqueleto humano sedento por carne de humanos')
  elif name=='ogro':
    return Enemy(name,50, create_weapon('espadão'), 'Um ser que usa de força bruta que utiliza ')
  elif name=='elfo':
    return Enemy(name,50, create_weapon('arco curvo'), 'Um elfo arqueiro que usa apenas de sua habilidade para matar aqueles a sua volta')
  elif name=='mago':
    return Enemy(name,50, create_weapon('arco longo'), 'Um mago arqueiro que mata todos aqueles em seu caminho utilizando flechas encantadas')
  else:
    return Enemy(name,50, create_weapon('mosquete'),'um carecão lindo pelado com o mosquetão de fora vindo te pegar' )
