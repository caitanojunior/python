numero = int(input('Entre com o número: '))
i = 1
prod = 0
while prod < numero:
	prod = i*(i+1)*(i+2)
	i += 1

if prod == numero:
	print ('%d é triangular' %numero)
else:
    print('%d não é triangular' % numero)