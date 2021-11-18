def descobrir(p):
    p1x = ''
    p1y = ''
    p2x = ''
    p2y = ''
    v = 0
    x1 = 0
    x2 = 0
    for i in p:
        if i != ' ' and v == 0:

            if i == ',':
                x1 += 1
            elif x1 == 0:
                p1x += i
            else:
                p1y += i
        elif i == ' ':
            v += 1
        else:

            if i == ',':
                x2 += 1
            elif x2 == 0:
                p2x += i
            else:
                p2y += i
    p1x = int(p1x)
    p2x = int(p2x)
    p1y = int(p1y)
    p2y = int(p2y)
    a = int((p2y-p1y)/(p2x-p1x))
    b = int(a*p2x-p2y)
    if b > 0:
        print(f'a função afim é: f(x)={a}x+{b}')
    elif b < 0:
        print(f'a função afim é: f(x)={a}x{b}')
    else:
        print(f'a função afim é: f(x)={a}x')
    return f'{a}x+{b}'


def função(funçao):
    a = ''
    b = ''
    x = 0
    while x < len(funçao):
        if funçao[x] == 'x':
            a = int(funçao[:x])
            b = int(funçao[x+2:])
        x += 1
    print(f'o coeficiente angular é: {a}')
    print(f'o coeficiente linear é: {b}')
    x = 0
    raiz = a*x+b
    print(f'a raiz da função é: {raiz}')
    z = input(
        'digite o valor de X para descobrir sua imagem: (obs. o comando irá morrer caso você digite não) ')
    while z != 'não':
        z = int(z)
        ponto = a*z+b
        print(f'a imagem de {z} é : {ponto}')
        z = input(
            'digite o valor de X para descobrir sua imagem: (obs. o comando irá morrer caso você digite não) ')


f = input('digite a função afim, ex:12x+3 ou  dois pontos ex: 12,4 13,2 ')
x = 0
for i in f:
    if i in 'x+':
        x += 1
if x == 0:
    função(descobrir(f))
else:
    função(f)
