#crie um programa para ler um número de 0 até 999 e em seguida mostrar o valor dele por extenso.


t = True
while t:
    dic = {0 : 'zero', 1 : 'um', 2 : 'dois', 3 : 'três', 4 : 'quatro', 5 : 'cinco', 6 : 'seis', 7 : 'sete', 8 : 'oito', 9 : 'nove', 10 : 'dez', 11 : 'onze', 12 : 'doze', 13 : 'treze', 14 : 'catorze', 15 : 'quinze', 16 : 'dezesseis', 17 : 'dezessete', 18 : 'dezoito', 19 : 'dezenove', 20 : 'vinte', 30 : 'trinta', 40 : 'quarenta', 50 : 'cinquenta', 60 : 'sessenta', 70 : 'setenta', 80 : 'oitenta', 90 : 'noventa', 100 : 'cento',101 : 'cem', 200 : 'duzentos', 300 : 'trezentos', 400 : 'quatrocentos', 500 : 'quinhentos', 600 : 'seiscentos', 700 : 'setecentos', 800 : 'oitocentos', 900 : 'novecentos'}
    valor = int(input(f'digite um número: '))
    if valor == 100:
        print(dic[valor + 1])
    if valor > 100:
        print(dic[valor - (valor % 100)], end=' e ')
        valor %= 100
    if 20 <= valor < 100:
        print(dic[valor - (valor % 10)], end=' e ')
        valor %= 10
    if valor < 20:
        print(dic[valor])
    t = input('quer continuar?')
    if t in ('s','S','Sim','sim','SIM'):
        t = True
    else:
        t = False