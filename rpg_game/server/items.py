import random


weapon_names=('adaga','espada de mão','espadão','arco curvo','arco longo','mosquete')

class Weapon:
  def __init__(self,name:str,damage:float,accuracy:int)->None:
    self.name=name
    self.damage=damage
    self.accuracy=accuracy

  def attack(self)->float:
    if random.randint(0,1000)<=self.accuracy:
      if self.name=='mosquete':
        print('bang')
      return self.damage
    else:
      return 0

  def show_description(self)->None:
    return '%s:{dano:%.2f, precisão:%.1f}'%(self.name, self.damage, self.accuracy/10)

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
