import random


weapon_names=('adaga','espada de mão','espadão','arco curvo','arco longo','mosquete')

class Weapon:
  def __init__(self,name:str,damage:float,accuracy:int) -> None:
    self.name=accuracy
    self.damage=damage
    self.accuracy=accuracy

  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      return self.damage
    else:
      return 0

def create_weapon(nome:str)->Weapon:
  if nome=='adaga':
    return Weapon(nome,66,910)
  elif nome=='epada de mão':
    return Weapon(nome,66,910)
  elif nome=='espadão':
    return Weapon(nome,66,910)
  elif nome=='arco curvo':
    return Weapon(nome,66,910)
  elif nome=='arco longo':
    return Weapon(nome,66,910)
  else:
    return Weapon(nome,66,910)
