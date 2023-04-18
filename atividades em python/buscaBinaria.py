import random
import multiprocessing as mp
import time as t


def ordenar(lista:list)->list:
    y = 0
    while y != len(lista):
        x = 0
        while x != len(lista)-1:
            if lista[x] > lista[x+1]:
                temp = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = temp
            x += 1
        y += 1
    return lista


def busca(q:mp.Queue, lista:list[int]or tuple[int], valor:int):
    val = []
    if type(lista) == tuple:
        val = [*lista,]
    else:
        val = lista
    val = ordenar(list(set(val)))
    inicio = 0
    fim = len(val)-1

    while not (inicio == fim-1 or fim==inicio-1):
        local = (inicio + fim)//2
        if val[local] == valor:
            q.put((True, local))
            return
        elif val[local]<valor:
            inicio = local
        else:
            fim = local
    if val[inicio] == valor:
        q.put((True, inicio))
        return
    elif val[fim] == valor:
        q.put((True, fim))
        return
    q.put((False, ))
    return

def criarArr(q:mp.Queue, comprimento:int, valorMin:int, valorMax:int):
    arr = []
    for i in range(comprimento):
        arr.append(random.choice(range(valorMin, valorMax)))
    q.put(arr)


q1:mp.Queue = mp.Queue(25)

processArr:list[mp.Process] = []

for i in range(8):
    processArr.append(mp.Process(target=criarArr, args=(q1, 2500, 100, 3000)))
    processArr[i].start()

for i in processArr:
    i.join()

lista:list[int] = []

processArr = []

q2:mp.Queue = mp.Queue(25)

x = 0
while q1.qsize()!=0:
    processArr.append(mp.Process(target=busca, args=(q2, q1.get(), int(input('qual valor deseja(entre 100 a 3000)')))))
    processArr[x].start()
    x += 1


for i in processArr:
    i.join()
    print(q2.get())


print(t.process_time())