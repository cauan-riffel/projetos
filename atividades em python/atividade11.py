#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1=int(input('digite um numero inteiro'))
n2=int(input('digite outro numero inteiro'))
n3=float(input('digite um numero real'))
a=(n1*2)*(n2/2)
b=n1*3+(n3)
c=(n3)**3
print('o produto do dobro do primeiro com metade do segundo é',a)
print('a soma do triplo do primeiro com o terceiro é',b)
print('o terceiro elevado ao cubo é',c)