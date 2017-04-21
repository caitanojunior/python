# funcão que recebe uma lista e devolve a soma de todos os elementos desta lista

def soma_elementos(l):
    lista = l
    soma = 0
    for elem in lista:
        soma = soma + elem
    return soma

lista = [7,3,33,12,3,3,3,7,12,100]

print(soma_elementos(lista))
