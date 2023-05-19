import random


weapon_names=('adaga','espada de mão','espadão','arco curvo','arco longo','mosquete')

class Weapon:
  def __init__(self,name:str,damage:float,accuracy:int)->None:
    self.name=name
    self.damage=damage
    self.accuracy=accuracy

  def show_description(self)->None:
    return '%s:{dano:%.2f, precisão:%.1f}'%(self.name, self.damage, self.accuracy/10)


class Adaga(Weapon):
  def __init__(self, name: str, damage: float, accuracy: int) -> None:
    super().__init__('adaga',45,910)

  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0

    
    
class Mosquete(Weapon):
  def __init__(self, name: str, damage: float, accuracy: int) -> None:
    super().__init__('mosquete',400,230)

  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0

def create_weapon(name:str)->Weapon:
  if name=='adaga':
    return Weapon(name,45,910)
  elif name=='espada de mão':
    return Weapon(name,135,700)
  elif name=='espadão':
    return Weapon(name,210,410)
  elif name=='arco curvo':
    return Weapon(name,250,300)
  elif name=='arco longo':
    return Weapon(name,150,430)
  else:
    return Weapon(name,400,230)
