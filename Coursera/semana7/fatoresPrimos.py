def fatorPrimo():
    n = int(input("Digite um número inteiro maior que 1: "))
    fator = 2
    multiplicidade = 0

    while(n > 1):
        while n % fator == 0:
            multiplicidade = multiplicidade + 1
            n = n / fator
        if (multiplicidade > 0):
            print("No fator", fator, "a multiplicidade é", multiplicidade)
        fator = fator + 1
        multiplicidade = 0
    fatores = list(str(fator))
    return fatores

def verificaFatorPrimo(f):
    listaDeFatores = f
    print("Minha lista de fatores:", listaDeFatores)

verificaFatorPrimo(fatorPrimo())
