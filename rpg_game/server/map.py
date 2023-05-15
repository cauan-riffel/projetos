import random
from entities import enemy_names,create_enemy
from items import weapon_names,create_weapon


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
  def __init__(self,name:str,description:str,step=0,path=1,chances:tuple[int]=(75,250))->None:
    self.step=step
    self.path=path
    self.name=name
    self.desc=description
    self.event=self.do_event(chances)
    self.gift=None
    self.enemy=None
    if self.event==1:
      self.gift=create_weapon(random.choice(weapon_names))
    elif self.event==2 or step==5:
      self.enemy=create_enemy(enemy_names[step])
    print('heht')

  def show_local(self)->None:
    last_word=self.name.split(' ')[0][-1]
    end='o'if last_word=='o'else'a'
    return 'você adentrou n%s %s\n%s'%(end,self.name,self.desc)

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
      return Game_map('caverna dos lobos', 'A caverna é um lugar escuro, você ouve goteiras por todo o local e um forte cheiro de carne podre, vinda das vidas que, precocemente foram abatidas enquanto se debatiam em dor.')
    elif step==1:
      return Game_map('Floresta Negra', "Após sair da caverna você se depara no meio de uma floresta de pinheiros enormes. A neblina cerca o lugar, limitando sua visão, nunca se sabe o que pode estar se escondendo nas trevas deste lugar sombrio.",1)
    elif step==2:
      return Game_map("Casa assombrada", "No meio da neblina você encontra uma casa escura cheia de luz, você decide abrir a porta, afinal, ali há menos lugares para os perigos se esconderem, mas também a menos lugar para você se esconder delas.",2)
    elif step==3:
      return Game_map('Vila Destruída', 'Apesar de alguns arranhões e mordidas, você consegue sobreviver a noite na casa e vencer todos os desafios dela. Agora, é hora de desafiar a vila que  a escuridão escondia. Ela está totalmente destruída, como que atacada por uma entidade superior. No chão você vê corpos, um pó de coloração escura que lembrava pólvora e rastros, alguns de sangue, outros de lesma. Você não tem ideia do que aconteceu, apenas sabe de uma coisa: foi brutal.',3)
    elif step==4:
      return Game_map("Forjas Sagradas", "Após vencer a floresta, você vê uma montanha gigante e decide escalá-la, porém busca abrigo em uma construção ao pé dela. Parece ser uma construção usada por ferreiros, conhecidos por sua habilidade e altos preços cobrados de seus clientes. Lá você confirma suas teorias, vendo um bigorna usada na idade média, algo semelhante a uma luneta coberto por uma substância gelatinosa. Ao lado você encontra também uma carta, destinada a Walter. Ela era de um amigo, que contava como os guardas  ouviram vozes em celas vazias da prisão do Rei.", 4)
    else:
      return Game_map("Templo Sagrado", "Em uma vasta planície se encontra um templo, para o qual inúmeras raças veneram. Porém, o que chamou sua atenção à distância não foi o templo em si, mas o ser que estava em sua entrada, possuindo mais de 5 metros de altura, músculos que poderiam facilmente erguer a mais grossa árvore. O que mais chamou a atenção no ser foi a grandiosa habilidade de mudar o percurso da luz, fazendo-a seguir os seus desejos. Mais assustador que seu brilho, era o majestoso mosquete que carregava e sequer fazia esforço algum para escondê-lo da visão de todos, fazendo qualquer um cair de joelhos e orar para a deidade, cujo os atos eram grandiosos sem precedentes que ninguém era capaz de explicar. Realmente, apesar do medo e da imponência que causava, era sem dúvidas uma cena linda de se ver.",5)
  elif path==2:
    if step==1:
      return Game_map('caverna dos bruxos', 'A caverna se torna cada vez mais escura, nela você também sente um pequeno resquício de intenção assassina que cobria todo o local, causando calafrios até mesmo no mais corajoso guerreiro que enfrentava a morte diariamente.',1,2)
    elif step==2:
      return Game_map('rauina do golens', 'As ruínas estão cada vez mais precárias, as estátuas estão incrivelmente desgastadas tornando-se cada vez mais evidente a possibilidade de desprender-se uma rocha da mesma, estes golens eram muito semelhantes um dos outros, possuindo, no lugar da cabeça, rachaduras e em sua cintura algo estranho que nem ao menos você sonhou em possuir em sua vida.',2,2)
    elif step==3:
      return Game_map('caverna dos anjos', 'As cavernas se parecem muito com um refúgio que devia ter sido usado durante a guerra divina, nela você encontrará muitos ossos, que ao menor dos toques irá se esfarelar. Nas paredes rachadas você vê desenhos de pessoas adorando seres enormes, alguns com asas e outros com mosquetes.',3,2)
    elif step==4:
      return Game_map('forja rotacional', 'Ao visualizar uma pequena série de motores, você percebe pequenos raios de luz, mostrando que você está próximos da superfície, porém como não existe almoço grátis, você encontra grandes circunferências presas em algo que parecia ser um barco, estas circunferências soltam grossos rolos que possuíam pequenas fios de vidro.',4,2)
  else:
    return Game_map('caverna de visão curta', 'Esta caverna, relativamente avermelhada, possui em suas paredes escrituras muito antigas, porém, com muito esforço você consegue decifrar alguns caracteres  formando a seguinte mensagem: "todos os aqui presentes devem ab#icar dos bens mortais, e div&%i-los, dei@#ndo de la@o a gan$&!ia e a part!r de hoje de$em se t$%nar bol#*eviq!es usufruidores dos pr!dut@s da abençoada ma#ã"',3,3)

def move_possibilitys(obj:Game_map)->tuple[tuple[int,int]]:
  if obj.path==1 and obj.step!=0:
    return ((obj.step+1,obj.path))
  elif obj.path==1:
    return ((obj.step+1,obj.path),(obj.step+1,obj.path+1))
  elif obj.step==2:
    return ((obj.step+1,obj.path),(obj.step+1,obj.path+1))
  elif obj.path==3 or obj.step==4:
    return ((obj.step+1,obj.path-1))
  else:
    return ((obj.step+1,obj.path))
  

