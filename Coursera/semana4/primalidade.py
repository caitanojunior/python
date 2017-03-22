numero = int(input('Digite um número inteiro: '))

for i in range(2, numero+1):
	if i != numero:
		i = numero % i
		if i == 0:
			print ('não primo')
			break
	else:
		print ('primo')
		break

