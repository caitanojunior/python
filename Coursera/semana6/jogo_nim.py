import random

computador = 0
você = 0

def computador_escolhe_jogada(n, m):
    jogada = 1
    peçasRestante = n - jogada
    if (peçasRestante % (m + 1) != 0):
        jogada = m
        peçasRestante = n - jogada
        if (jogada > n):
            jogada = n
            peçasRestante = n - jogada
        else:
            jogada
            peçasRestante = n - jogada
    else:
        jogada = 1
        peçasRestante = n - jogada
    n = peçasRestante
    if(jogada > 1):
        print("O computador tirou", jogada, "peças.")
    else:
        print("O computador tirou", jogada, "peça.")
    if(n > 1):
        print("Agora restam", n, "peças no tabuleiro.")
        print()
        usuario_escolhe_jogada(n, m)
    elif(n == 1):
        print("Agora resta apenas", n, "peça no tabuleiro.")
        print()
        usuario_escolhe_jogada(n, m)
    else:
        print("Fim do jogo! O computador ganhou!")
        global computador
        computador = 1

def usuario_escolhe_jogada(n, m):
    jogada = int(input("Quantas peças você vai tirar? "))
    if(jogada > m or jogada < 1):
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        usuario_escolhe_jogada(n, m)
    else:
        n = n - jogada
        if(jogada == 1):
            print("Você tirou", jogada, "peça.")
        else:
            print("Você tirou", jogada, "peças.")
        if (n > 1):
            print("Agora restam", n, "peças no tabuleiro.")
            print()
            computador_escolhe_jogada(n, m)
        elif (n == 1):
            print("Agora resta uma peça no tabuleiro.")
            print()
            computador_escolhe_jogada(n, m)
        else:
            print("Fim do jogo! Você ganhou!")
            print()
            global você
            você = 1

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    if(n > 1 and m >= 1):
        if n % (m + 1) == 0:
            usuario_escolhe_jogada(n, m)
        else:
            computador_escolhe_jogada(n, m)
    else:
        print("Valores inválidos")
        partida()

def campeonato():
    i = 1
    global computador
    global você
    pontosComputador = 0
    pontosUsuário = 0
    while i <= 3:
        print("**** Rodada", i, "****")
        print()
        partida()
        i = i + 1
        pontosComputador = pontosComputador + computador
        pontosUsuário = pontosUsuário + você
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", pontosUsuário, "X", pontosComputador, "Computador")

print()
print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
opção = int(input())

while(opção != 1 and opção != 2):
    print("Oops! Opção inválida")
    opção = int(input())

if (opção == 1):
    print("Voce escolheu uma partida isolada!")
    print()
    partida()
else:
    print("Voce escolheu um campeonato!")
    print()
    campeonato()
