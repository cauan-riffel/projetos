#Escreva um programa que mostre todos os números entre 5 e 100 que são divisíveis por 7, mas não são múltiplos de 5. Os números obtidos devem ser impressos em sequência.


num = 7
vr = 1
while(vr * num) <= 100:
    if ((vr * num) % 5) != 0:
        print(vr * num)
    vr += 1