import random
import items

class Game_map:
	"""
	step:path
		map:
					5:1
			4:1			4:2
			3:1	 3:2	3:3
			2:1			2:2
			1:1			1:2
					0:1
		"""
	def __init__(self,name:str,description:str,step=0,path=1,move_possibilities:tuple[int]=(),chances:tuple[int]=(130,270))->None:
		self.step=step
		self.path=path
		self.name=name
		self.desc=description
		self.event=self._do_event(chances)
		self.gift=None
		self.enemy=None
		if step==5:
			self.move_possibilities=None
		else:
			self.move_possibilities=move_possibilities
		if self.event==1:
			self.gift=random.choice(items.weapon_names)()
		elif self.event==2 or step==5:
			self.enemy=enemy_names[step]()

	def show_local(self)->str:
		last_word=self.name.split(' ')[0][-1]
		end='o'if last_word=='o'else'a'
		return 'você adentrou n%s %s\n%s'%(end,self.name,self.desc)

	def _do_event(self,chances:tuple[int])->int:
		temp=random.randint(0,1000)
		if temp<=chances[0]:
			return 1
		elif temp<=chances[0]+chances[1]:
			return 2
		else:
			return 0
		
	def show_possibilities(self)->str:
		temp
		for i in self.move_possibilities:
			temp+=f'\t{i}'+'\n'
		return temp

class Wolf_cave(Game_map):
	def __init__(self)->None:
		super().__init__('caverna dos lobos','A caverna é um lugar escuro, você ouve goteiras por todo o local e um forte cheiro de carne podre, vinda das vidas que, precocemente foram abatidas enquanto se debatiam em dor.',move_possibilities=(("floresta negra"),("caverna dos bruxos")))

class Dark_forest(Game_map):
	def __init__(self)->None:
		super().__init__('Floresta Negra',"Após sair da caverna você se depara no meio de uma floresta de pinheiros enormes. A neblina cerca o lugar, limitando sua visão, nunca se sabe o que pode estar se escondendo nas trevas deste lugar sombrio.",1,move_possibilities=(("casa assombrada"),))

class Haunted_house(Game_map):
	def __init__(self)->None:
		super().__init__("Casa assombrada","No meio da neblina você encontra uma casa escura cheia de luz, você decide abrir a porta, afinal, ali há menos lugares para os perigos se esconderem, mas também a menos lugar para você se esconder delas.",2,move_possibilities=(("vila destruída"),))

class Destroyed_village(Game_map):
	def __init__(self) -> None:
		super().__init__("Vila Destruída",'Apesar de alguns arranhões e mordidas, você consegue sobreviver a noite na casa e vencer todos os desafios dela. Agora, é hora de desafiar a vila que	a escuridão escondia. Ela está totalmente destruída, como que atacada por uma entidade superior. No chão você vê corpos, um pó de coloração escura que lembrava pólvora e rastros, alguns de sangue, outros de lesma. Você não tem ideia do que aconteceu, apenas sabe de uma coisa: foi brutal.',3,move_possibilities=(("forjas sagradas"),))

class Holy_forges(Game_map):
	def __init__(self)->None:
		super().__init__('Forjas Sagrada',"Após vencer a floresta, você vê uma montanha gigante e decide escalá-la, porém busca abrigo em uma construção ao pé dela. Parece ser uma construção usada por ferreiros, conhecidos por sua habilidade e altos preços cobrados de seus clientes. Lá você confirma suas teorias, vendo um bigorna usada na idade média, algo semelhante a uma luneta coberto por uma substância gelatinosa. Ao lado você encontra também uma carta, destinada a Walter. Ela era de um amigo, que contava como os guardas ouviram vozes em celas vazias da prisão do Rei.",4,move_possibilities=(("templo sagrado"),))

class Holy_temple(Game_map):
	def __init__(self)->None:
		super().__init__("Templo Sagrado", "Em uma vasta planície se encontra um templo, para o qual inúmeras raças veneram. Porém, o que chamou sua atenção à distância não foi o templo em si, mas o ser que estava em sua entrada, possuindo mais de 5 metros de altura, músculos que poderiam facilmente erguer a mais grossa árvore. O que mais chamou a atenção no ser foi a grandiosa habilidade de mudar o percurso da luz, fazendo-a seguir os seus desejos. Mais assustador que seu brilho, era o majestoso mosquete que carregava e sequer fazia esforço algum para escondê-lo da visão de todos, fazendo qualquer um cair de joelhos e orar para a deidade, cujo os atos eram grandiosos sem precedentes que ninguém era capaz de explicar. Realmente, apesar do medo e da imponência que causava, era sem dúvidas uma cena linda de se ver.",5,move_possibilities=(('',),))

class Witch_caves(Game_map):
	def __init__(self)->None:
		super().__init__('caverna dos bruxos','A caverna se torna cada vez mais escura, nela você também sente um pequeno resquício de intenção assassina que cobria todo o local, causando calafrios até mesmo no mais corajoso guerreiro que enfrentava a morte diariamente.',1,2,move_possibilities=(("ruina dos golens"),))

