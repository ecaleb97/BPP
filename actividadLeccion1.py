import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('finanzas2020[1].csv', sep='\t')
    print(df)
except Exception as e:
    print('No se ha podido abrir el fichero ', e)
    
df = pd.DataFrame(df)

try:
    for i in df.columns:
        df[i] = pd.to_numeric(df[i], errors='coerce').fillna(0).astype('int')
        print('Beneficios', i, ': ', df[i].sum(), '€')
        print('\n')
except Exception as e:
    print('Error inesperado:', e)

lista_mayor_0 = []
lista_menor_0 = []

try:
    for i in df.columns:
        for y in df[i]:
            if y > 0:
                lista_mayor_0.append(y)
            else:
                lista_menor_0.append(y)
except Exception as e:
    print('Error inesperado', e)

suma_gastos_año = sum(lista_menor_0)

def media(lista_numeros):
    return sum(lista_numeros)/len(lista_numeros)

media_gastos_año = media(lista_menor_0)

print('Gasto total en el año: ', suma_gastos_año, '€')
print('Total ingresos en el año ', sum(lista_mayor_0), '€')
print('Media de gastos al año: ' , '{:.2f}'.format(media_gastos_año), '€')

lista_enero_mayor_0 = []
lista_enero_menor_0 = []
lista_febrero_mayor_0 = []
lista_febrero_menor_0 = []
lista_marzo_mayor_0 = []
lista_marzo_menor_0 = []
lista_abril_mayor_0 = []
lista_abril_menor_0 = []
lista_mayo_mayor_0 = []
lista_mayo_menor_0 = []
lista_junio_mayor_0 = []
lista_junio_menor_0 = []
lista_julio_mayor_0 = []
lista_julio_menor_0 = []
lista_agosto_mayor_0 = []
lista_agosto_menor_0 = []
lista_septiembre_mayor_0 = []
lista_septiembre_menor_0 = []
lista_octubre_mayor_0 = []
lista_octubre_menor_0 = []
lista_noviembre_mayor_0 = []
lista_noviembre_menor_0 = []
lista_diciembre_mayor_0 = []
lista_diciembre_menor_0 = []

for x in df['Enero']:
    if x > 0:
        lista_enero_mayor_0.append(x)
    else:
        lista_enero_menor_0.append(x)
            
    
for x in df['Febrero']:
    if x > 0:
        lista_febrero_mayor_0.append(x)
    else:
        lista_febrero_menor_0.append(x)

for x in df['Marzo']:
    if x > 0:
        lista_marzo_mayor_0.append(x)
    else:
        lista_marzo_menor_0.append(x)

for x in df['Abril']:
    if x > 0:
        lista_abril_mayor_0.append(x)
    else:
        lista_abril_menor_0.append(x)

for x in df['Mayo']:
    if x > 0:
        lista_mayo_mayor_0.append(x)
    else:
        lista_mayo_menor_0.append(x)

for x in df['Junio']:
    if x > 0:
        lista_junio_mayor_0.append(x)
    else:
        lista_junio_menor_0.append(x)
        
for x in df['Julio']:
    if x > 0:
        lista_julio_mayor_0.append(x)
    else:
        lista_julio_menor_0.append(x)

for x in df['Agosto']:
    if x > 0:
        lista_agosto_mayor_0.append(x)
    else:
        lista_agosto_menor_0.append(x)

for x in df['Septiembre']:
    if x > 0:
        lista_septiembre_mayor_0.append(x)
    else:
        lista_septiembre_menor_0.append(x)

for x in df['Octubre']:
    if x > 0:
        lista_octubre_mayor_0.append(x)
    else:
        lista_octubre_menor_0.append(x)

for x in df['Noviembre']:
    if x > 0:
        lista_noviembre_mayor_0.append(x)
    else:
        lista_noviembre_menor_0.append(x)

for x in df['Diciembre']:
    if x > 0:
        lista_diciembre_mayor_0.append(x)
    else:
        lista_diciembre_menor_0.append(x)


