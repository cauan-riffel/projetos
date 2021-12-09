import random

# 4 – Faça um programa que preenche um cubo de 50 x 50 x 50 com valores aleatórios entre 0 e 100 e encontre: 
# (a) a soma dos valores armazenados no cubo  chec
# (b) o número de ocorrências do valor 90  chec
# (c) o maior	valor armazenado no cubo chec
# (d) as posições onde aparecem o maior valor encontrado em (c) – notar que aqui o programa possivelmente imprimirá mais de uma posição 


def preencher():
    cubo = [[],[],[]]
    if len(cubo[0]) != 50:
        cubo[0].append(random.choice(range(101)))
    if len(cubo[1]) != 50:
        cubo[1].append(random.choice(range(101)))
    if len(cubo[2]) != 50:
        cubo[2].append(random.choice(range(101)))
    while len(cubo[0]) != 50 and len(cubo[1]) != 50 and len(cubo[2]) !=0:
        if len(cubo[0]) != 50:
            cubo[0].append(random.choice(range(101)))
        if len(cubo[1]) != 50:
            cubo[1].append(random.choice(range(101)))
        if len(cubo[2]) != 50:
            cubo[2].append(random.choice(range(101)))
    return cubo
cubo = preencher()
maior = 0
posisao = []
vr = 0
soma = 0
noventa = 0
for _ in cubo:
    for i in _:
        soma += i
        if i == 90:
            noventa += 1
        if i > maior:
            maior = i
z = 0
for _ in cubo:
    x = 0
    for i in _:
        if i == maior:
            posisao.append(z)
            posisao.append(x)
        x += 1
    z += 1
print('a soma dos vaalores no cubo é de:', soma)
print('as ocorrências do numero 90 é de:', noventa)
print('o maior valor do cubo é de:', maior)
print('as posisões do maior número são: ', end=' ')
x = 0
for i in posisao:
    if (x%2) == 0:
        vr = i
    else:
        print(cubo[vr][i])
    x += 1