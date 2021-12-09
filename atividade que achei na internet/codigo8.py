#Faça um programa que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado. Por exemplo, se o usuário digitou o número 4, a saída deve ser 10


num = int(input('digite um número '))
vr = 1
soma = 0
while vr <= num:
    soma += vr
    vr += 1
print('a soma é',soma)