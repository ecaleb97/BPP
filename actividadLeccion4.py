import pdb

lista = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7,8], [100, 250, 43]]
print(lista)

pdb.set_trace()
maximo = [max(i) for i in lista]
print(maximo)

# Funcion get_max: De una lista dada, te devuelve el elemento mayor.
def get_max(lista):
    """Funcion get_max: Esta funcion determina el elemento maximo 
    de una lista de numeros

    Args:
        lista (list): lista de numeros

    Returns:
        int: elemento mayor de una lista dada
    """
    return max(lista)

elem_max = list(map(get_max, lista))

print("Los elementos mayores son:", elem_max)


lista_numeros = [3, 4, 8, 5, 5, 22, 13]
print(lista_numeros)

def es_primo(n):
    """Funcion es_primo: Esta funcion determina si el numero
    pasado como argumento es primo o no.

    Args:
        n (list): lista de numeros

    Returns:
        retorna si el numero es primo o no 
    """
    primo = True
    if n % 2 == 0:
        primo = False
    return primo

print("Números primos de la lista anterior:", list(filter(es_primo, lista_numeros)))