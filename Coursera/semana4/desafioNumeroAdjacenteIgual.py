numero = input('Digite um número inteiro com no mínimo 3 dígitos')

numeroDigitado = '1'
temNumeroAdjacenteIgual = False

while(numeroDigitado != '0' and not temNumeroAdjacenteIgual):
    input('Digite o proximo número inteiro com no mínimo 3 dígitos')
    i=0
    for i in numero:
        elemento = str(numero[i])
        anterior = str(numero[i-1])
        if elemento == anterior:
            temNumeroAdjacenteIgual = True
            print('O numero digitado tem 2 digitos adjacentes iguais')
            anterior = elemento
        else:
            print('O número não tem adjacentes iguais')


