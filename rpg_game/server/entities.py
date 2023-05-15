from items import Weapon,create_weapon

class Character:
  def __init__(self,name:str,equipment:Weapon,life:int=200)->None:
    self.name=name
    self.equipment=equipment
    self.life=life
    self.MAX_LIFE=life

  def receive_attack(self, damage:int)->bool:
    '''
    return True if this character is dead
    '''
    self.life-=damage
    if self.life<=0:
      return True
    else:
      return False

  def attack(self)->float:
    return self.equipment.attack()

  def show_status(self):
    print('nome: %s\nvida: %.2f/%.2f'%(self.name,self.life,self.MAX_LIFE))
    self.equipment.show_description()


enemy_names=('mercenario','esqueleto','elfo','elfo negro','ogro','Mazzutti')

class Enemy:
  def __init__(self,name:str,life:int,equipment:Weapon,description:str) -> None:
    self.name=name
    self.life=life
    self.equipment=equipment 
    self.description=description

  def receive_attack(self, damage:int)->bool:
    '''
    return True if this enemy is dead
    '''
    self.life-=damage
    if self.life<=0:
      return True
    else:
      return False

  def attack(self):
    return self.equipment.attack()


def create_enemy(name:str)->Enemy:
  if name=='mercenario':
    return Enemy(name,100,create_weapon('adaga'),'Este mercenário esta disposto a tudo para pilhar aqueles no seu caminho com sua adaga')
  elif name=='esqueleto':
    return Enemy(name,150,create_weapon('espada de mão'),'Um esqueleto humano sedento por carne de humanos que quando você menos espera, ataca você com sua espada de mão')
  elif name=='ogro':
    return Enemy(name,250,create_weapon('espadão'),'Um ser que usa de força bruta que utiliza um grande espadão')
  elif name=='elfo':
    return Enemy(name,200,create_weapon('arco curvo'),'Um elfo arqueiro que usa apenas de sua habilidade para matar aqueles a sua volta utilizando um arco curvo')
  elif name=='elfo negro':
    return Enemy(name,250,create_weapon('arco longo'),'Um elfo negro arqueiro que mata todos aqueles em seu caminho utilizando um arco longo')
  else:
    return Enemy(name,5000,create_weapon('mosquete'),'um carecão lindo pelado com o mosquetão de fora vindo te pegar')
