#Elabore um programa em Python que calcule o resultado de nx, onde n e x são números inteiros positivos lidos. Por exemplo, se n = 2 e x = 3, o valor 2 3 = 8.	
# Para o cálculo, use apenas os comandos iterativos do Python e as operações aritméticas de soma, subtração, multiplicação e divisão (não use as funções prédefinidas de Pyhton). Lembre:se, quando	x =	0, o resultado é 1, independente do valor de n.


vr1 = 1
n = int(input('digite um valor para n '))
vr2 = n
x = int(input('digite um valor para x '))
if x != 0:
    while x > vr1:
        vr2 *= n
        vr1 += 1
    print(vr2)
else:
    print(1)