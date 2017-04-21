# Funcão que recebe valores digitados e imprime em ordem inversa da que foram digitados
def inverte():
    numero = 1
    lista = []
    while numero > 0:
        numero = int(input("digite um número: "))
        lista.append(numero)
    new_lista = lista.remove(lista[-1])
    lista.reverse()
    for x in lista:
        print(x)

inverte()