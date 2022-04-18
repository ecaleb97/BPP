import pdb
pdb.set_trace()

def suma_cuadrados(n):
    suma_cuadrados = 0
    while(n):
        suma_cuadrados += (n % 10) * (n % 10)
        n = n // 10
    return suma_cuadrados

def esNumeroFeliz(n):
    s = n
    f = n
    while(True):
        s = suma_cuadrados(s)
        f = suma_cuadrados(suma_cuadrados(f))
        if s != f:
            continue
        else:
            break