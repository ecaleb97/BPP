from functools import reduce

row = 8
cols = 4

m = [[i*cols+j for j in range(cols)] for i in range(row)]
print(m)

def get_maximo(lista):
    return max(lista)

elem_maximos = list(map(get_maximo, m))

print('Los elementos mayores son: ', elem_maximos)

def es_primo(n):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    return primo

num_primos = list(filter(es_primo, elem_maximos))

print('Los primos son: ', num_primos)

def sumatorio(a, b):
    return a + b

resultado_suma = reduce(sumatorio, num_primos)
print("El resultado de la suma es:", resultado_suma)