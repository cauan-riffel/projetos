# Documentação
## protocolo utilizado
O protocolo utilizado foi o protocolo TCP para diminuir a chance de ocorrer erros no envio das mensagens

## arquivos
### **servidor**
#### data.py
Este é o arquivo que contém o IP e HOST do servidor, bem com uma função responsável por criar o servidor.

#### items.py
Este arquivo contém uma classe pai Weapon, responsável pelo ataque do personagem e subclasses que colocam automaticamente o nome, dano e precisão de cada equipamento.
Obs.: o uso de classes filho foi recomendação do Mazzutti

#### map_and_entities.py
Este arquivo é a junção de 2 arquivos diferentes sendo eles map e entities, esta junção foi necessária, pois estava ocorrendo erros de circular import. Esse arquivo contém três classes pai que são Character-que é a classe do personagem controlado pelo cliente-, Enemy-classe que representa cada um dos inimigos- e Game_map que é a classe que possui todas as informações do mapa do jogo. As subclasses de Enemy adicionam o nome, vida, equipamento e descrição de cada inimigo, o mesmo ocorre com as subclasses de Game_map. 
Obs.: o uso de classes filho foi recomendação do Mazzutti

#### server.py
Este arquivo contém toda a comunicação do servidor, ele possui 4 funções principais que são:
* send-que envia os dados para o cliente.
* create_map que cria e retorna um mapa.
* get_map_infos que retorna um dict contendo todas as informações do mapa contendo descrição, inimigo e item.
* cliente que possui todos os métodos que o cliente pede para o servidor.

Após a declaração das funções é criado o servidor e cria-se um loop while que sempre se repetirá, em que o servidor ficará esperando uma conexão para mostrar o HOST e IP do cliente e depois disso criar uma nova thread para este cliente

### **cliente**
####  data.py
Este é o arquivo que contém o IP e HOST do servidor, bem com uma função responsável por criar uma conexão com o servidor.

#### cliente.py
Este arquivo é o que realiza todas as comunicações por parte do cliente, possui 3 funções principais que são:
* get_type que retorna 'a' se a palavra for feminina ou ''.
* send envia os dados para o servidor.
* change_map que irá mostrar ao usuário as informações do mapa.

# tipos de mensagem do servidor
### GN-get nicknames
Retorna para o cliente uma lista com o nome de todos os personagens criados no jogo.
### CC-create character
Cria e usa um personagem com o nome enviado pelo cliente.
### GW-getWeapon
Retorna para o cliente uma lista com todos os equipamentos no inventário do personagem.
### UC-use character
Usa o personagem com o nome passado pelo cliente.
### MI-map infos
Retorna para o cliente um dicionário contendo todas as informações do mapa que ele esta.
### AT-attack
Ataca o inimigo que esta com o personagem e retorna para o cliente uma lista contendo:
* ['ND',character damage, enemy damage](ND significa nobody died).
* ['CD',character damage, enemy damage](CD significa Character died).
* ['ED', chracter damage](ED significa Enemy died).
### MV-move
Envia para o cliente todos os locais que o personagem pode se mover, após isso fica esperando o cliente enviar o nome do local, o traduz para o inglês e cria um novo mapa usando a função create map.
### UW-use Weapon
Faz o personagem utilizar o equipamento especificado pelo cliente.
### GS-get status
Retorna para o cliente os status do personagem.

# Instalação
## server
Para o computador que conterá o servidor ele precisa baixar todos os arquivos contidos na pasta server.
## client
Para os clientes é necessário baixar os arquivos contidos na pasta client
## ateração necessária
Tanto no servidor como no cliente é necessário alterar o host em ambos os arquivos data.py, o host deve ser o IP do servidor na rede
