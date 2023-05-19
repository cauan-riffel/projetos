from items import Weapon,Adaga,Espada_de_mao,Mosquete,Espadao,Arco_longo,Arco_recurvo
from server.items import Weapon

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
    return 'nome: %s\nvida: %.2f/%.2f\ndescrição:%s'%(self.name,self.life,self.MAX_LIFE,self.equipment.show_description())

enemy_names=('mercenario','esqueleto','elfo','elfo negro','ogro','Mazzutti')

class Enemy:
  def __init__(self,name:str,life:int,equipment:Weapon,description:str) -> None:
    self.name=name
    self.life=life
    self.equipment=equipment 
    self.description=description
    '''
    receive_attack return True if this enemy is dead
    '''

  def attack(self):
    return self.equipment.attack()

class Mercenario(Enemy):
  def __init__(self)->None:
    super().__init__('mercenario',100,Adaga(),'Este mercenário esta disposto a tudo para pilhar aqueles no seu caminho com sua adaga')

  def receive_attack(self,damage:int)->bool:
    self.life-=damage
    if self.life<=0:
      return True
    else:
      return False


class Esqueleto(Enemy):
  def __init__(self) -> None:
    super().__init__("Esqueleto",150,Espada_de_mao(),"Um esqueleto  sedento por carne de humanos que quando você menos espera, ataca você com sua espada de mão")  

  def receive_attack(self,damage:int)->bool:
    self.life-=damage
    if self.life<=0:
      return True
    else:
      return False


class Ogro(Enemy):
  def __init__(self) -> None:
    super().__init__("Ogro",250,Espadao(),"Um ser que usa de força bruta que utiliza um grande espadão")

  def receive_attack(self,damage:int)->bool:
    self.life-=damage
    if self.life<=0:
      return True
    else:
      return False


class Elfo(Enemy):
  def __init__(self) -> None:
    super().__init__("Elfo",00, Arco_recurvo,"Um elfo arqueiro que usa apenas de sua habilidade para matar aqueles a sua volta utilizando um arco recurvo")

  def receive_attack(self,damage:int)->bool:
    self.life-=damage
    if self.life<=0:
      return True
    else:
      return False


class Elfo_Negro(Enemy):
  def __init__(self,) -> None:
    super().__init__("Elfo Negro", 250, Arco_longo, "Um elfo negro arqueiro que mata todos aqueles em seu caminho utilizando um arco longo")

  def receive_attack(self,damage:int)->bool:
    self.life-=damage
    if self.life<=0:
      return True
    else:
      return False
    

class Mazzutti(Enemy):
  def __init__(self)->None:
    super().__init__('Mazzutti',150,Mosquete(),'um carecão lindo pelado com o mosquetão de fora vindo te pegar')

    def receive_attack(self,damage:int)->bool:
      self.life-=damage
      if self.life<=0:
        return True
      else:
        return False