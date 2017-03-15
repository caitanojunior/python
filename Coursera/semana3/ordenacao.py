numero = ((input('Digite um número inteiro: ')))


primeiroNum = numero[0:1]
segundoNum = numero[1:2]
terceiroNum = numero[2:3]

num1 = int(primeiroNum)
num2 = int(segundoNum)
num3 = int(terceiroNum)

if(num1 < num2 < num3):
    print('crescente')
else:
    print('decrescente')