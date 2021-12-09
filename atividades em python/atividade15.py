#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

'''- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
- Salário Líquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

GH = float(input('quanto você recebe por hora?'))
HM = float(input('quantas horas você trabalha por mês?'))
SB = GH * HM
IR = (SB / 100) * 11
INSS = (SB / 100) * 8
sindicato = (SB / 100) * 5
SL = SB - IR - INSS - sindicato
print('seu salário bruto é de',SB,'reais')
print('você pagou',IR,'reais do imposto de renda(11%)')
print('você pagou',INSS,'reais para o INSS(8%)')
print('você pagou',sindicato,'reais para o sindicato(5%)')
print('seu salário liquido é de',SL,'reais')

