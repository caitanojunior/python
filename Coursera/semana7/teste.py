n = int(input("Digite um número inteiro positivo: "))

def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)

while n >= 0:
    fatorial(n)
    n = int(input("Digite um número inteiro positivo: "))


