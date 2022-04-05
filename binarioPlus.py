def descriptografar(numero):
    comprimento = len(numero) - 1
    resultado = 0
    for i in range(comprimento + 1):
        resultado += int(numero[i]) * 2 ** comprimento
        comprimento -= 1

    print(resultado)

def criptografar(numero):
    resto = int(numero)
    total = ''
    while not(resto == 1 or resto == 2):
        total += str(resto % 2)
        resto = resto // 2
    if resto == 1:
        total += '1'
    else:
        total += '01'
    return reversed(total)


numero = input('digite um numero em binario ')
x = criptografar(numero)
for i in x:
    print(i, end='')
print()
