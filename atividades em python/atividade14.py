# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso=int(input('peso dos peixes pescados em kg'))
if peso<=50:
    print('você pescou',peso,'quilos de peixe')
else:
    exesso=peso-50
    multa=exesso*4
    print('você pescou',peso,'quilos de peixe, por ter pescado',exesso,'quilos acima do permitido de peixe você terá que pagar uma multa de',multa,'reais.')
