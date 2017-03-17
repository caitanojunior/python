numero = input('Digite um número: ')

soma = 0
num = int(numero)
i = 0

while i <= len(numero):
    ultimoDigito = num % 10
    num = num // 10
    soma = soma + ultimoDigito
    i = i + 1

print('A soma dos dígitos é:', soma)