class Golem_ruin(Game_map):
	def __init__(self)->None:
		super().__init__('ruina dos golens', 'As ruínas estão cada vez mais precárias, as estátuas estão incrivelmente desgastadas tornando-se cada vez mais evidente a possibilidade de desprender-se uma rocha da mesma, estes golens eram muito semelhantes um dos outros, possuindo, no lugar da cabeça, rachaduras e em sua cintura algo estranho que nem ao menos você sonhou em possuir em sua vida.',2,2,move_possibilities=(('caverna dos anjos'),('caverna de visão curta')))

class Angel_caves(Game_map):
	def __init__(self)->None:
		super().__init__('Caverna dos anjos','As cavernas se parecem muito com um refúgio que devia ter sido usado durante a guerra divina, nela você encontrará muitos ossos, que ao menor dos toques irá se esfarelar. Nas paredes rachadas você vê desenhos de pessoas adorando seres enormes, alguns com asas e outros com mosquetes.',3,2,move_possibilities=(("forja rotacional"),))

class Rotational_forge(Game_map):
	def __init__(self)->None:
		super().__init__('forja rotacional', 'Ao visualizar uma pequena série de motores, você percebe pequenos raios de luz, mostrando que você está próximos da superfície, porém como não existe almoço grátis, você encontra grandes circunferências presas em algo que parecia ser um barco, estas circunferências são rolões que possuem pequenos fios de vidro.',4,2,move_possibilities=(('templo sagrado'),))

class Short_sighted_cave(Game_map):
	def __init__(self)->None:
		super().__init__('caverna de visão curta','Esta caverna, relativamente avermelhada, possui em suas paredes escrituras muito antigas, porém, com muito esforço você consegue decifrar alguns caracteres	formando a seguinte mensagem: "todos os aqui presentes devem ab#icar dos bens mortais, e div&%i-los, dei@#ndo de la@o a gan$&!ia e a part!r de hoje de$em se t$%nar bol#*eviq!es usufruidores dos pr!dut@s da abençoada ma#ã"',3,3,move_possibilities=(("forja rotacional"),))

class Character:
	def __init__(self,name:str,equipment:items.Weapon,path:Game_map,life:int=600)->None:
		self.name=name
		self.used_equipment=equipment
		self.life=life
		self.MAX_LIFE=life
		self.map=path

	def receive_attack(self, damage:int)->bool:
		'''
		return True if this character is dead
		'''
		self.life-=damage
		if self.life<=0:
			return True
		else:
			return False

	def attack(self)->int:
		return self.used_equipment.attack()

	def show_status(self,equips:list[str])->str:
		equipments_names=''
		for i in equips:
			equipments_names+='\n\t'+i
		return 'nome: %s\nvida: %i/%i\ndescrição do equipamento utilizado:%s\nequipamentos:%s'%(self.name,self.life,self.MAX_LIFE,self.used_equipment.show_description(),equipments_names)

class Enemy:
	def __init__(self,name:str,life:int,equipment:items.Weapon,description:str) -> None:
		self.name=name
		self.life=life
		self.MAX_LIFE=life
		self.equipment=equipment 
		self.description=description

	def receive_attack(self,damage:int)->bool:
		self.life-=damage
		if self.life<=0:
			return True
		else:
			return False

	def attack(self):
		return self.equipment.attack()

	def show_description(self):
		return self.name+self.description

class Mercenario(Enemy):
	def __init__(self)->None:
		super().__init__('mercenario',100,items.Adaga(),'Este mercenário esta disposto a tudo para pilhar aqueles no seu caminho com sua adaga')

class Esqueleto(Enemy):
	def __init__(self) -> None:
		super().__init__("Esqueleto",150,items.Espada_de_mao(),"Um esqueleto	sedento por carne de humanos que quando você menos espera, ataca você com sua espada de mão")	

class Ogro(Enemy):
	def __init__(self) -> None:
		super().__init__("Ogro",250,items.Espadao(),"Um ser que usa de força bruta que utiliza um grande espadão")

class Elfo(Enemy):
	def __init__(self) -> None:
		super().__init__("Elfo",200,items.Arco_recurvo(),"Um elfo arqueiro que usa apenas de sua habilidade para matar aqueles a sua volta utilizando um arco recurvo")

class Elfo_Negro(Enemy):
	def __init__(self,) -> None:
		super().__init__("Elfo Negro", 250,items.Arco_longo(), "Um elfo negro arqueiro que mata todos aqueles em seu caminho utilizando um arco longo")

class Mazzutti(Enemy):
	def __init__(self)->None:
		super().__init__('Mazzutti',15000,items.Mosquete(),'um carecão lindo pelado com o mosquetão de fora vindo te pegar')

		def receive_attack(self,damage:int)->bool:
			self.life-=(damage//2)
			if self.life<=0:
				return True
			else:
				return False

enemy_names=(Mercenario,Esqueleto,Elfo,Elfo_Negro,Ogro,Mazzutti)
