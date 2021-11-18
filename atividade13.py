# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

D = int(input('digite 1 caso seja homem e 2 caso seja mulher'))
h = float(input('digite sua altura'))
if D == 1:
    pi = (72.7*h)-58
    print('seu peso ideal é', pi)
else:
    pi = float((62.1*h)-44.7)
    print('seu peso ideal é', pi)
