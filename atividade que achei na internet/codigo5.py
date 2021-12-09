#Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.


print('::::::::::::::::::::::::::::::::')
print('::::::: função matemática ::::::')
print('::::::::::::::::::::::::::::::::')

num = int(input('digite a tabuada que quer ver: '))
while not 1 <= num <= 10:
    num = int(input('digite a tabuada que quer ver: '))
x = 1
while x <= 10:
    calculo = f'{num} * {x}'
    print(calculo, '=', eval(calculo))
    x += 1