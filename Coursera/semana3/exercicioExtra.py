n = input('Digite um número inteiro maior que 0: ')
d = input('Digite um número maior ou igual a 0 e menor que 9:')

contador = 0
for i in n:
    if d == i:
        contador = contador + 1
print('O dígito', d, 'ocorre', contador, 'vezes em', n)