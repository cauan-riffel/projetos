#Faça um programa que leia um código de operação (+,:,*	ou /), e também dois valores inteiros A e B. O programa deve calcular o resultado da operação escolhida aplicado a A e B. Por exemplo, se a operação escolhida foi * e A = 1 e B = 3, o programa deve fornecer como esultado o valor de 1*3, que é 3.


operaçao = input('digite a operação que deseja fazer(ex. + ,- ,* ,/ ,** ,% ) ')
a=int(input('digite o valor de A '))
b=int(input('digite o valor de B '))
if operaçao== '+' :
    r = a + b
elif operaçao == '-':
    r = a - b
elif operaçao == '*':
    r = a * b
elif operaçao == '/':
    r = a / b
elif operaçao == '%':
    r = a % b
else:
    r = a ** b
print(r)
