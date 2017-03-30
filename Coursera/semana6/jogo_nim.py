import random

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        usuario_escolhe_jogada(n, m)
    else:
        computador_escolhe_jogada(n, m)

def computador_escolhe_jogada(n, m):
    if(m > 1):
        jogada = random.randint(1, m -1)
    else:
        jogada = 1

    peçasRestante = n - jogada

    if peçasRestante % (m + 1) == 0:
        n = n - jogada
        print("O computador tirou", jogada, "peça.")
        print("Agora restam", n, "peças no tabuleiro.")
        if (m <= n):
            usuario_escolhe_jogada(n, m)
        else:
            print("Fim do jogo! O computador ganhou!")
    else:
        jogada = m
        n = n - jogada
        print("O computador tirou", jogada, "peça.")
        print("Agora restam", n, "peças no tabuleiro.")
        if(m <= n):
            usuario_escolhe_jogada(n, m)
        else:
            print("Fim do jogo! O computador ganhou!")

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    n = n - jogada
    print("Você tirou", jogada, "peça.")
    print("Agora restam", n, "peças no tabuleiro.")
    if (m <= n):
        computador_escolhe_jogada(n, m)
    else:
        print("Fim do jogo! Você ganhou!")


partida()