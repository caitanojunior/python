numero = int(input('Digite um número inteiro: '))

i = 2
ehprimo = True

while i < numero and ehprimo:
	if numero % i == 0:
		ehprimo = False
	i = i + 1

if(ehprimo):
	print('primo')
else:
	print('não é primo')