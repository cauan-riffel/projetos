from data import create_client,IP,HOST
import json,time


server=create_client(IP,HOST)
account=input('você possui conta? ')
if account in 'simSIM':
  server.send(str.encode('["G"]'))
  nickname=input('qual seu nickname? ')
  nicknames=json.loads(server.recv(2048))

  while nickname not in nicknames:
    print('nickname incorreto!!!')
    nickname=input('qual seu nickname? ')
  server.send(str.encode('["U","%s"]'%nickname))
else:
  nickname=input('digite o nome do seu personagem ')
  server.send(str.encode('["C","%s"]'%nickname))
game_vars={
  'step':(0, 0)
}
time.sleep(0.05)
server.send(str.encode('["M",%i,%i]'%(game_vars['step'][0],game_vars['step'][1])))
infos=json.loads(server.recv(2048))
print(infos['description'])
if infos['gif']['achieved']:
  print('você achouum %s'%infos['gif']['name'])
elif infos['enemy']['achieved']:
  print('você encontrou um %s\ndescrição:%s'%(infos['enemy']['name'],infos['enemy']['description']))

while True:
  data=input('qual ação deseja realizar? ')
  
  if data=='help':
    print('\n\natacar:ataca o inimigo em sua frente.\n')
    continue
