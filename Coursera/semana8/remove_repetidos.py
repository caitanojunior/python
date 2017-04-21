#FUNÇÃO QUE RECEBE UMA LISTA COMO PARÂMETRO E DEVOLVE ORDENADA E SEM REPETIÇÃO

def remove_repetidos(l):
        lista = l
        new_lista = set(lista)
        final_list = list(new_lista)
        final_list.sort()
        return final_list

lista = [7,3,33,12,3,3,3,7,12,100]

print(remove_repetidos(lista))

