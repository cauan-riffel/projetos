import random
import time


def main():
    z = ['carregando funções', 'carregando área visual', 'carregando variáveis',
         'preparando comandos principais', 'calculando quando você irá perder....']
    print('\n'*32)
    print('Loading…')
    print('█▒▒▒▒▒▒▒▒▒')
    x = random.choice(range(len(z)))
    print(z[x])
    del(z[x])
    time.sleep(1.5)
    print('\n'*32)
    print('10%')
    print('███▒▒▒▒▒▒▒')
    x = random.choice(range(len(z)))
    print(z[x])
    del(z[x])
    time.sleep(1.5)
    print('\n'*32)
    print('30%')
    print('█████▒▒▒▒▒')
    x = random.choice(range(len(z)))
    print(z[x])
    del(z[x])
    time.sleep(1.5)
    print('\n'*32)
    print('50%')
    print('███████▒▒▒')
    x = random.choice(range(len(z)))
    print(z[x])
    del(z[x])
    time.sleep(1.5)
    print('\n'*32)
    print('99%')
    print('██████████')
    x = random.choice(range(len(z)))
    print(z[x])
    time.sleep(1)
    print('concluído')
    time.sleep(1.5)
    print('\n'*32)
    print()
    print("=================================================")
    print("             Bem-vindo ao Gemas!                 ")
    print("=================================================")
    print()

    pontos = 0
    # parâmetros do jogo
    num_linhas = int(input("Digite o número de linhas [3-10]: "))  # exemplo: 8
    num_colunas = int(
        input("Digite o número de colunas [3-10]: "))  # exemplo: 8
    num_cores = int(input("Digite o número de cores [3-26]: "))  # exemplo: 7
    # cria tabuleiro com configuração inicial
    tabuleiro = criar(num_linhas, num_colunas)
    completar(tabuleiro, num_cores)
    num_gemas = eliminar(tabuleiro)
    while num_gemas > 0:
        deslocar(tabuleiro)
        completar(tabuleiro, num_cores)
        num_gemas = eliminar(tabuleiro)
    # laço principal do jogo
    # Enquanto houver movimentos válidos...
    while existem_movimentos_validos(tabuleiro):
        exibir(tabuleiro)
        comando = input("Digite um comando (perm, dica, sair ou ajuda): ")
        if comando == "perm":
            linha1 = int(input("Digite a linha da primeira gema: "))-1
            coluna1 = int(input("Digite a coluna da primeira gema: "))-1
            linha2 = int(input("Digite a linha da segunda gema: "))-1
            coluna2 = int(input("Digite a coluna da segunda gema: "))-1
            print()
            valido = trocar(linha1, coluna1, linha2, coluna2, tabuleiro)
            if valido:
                num_gemas = eliminar(tabuleiro)
                total_gemas = 0
                while num_gemas > 0:
                    # Ao destruir gemas, as gemas superiores são deslocadas para "baixo",
                    # criando a possibilidade de que novas cadeias surjam.
                    # Devemos então deslocar gemas e destruir cadeias enquanto houverem.
                    deslocar(tabuleiro)
                    completar(tabuleiro, num_cores)
                    total_gemas += num_gemas
                    print("Nesta rodada: %d gemas destruídas!" % num_gemas)
                    exibir(tabuleiro)
                    num_gemas = eliminar(tabuleiro)
                pontos += total_gemas
                print()
                print("*** Você destruiu %d gemas! ***" % (total_gemas))
                print()
            else:
                print()
                print("*** Movimento inválido! ***")
                print()
        elif comando == "dica":
            pontos -= 1
            linha, coluna = obter_dica(tabuleiro)
            print()
            print("*** Dica: Tente permutar a gema na linha %d e coluna %d ***" %
                  (linha, coluna))
            print()
        elif comando == "sair":
            print("Fim de jogo!")
            print("Você destruiu um total de %d gemas" % (pontos))
            return
        elif comando == "ajuda":
            print("""
============= Ajuda =====================
perm:  permuta gemas
dica:  solicita uma dica (perde 1 ponto)
sair:  termina o jogo
=========================================
                  """)
        else:
            print()
            print(
                "*** Comando inválido! Tente ajuda para receber uma lista de comandos válidos. ***")
            print()
    print("*** Fim de Jogo: Não existem mais movimentos válidos! ***")
    print("Você destruiu um total de %d gemas" % (pontos))


# ======================================================================
#
#   FUNÇÕES A SEREM IMPLEMENTADAS POR VOCÊ
#
# ======================================================================


