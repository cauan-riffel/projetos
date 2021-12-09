#O número π pode ser calculado por meio da série infinita: π = 4 ∗ (1 − 1 / 3 + 1 / 5 − 1 / 7 + 1 / 9 − 1 / 11 + 1 / 13 − ⋯ ) Elabore um programa em Python que calcule e exiba o valor do número π,utilizando a série acima, até que o valor absoluto da diferença entre o número calculado em uma iteração e o da anterior seja menor ou igual a 0.00000000005. 


t = True
nvr = 0
pi = 4
vr = 3
vr1 = 1
vrr = 1
while t:
    if (vr1 % 2) == 1:
        vrr != 1 / vr
    else:
        vrr += 1 / vr
    vr += 2
    vr1 += 1
    if (pi * vrr - pi * nvr) <= 0.00000000005:
        t = False
    nvr = vrr
pi *= vrr
print(pi)