lista_ingresos_por_meses = [sum(lista_enero_mayor_0), sum(lista_febrero_mayor_0), sum(lista_marzo_mayor_0), sum(lista_abril_mayor_0), 
                            sum(lista_mayo_mayor_0), sum(lista_junio_mayor_0), sum(lista_julio_mayor_0), sum(lista_agosto_mayor_0),
                            sum(lista_septiembre_mayor_0), sum(lista_octubre_mayor_0), sum(lista_noviembre_mayor_0), 
                            sum(lista_diciembre_mayor_0)]

lista_gastos_por_meses = [sum(lista_enero_menor_0), sum(lista_febrero_menor_0), sum(lista_marzo_menor_0), sum(lista_abril_menor_0),
                          sum(lista_mayo_menor_0), sum(lista_junio_menor_0), sum(lista_julio_menor_0), sum(lista_agosto_menor_0),
                          sum(lista_septiembre_menor_0), sum(lista_octubre_menor_0), sum(lista_noviembre_menor_0),
                          sum(lista_diciembre_menor_0)]

gastos_por_meses = {'Enero': sum(lista_enero_menor_0), 
                    'Febrero': sum(lista_febrero_menor_0),
                    'Marzo': sum(lista_marzo_menor_0), 
                    'Abril': sum(lista_abril_menor_0),
                    'Mayo': sum(lista_mayo_menor_0),
                    'Junio': sum(lista_junio_menor_0), 
                    'Julio': sum(lista_julio_menor_0), 
                    'Agosto': sum(lista_agosto_menor_0),
                    'Septiembre': sum(lista_septiembre_menor_0), 
                    'Octubre': sum(lista_octubre_menor_0), 
                    'Noviembre': sum(lista_noviembre_menor_0),
                    'Diciembre': sum(lista_diciembre_menor_0)}

lista_beneficios_por_meses = {'Enero': (lista_ingresos_por_meses[0]+lista_gastos_por_meses[0]),
                              'Febrero': (lista_ingresos_por_meses[1]+lista_gastos_por_meses[1]),
                              'Marzo': (lista_ingresos_por_meses[2]+lista_gastos_por_meses[2]),
                              'Abri': (lista_ingresos_por_meses[3]+lista_gastos_por_meses[3]),
                              'Mayo': (lista_ingresos_por_meses[4]+lista_gastos_por_meses[4]),
                              'Junio': (lista_ingresos_por_meses[5]+lista_gastos_por_meses[5]),
                              'Julio': (lista_ingresos_por_meses[6]+lista_gastos_por_meses[6]),
                              'Agosto': (lista_ingresos_por_meses[7]+lista_gastos_por_meses[7]),
                              'Septiembre': (lista_ingresos_por_meses[8]+lista_gastos_por_meses[8]),
                              'Octubre': (lista_ingresos_por_meses[9]+lista_gastos_por_meses[9]),
                              'Noviembre': (lista_ingresos_por_meses[10]+lista_gastos_por_meses[10]),
                              'Diciembre': (lista_ingresos_por_meses[11]+lista_gastos_por_meses[11])}

def mas_ahorro(d):
    return max(d.keys(), key=lambda k: d[k])

def menos_ahorro(d):
    return min(d.keys(), key=lambda k: d[k])

mes_mas_ahorro = mas_ahorro(lista_beneficios_por_meses)
print('*** Mes con más ahorro ***')
print(mes_mas_ahorro)
print(lista_beneficios_por_meses[mes_mas_ahorro], '€')
print('\n')

print('*** Mes con más gastos ***')
mes_mas_gastos = menos_ahorro(gastos_por_meses)
print(mes_mas_gastos)
print(gastos_por_meses[mes_mas_gastos], '€')

lista_meses = []

for i in df.columns:
    lista_meses.append(i)

fig, ax = plt.subplots()

ax.set_ylabel('Ingresos (€)')
ax.set_title('Meses')
plt.bar(lista_meses, lista_ingresos_por_meses)
plt.show()













