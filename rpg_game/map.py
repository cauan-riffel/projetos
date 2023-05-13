import random
# from entities import enemy,enemys_names
#from items import weapons,weapon_names

class Game_map:
  """
    map:
        6
      5  5
      4  4 4
      3  3 3
      2   2
      1   1
        0
    """
  def __init__(self,name:str,description:str,chances:list[int]=[25,100],step=0) -> None:
    self.step=step
    self.name=name
    self.desc=description
    self.evet=self.do_event(chances)
    if self.evet==1:
      # self.gif=weapons(random.choice(weapon_names))
      pass
    elif self.evet==2:
      # self.enemy=enemy(random.choice(enemys_names))
      pass



  def show_local(self):
    last_word=self.name.split(' ')[0][-1]
    end='o'if last_word=='o'else'a'
    print('você adentrou n%s %s'%(end, self.name))
    print(self.desc)

  def do_event(self,chances)->int:
    temp=random.randint(0,100)
    if temp<=chances[0]:
      return 1
    elif temp<=chances[0]+chances[1]:
      return 2
    else:
      return 0
