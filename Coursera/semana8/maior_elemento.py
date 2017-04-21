# funcão recebe uma lista e retorna um inteiro com o maior valor

def maior_elemento(l):
    lista = l
    new_lista = list(lista)
    new_lista.sort()
    return new_lista[-1]

lista = [2,9,38,8,6,10,15] #lista exemplo

print(maior_elemento(lista))