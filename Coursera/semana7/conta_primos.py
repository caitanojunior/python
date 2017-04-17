def n_primos(x):
    i = 2
    while i <= x:
        while x % 2 == 0 and x != 2:
            print(i)
            i = i + 1


n = int(input("Digite um número inteiro maior ou igual a 2: "))

n_primos(n)


# corrigir código e terminar