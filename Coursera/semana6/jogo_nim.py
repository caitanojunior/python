def computador_escolhe_jogada(n, m):
    peçasRestantes = n % (m + 1)
    if peçasRestantes > 0 and peçasRestantes <= m:
        jogada = peçasRestantes
    else:
        jogada = m
    if jogada == 1:
        print()
        print("O computador tirou uma peça")
    else:
        print()
        print("O computador tirou", jogada, "peças")
    return jogada


def usuario_escolhe_jogada(n, m):
    print()
    jogada = int(input("Quantas peças você vai tirar? "))
    print()
    jogadaInvalida = True
    while jogadaInvalida:
        if jogada > m or jogada <= 0 or jogada > n:
            print("Opps! Jogada inválida! tente de novo.")
            jogada = int(input("Quantas peças você vai tirar? "))
        else:
            jogadaInvalida = False
    if jogada == 1:
        print("Você tirou uma peça")
    else:
        print("Você tirou", jogada, "peças")
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    valor_invalido = True

    if (n > 0 and m > 0):
        valor_invalido = False
        if n % (m + 1) == 0:
            print()
            print("Você começa!")
            print()
        else:
            print()
            print("Computador começa!")
            print()
        while(n > 0):
            valor_invalido = False
            if n % (m + 1) == 0:
                n = n - usuario_escolhe_jogada(n, m)
                if( n == 1):
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora resta", n, "peças no tabuleiro.")
                usuario = True
            else:
                n = n - computador_escolhe_jogada(n, m)
                if (n == 1):
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora resta", n, "peças no tabuleiro.")
                usuario = False
        if usuario == True:
            print("Fim de jogo! Você ganhou!")
        else:
            print("Fim de jogo! O computador ganhou!")
    else:
        print("Valores inválidos")
        partida()

def campeonato():
    i = 1
    meusPontos = 0
    pontosComputador = 0

    while i <= 3:
        print("**** Rodada", i, "****")
        print()
        partida()
        i = i + 1
    meusPontos += 1
    pontosComputador += 1

    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você 0 X 3 Computador")

def main():
    try:
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
    except ValueError:
      print("Oops! Opção inválida")
      main()

main()