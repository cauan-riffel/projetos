#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#- comprar apenas latas de 18 litros;
#- comprar apenas galões de 3,6 litros;
#- Misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb=float(input('digite o tamanho do arquivo em Mb'))
mbs=float(input('digite o mbps da sua internet'))
b=mb*8
tes=float(b/mbs)
tem=float(b/mbs/60)
teh=float(b/mbs/60/60)
print('o tempo esperado é',tes,'segundos')
print('o tempo esperado em minutos são',tem)
print('o tempo esperado em horas são',teh)