def criar(lin, col):
    x = 0
    # criação de tabela
    while x == 0:
        if lin == 3 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 3 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 3 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 3 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 3 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 3 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 3 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 3 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 4 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 5 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 6 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 7 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 8 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 9 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 3:
            tab = [[' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' '],
                   [' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 4:
            tab = [[' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 5:
            tab = [[' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 6:
            tab = [[' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 7:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 8:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 9:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        elif lin == 10 and col == 10:
            tab = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
            x += 1
        else:
            if not 3 >= lin <= 10:
                lin = int(input('Digite o número de linhas [3-10]: '))
            if not 3 >= col <= 10:
                lin = int(input('Digite o número de colunas [3-10]: '))
    return tab


def exibir(tabs):
    # mostra ao usuário a tabela
    x = 1
    print('     ', end='')
    while x <= len(tabs[0]):
        print(x, end=' ')
        x += 1
    print('')
    print('  ', '+', '-'*(len(tabs[0])*2-1), '+')
    x = 1
    z = 0
    while x <= len(tabs):
        if x == 10:
            print(x, '|', end=' ')
        else:
            print(f'{x} ', '|', end=' ')
        for i in tabs[z]:
            print(i, end=' ')
        z += 1
        print('|')
        x += 1
    print('  ', '+', '-'*(len(tabs[0])*2-1), '+')


def completar(tabs, ng):
    # completa a primeira linha com peças aleatórias
    peças = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'w', 'X', 'Y', 'Z']
    for _ in range(len(tabs)):
        x = 0
        for i in tabs[0]:
            z = random.choice(peças[:ng])
            if i == ' ':
                tabs[0][x] = z
            x += 1
        deslocar(tabs)


def deslocar(tabs):
    # desce todas as linhas da tabela
    y = 1
    for i in tabs[1:]:
        x = 0
        for e in i:
            if e == ' ':
                tabs[y][x] = tabs[y-1][x]
                tabs[y-1][x] = ' '
            x += 1
        y += 1


def descerlin(tabs, lin):
    for i in range(len(tabs)):
        lin -= 1
        y = 0
        while y < len(tabs):
            if tabs[y][lin] == ' ':
                tabs[y][lin] = tabs[y-1][lin]
                tabs[y-1][lin] = ' '
            y += 1


def lin(tabs):
    z = []

    for e in range(len(tabs)):
        for i in range(len(tabs[0])-2):
            if tabs[e][i] == tabs[e][i + 1] == tabs[e][i + 2]:
                j = i + 2
                while (j + 1) < len(tabs[0]) and tabs[e][j + 1] == tabs[e][j]:
                    j += 1
                z.append([e, i, j])
    return z


def col(tabs):
    z = []
    for e in range(len(tabs[0])):
        for i in range(len(tabs)-2):
            if tabs[i][e] == tabs[i+1][e] == tabs[i+2][e]:
                j = i + 2
                while (j + 1) < len(tabs) and tabs[j + 1][e] == tabs[j][e]:
                    j += 1
                z.append([e, i, j])
    return z


def eliminar(tabs):
    points = 0
    l = lin(tabs)
    c = col(tabs)
    if len(l) > 0:
        for i in l:
            x = i[0]
            y = i[1]
            y1 = i[2]
            while y <= y1:
                if tabs[x][y] != ' ':
                    tabs[x][y] = ' '
                    points += 1
                y += 1
    if len(c) > 0:
        for i in c:
            y = i[0]
            x = i[1]
            x1 = i[2]
            while x <= x1:
                if tabs[x][y] != ' ':
                    tabs[x][y] = ' '
                    points += 1
                x += 1

    return points


def trocar(p1, p2, p3, p4, tabs):
    # move as peças informadas
    param = [p1-1, p2]
    param2 = [p3, p4]
    if param == param2:
        z = tabs[p1][p2]
        tabs[p1][p2] = tabs[p3][p4]
        tabs[p3][p4] = z
        return True
    param = [p1, p2]
    param2 = [p3-1, p4]
    if param == param2:
        z = tabs[p1][p2]
        tabs[p1][p2] = tabs[p3][p4]
        tabs[p3][p4] = z
        return True
    param = [p1, p2-1]
    param2 = [p3, p4]
    if param == param2:
        z = tabs[p1][p2]
        tabs[p1][p2] = tabs[p3][p4]
        tabs[p3][p4] = z
        return True
    param = [p1, p2]
    param2 = [p3, p4-1]
    if param == param2:
        z = tabs[p1][p2]
        tabs[p1][p2] = tabs[p3][p4]
        tabs[p3][p4] = z
        return True
    return False


def obter_dica(tabs):
    # verifica linha por linha, coluna por coluna se há possiveis movimentos e retorna um movimento aleatório
    tips = []
    # linha
    for i in range(len(tabs)-1):
        for e in range(len(tabs[0])-2):
            if tabs[i][e] == tabs[i][e+1] == tabs[i+1][e+2]:
                tips.append([i+1, e+3])
                tips.append([i+2, e+3])
            if i > 0 and tabs[i][e] == tabs[i][e+1] == tabs[i-1][e+2]:
                tips.append([i+1, e+3])
                tips.append([i, e+3])
            if tabs[i][e] == tabs[i+1][e+1] == tabs[i][e+2]:
                tips.append([i+1, e+2])
                tips.append([i+2, e+2])
            if i > 0 and tabs[i][e] == tabs[i-1][e+1] == tabs[i][e+2]:
                tips.append([i, e+2])
                tips.append([i+1, e+2])
            if tabs[i+1][e] == tabs[i][e+1] == tabs[i][e+2]:
                tips.append([i+1, e+1])
                tips.append([i+2, e+1])
            if i > 0 and tabs[i-1][e] == tabs[i][e+1] == tabs[i][e+2]:
                tips.append([i+1, e+1])
                tips.append([i, e+1])
            if e <= len(tabs[0])-4 and tabs[i][e] == tabs[i][e+2] == tabs[i][e+3]:
                tips.append([i+1, e+1])
                tips.append([i+1, e+2])
            if e <= len(tabs[0])-4 and tabs[i][e] == tabs[i][e+1] == tabs[i][e+3]:
                tips.append([i+1, e+3])
                tips.append([i+1, e+4])

    # coluna
    for e in range(len(tabs[0])-1):
        for i in range(len(tabs)-2):
            if tabs[i][e] == tabs[i+1][e] == tabs[i+2][e+1]:
                tips.append([i+3, e+1])
                tips.append([i+3, e+2])
            if tabs[i][e] == tabs[i+1][e] == tabs[i+2][e-1]:
                tips.append([i+3, e+1])
                tips.append([i+3, e])
            if tabs[i][e] == tabs[i+1][e+1] == tabs[i+2][e]:
                tips.append([i+2, e+1])
                tips.append([i+2, e+2])
            if tabs[i][e] == tabs[i+1][e-1] == tabs[i+2][e]:
                tips.append([i+2, e+1])
                tips.append([i+2, e])
            if tabs[i][e+1] == tabs[i+1][e] == tabs[i+2][e]:
                tips.append([i+1, e+1])
                tips.append([i+1, e+2])
            if tabs[i][e-1] == tabs[i+1][e] == tabs[i+2][e]:
                tips.append([i+1, e+1])
                tips.append([i+1, e])
            if i >= 2 and tabs[i-2][e] == tabs[i][e] == tabs[i+1][e]:
                tips.append([i+1, e-1])
                tips.append([i, e+1])
            if i > 0 and tabs[i-1][e] == tabs[i][e] == tabs[i+2][e]:
                tips.append([i+3, e+1])
                tips.append([i+4, e+1])
    return random.choice(tips)


def existem_movimentos_validos(tabs):
    tips = []
    # linha
    for i in range(len(tabs)-1):
        for e in range(len(tabs[0])-2):
            if tabs[i][e] == tabs[i][e+1] == tabs[i+1][e+2]:
                tips.append([i+1, e+2])
                tips.append([i+2, e+3])
            if i > 0 and tabs[i][e] == tabs[i][e+1] == tabs[i-1][e+2]:
                tips.append([i+1, e+2])
                tips.append([i, e+2])
            if tabs[i][e] == tabs[i+1][e+1] == tabs[i][e+2]:
                tips.append([i+1, e+1])
                tips.append([i+2, e+1])
            if i > 0 and tabs[i][e] == tabs[i-1][e+1] == tabs[i][e+2]:
                tips.append([i, e+1])
                tips.append([i-1, e+1])
            if tabs[i+1][e] == tabs[i][e+1] == tabs[i][e+2]:
                tips.append([i, e])
                tips.append([i+1, e])
            if i > 0 and tabs[i-1][e] == tabs[i][e+1] == tabs[i][e+2]:
                tips.append([i, e])
                tips.append([i-1, e])
            if e >= 2 and tabs[i][e-2] == tabs[i][e] == tabs[i][e+1]:
                tips.append([i+1, e-1])
                tips.append([i+1, e])
            if e > 0 and tabs[i][e-1] == tabs[i][e] == tabs[i][e+2]:
                tips.append([i+1, e+3])
                tips.append([i+1, e+4])

    # coluna
    for e in range(len(tabs[0])-1):
        for i in range(len(tabs)-2):
            if tabs[i][e] == tabs[i+1][e] == tabs[i+2][e+1]:
                tips.append([i+3, e+1])
                tips.append([i+3, e+2])
            if tabs[i][e] == tabs[i+1][e] == tabs[i+2][e-1]:
                tips.append([i+3, e+1])
                tips.append([i+3, e])
            if tabs[i][e] == tabs[i+1][e+1] == tabs[i+2][e]:
                tips.append([i+2, e+1])
                tips.append([i+2, e+2])
            if tabs[i][e] == tabs[i+1][e-1] == tabs[i+2][e]:
                tips.append([i+2, e+1])
                tips.append([i+2, e])
            if tabs[i][e+1] == tabs[i+1][e] == tabs[i+2][e]:
                tips.append([i+1, e+1])
                tips.append([i+1, e+2])
            if tabs[i][e-1] == tabs[i+1][e] == tabs[i+2][e]:
                tips.append([i+1, e+1])
                tips.append([i+1, e])
            if i >= 2 and tabs[i-2][e] == tabs[i][e] == tabs[i+1][e]:
                tips.append([i+1, e-1])
                tips.append([i, e+1])
            if i > 0 and tabs[i-1][e] == tabs[i][e] == tabs[i+2][e]:
                tips.append([i+3, e+1])
                tips.append([i+4, e+1])
    if tips == []:
        return False
    return True


main()
