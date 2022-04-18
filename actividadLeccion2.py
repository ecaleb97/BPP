import pytest
import actividadLeccion1

def test_media():
    lista_numeros = [2, 4, 6, 8, 10]
    assert actividadLeccion1.media(lista_numeros) == 6
    
def test_mas_ahorro():
    d = {'Enero': 4,
         'Febrero': 5,
         'Marzo': 7,
         'Abril': 9,
         'Mayo': 10,
         'Junio': 14,
         'Julio': 20,
         'Agosto': 13,
         'Septiembre': 2,
         'Octubre': 1,
         'Noviembre': 8,
         'Diciembre': 11}
    assert actividadLeccion1.mas_ahorro(d) == 'Julio'

def test_menos_ahorro():
    d = {'Enero': 4,
         'Febrero': 5,
         'Marzo': 7,
         'Abril': 9,
         'Mayo': 10,
         'Junio': 14,
         'Julio': 20,
         'Agosto': 13,
         'Septiembre': 2,
         'Octubre': 1,
         'Noviembre': 8,
         'Diciembre': 11}
    assert actividadLeccion1.menos_ahorro(d) == 'Octubre'