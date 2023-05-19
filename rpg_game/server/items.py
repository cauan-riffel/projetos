import random


weapon_names=('adaga','espada de mão','espadão','arco curvo','arco longo','mosquete')


class Weapon:
  def __init__(self,name:str,damage:float,accuracy:int)->None:
    self.name=name
    self.damage=damage
    self.accuracy=accuracy

  def show_description(self)->None:
    return '%s:{dano:%.2i, precisão:%.1f}'%(self.name,self.damage,self.accuracy/10)


class Adaga(Weapon):
  def __init__(self)->None:
    super().__init__('adaga',45,910)

  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0


class Espada_de_mao(Weapon):
  def __init__(self)->None:
    super().__init__("espada de mão", 135, 700)

  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0


class Espadao(Weapon):
  def __init__(self)->None:
    super().__init__("Espadão", 210, 410)
  
  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0


class Arco_recurvo(Weapon):
  def __init__(self)->None:
    super().__init__("Arco Curvo", 250, 300)
    
  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0


class Arco_longo(Weapon):
  def __init__(self)->None:
    super().__init__("Arco Longo", 280, 430)

  def attack(self) -> float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0


class Mosquete(Weapon):
  def __init__(self)->None:
    super().__init__('mosquete',400,230)

  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0
