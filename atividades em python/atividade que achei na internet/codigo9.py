#  Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.


num = int(input('digite um número: '))
while num != 0:
    if num == 1:
        print('o número é neutro na multiplicação')
    elif (num % 2) == 1:
        print('o número é impar')
    elif (num % 2) == 0:
        print('o número é par')
    print('digite 0 para matar o programa')
    num = int(input('digite um número: '))