numero = input('Digite um número inteiro com no mínimo 3 dígitos: ')

naoTemNumeroAdjacenteIgual = True
num = int(numero)
tamanho = len(numero)

while(naoTemNumeroAdjacenteIgual):
    ultimoNumero = num % 10
    num = num // 10
    proximo = num%10
    if(ultimoNumero == proximo):
        print('Esta sequência tem um número igual')
        naoTemNumeroAdjacenteIgual = False
    else:
        print('Esta sequência não tem um número igual')
        break

