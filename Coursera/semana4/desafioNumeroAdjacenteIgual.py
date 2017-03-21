num = int(input('Digite um número inteiro com no mínimo 3 dígitos: '))

naoTemNumeroAdjacenteIgual = True

while(naoTemNumeroAdjacenteIgual and num > 0):
    ultimoNumero = num % 10
    num = num // 10
    proximo = num % 10
    if ultimoNumero == proximo:
        naoTemNumeroAdjacenteIgual = False
        break
    else:
        naoTemNumeroAdjacenteIgual = True

if naoTemNumeroAdjacenteIgual == False:
    print('Esta sequência tem um número igual')
    print(num)
else:
    print('Esta sequência não tem um número igual')


