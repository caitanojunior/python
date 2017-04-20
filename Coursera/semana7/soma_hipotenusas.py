# ------------------------------------------------------------------------
# Escreva uma função 'soma_hipotenusas' que receba como parâmetro um
# número inteiro positivo e retorna a soma de todos os inteiros
# entre 1 e n que são comprimento da hipotenusa de algum triângulo
# retângulo com catetos inteiros.
# ------------------------------------------------------------------------

def calc_hipotenusa(a, b):
    return ((a * a) + (b * b))


def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        _c = (c * c)
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (_c == calc_hipotenusa(a, b)):
                    # print(a, " - " ,b , " - " , c)
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1

    return soma