def partida():
    n = int(input("Digite o número de peças do jogo: "))
    m = int(input("Digite o número máximo de peças a retirar: "))
    if n % (m + 1) == 0:
        usuario_escolhe_jogada(n, m)
    else:
        computador_escolhe_jogada(n, m)

def computador_escolhe_jogada(n, m):
    jogada = 1
    n = n - (m + 1)
    while jogada < m and retante % (m + 1) == 0:
        return jogada
        jogada = jogada + 1
        print(jogada)

def usuario_escolhe_jogada(n, m):


partida()