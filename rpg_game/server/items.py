import random

class Weapon:
	def __init__(self,name:str,damage:int,accuracy:int)->None:
		self.name=name
		self.damage=damage
		self.accuracy=accuracy

	def show_description(self)->None:
		return '%s:{dano:%.2i, precisão:%.1f}'%(self.name,self.damage,self.accuracy/10)

	def attack(self)->int:
		if random.randint(0,1000)<=self.accuracy:
			return self.damage
		else:
			return 0

class Adaga(Weapon):
	def __init__(self)->None:
		super().__init__('adaga',45,910)

class Espada_de_mao(Weapon):
	def __init__(self)->None:
		super().__init__("espada de mão",135,700)

class Espadao(Weapon):
	def __init__(self)->None:
		super().__init__("espadão",210,410)

class Arco_recurvo(Weapon):
	def __init__(self)->None:
		super().__init__("arco recurvo",250,300)

class Arco_longo(Weapon):
	def __init__(self)->None:
		super().__init__("arco longo",280,430)

class Mosquete(Weapon):
	def __init__(self)->None:
		super().__init__('mosquete',400,230)

weapon_names=(Adaga,Espada_de_mao,Espadao,Arco_recurvo,Arco_longo,Mosquete)
