import random

você = 0
computador = 0

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
            computador = 1
            print("Fim do jogo! O computador ganhou!")
    else:
        jogada = m
        n = n - jogada
        print("O computador tirou", jogada, "peça.")
        print("Agora restam", n, "peças no tabuleiro.")
        if(m <= n):
            usuario_escolhe_jogada(n, m)
        else:
            computador = 1
            print("Fim do jogo! O computador ganhou!")

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    n = n - jogada
    print("Você tirou", jogada, "peça.")
    print("Agora restam", n, "peças no tabuleiro.")
    if (m <= n):
        computador_escolhe_jogada(n, m)
    else:
        você = 1
        print("Fim do jogo! Você ganhou!")

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
opção = int(input())

if(opção == 1):
    partida()
elif(opção == 2):
    i = 0
    while i < 3:
        partida()
        i = i + 1
        você = você + 1#verificar lógica
        computador = computador + 1#verificar lógica
    print("**** Final do campeonato! ****")
    print("Placar: Você", você, "X", computador, "Computador")
else:
    print("Opção inválida,")

