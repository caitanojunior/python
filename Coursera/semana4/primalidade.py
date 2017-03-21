numero = int(input('Digite um número inteiro: '))

i = 2
nãoéprimo = True

while i < numero and nãoéprimo:
    if(numero % i == 0):
        éprimo = False
    else:
        i = i + 1
if(nãoéprimo):
    print('não primo')
else:
    print('primo')