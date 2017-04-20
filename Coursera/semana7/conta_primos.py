def n_primos(x):
    x = n
    if x == 2 :
        quant = 1
    elif x == 3:
        quant = 2
    elif x <= 6:
        quant = 3
    else:
        quant = 4

    while x >= 2:
        if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
            quant = quant + 1
        x = x - 1
    return quant

n = int(input("Digite um número inteiro maior ou igual a 2: "))
print(n_primos(n))