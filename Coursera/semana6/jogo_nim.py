import random

computador = 0
você = 0

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        usuario_escolhe_jogada(n, m)
    else:
        computador_escolhe_jogada(n, m)

def campeonato():
    i = 1
    global computador
    global você
    while i <= 3:
        print("**** Rodada", i, "****")
        partida()
        i = i + 1
        computador = computador + 1
        você = você + 1
    print("**** Final do campeonato! ****")
    print("Placar: Você", você - 1, "X", computador - 1, "Computador")

def computador_escolhe_jogada(n, m):
    if(m > 1):
        jogada = random.randint(1, m -1)
        if(jogada > n):
            jogada = random.randint(1, n)
        else:
            jogada = jogada
    else:
        jogada = 1
    peçasRestante = n - jogada
    if peçasRestante % (m + 1) == 0:
        n = n - jogada
        print("O computador tirou", jogada, "peça.")
        print("Agora restam", n, "peças no tabuleiro.")
        if(n < 0):
            n = 0
            print("Agora restam", n, "peças no tabuleiro.")
        if (n == 0):
            print("Fim do jogo! O computador ganhou!")
            global  computador
            computador = 1
        else:
            usuario_escolhe_jogada(n, m)
    else:
        jogada = m
        n = n - jogada
        print("O computador tirou", jogada, "peça.")
        if (n < 0):
            n = 0
            print("Agora restam", n, "peças no tabuleiro.")
        if (n == 0):
            print("Fim do jogo! O computador ganhou!")
            computador = 1
        else:
            usuario_escolhe_jogada(n, m)


def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    if(jogada > n):
        print("Jogada inválida, escolha um valor maior ou igual a", n)
        usuario_escolhe_jogada(n, m)
    else:
        n = n - jogada
        print("Você tirou", jogada, "peça.")
        print("Agora restam", n, "peças no tabuleiro.")
        if (n == 0):
            global você
            você = 1
            print("Fim do jogo! Você ganhou!")
        else:
            computador_escolhe_jogada(n, m)

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
opção = int(input())

if (opção == 1):
    partida()
elif (opção == 2):
    campeonato()
else:
    print("Opção inválida")