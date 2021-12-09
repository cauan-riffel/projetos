# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.C = (5 * (F-32) / 9).

F = float(input('quantos graus Farenheit estão agora?'))
C = 5*(F-32)/9
print('agora estão', C, 'graus Celsius')