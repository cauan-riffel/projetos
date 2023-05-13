import random


class Weapon:
  def __init__(self,nome:str,dano:float,precisao:int) -> None:
    self.name=nome
    self.damage=dano
    self.ocuracity=precisao

  def atacar(self)->float:
    if random.randint(0,1000)<=self.ocuracity:
      return self.damage
    else:
      return 0
