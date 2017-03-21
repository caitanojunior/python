num = int(input('Digite um número inteiro: '))

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
    print('Esta sequência tem um número adjacente igual no dígito', num%10)
else:
    print('Esta sequência não tem um número adjacente igual.')


