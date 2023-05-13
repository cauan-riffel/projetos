import random
# from entities import enemy,enemys_names
#from items import weapons,weapon_names

class Game_map:
  """
  step:path
    map:
           5:1
      4:1      4:2
      3:1   3:2  3:3
      2:1      2:2
      1:1      1:2
           0:1
    """
  def __init__(self,name:str,description:str,chances:tuple[int]=(25,100),step=0,path=0)->None:
    self.step=step
    self.path=path
    self.name=name
    self.desc=description
    self.event=self.do_event(chances)
    self.gif=None
    self.enemy=None
    if self.event==1:
      self.gif=create_weapon(random.choice(weapon_names))
    elif self.event==2:
      self.enemy=enemy_names(random.choice(enemy_names))

  def show_local(self)->None:
    last_word=self.name.split(' ')[0][-1]
    end='o'if last_word=='o'else'a'
    print('você adentrou n%s %s'%(end, self.name))
    print(self.desc)

  def do_event(self,chances:tuple[int])->int:
    temp=random.randint(0,100)
    if temp<=chances[0]:
      return 1
    elif temp<=chances[0]+chances[1]:
      return 2
    else:
      return 0


def create_map(step:str, path:str)->Game_map:
  if path==1:
    if step==0:
      return Game_map()
  else:
