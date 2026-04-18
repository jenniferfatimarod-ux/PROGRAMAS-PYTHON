#p118-eliminar-diccionario.py

print('\033[H\033[J')

# Crear el diccionario
municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

# Mostrar diccionario inicial
print('Diccionario inicial:')
print(municipios)

# Eliminar Apozol con del
del municipios['Apozol']
print('Después de del Apozol:')
print(municipios)

# Eliminar Fresnillo con pop()
municipios.pop('Fresnillo')
print('Después de pop(\'Fresnillo\'):')
print(municipios)

# Eliminar último elemento con popitem()
municipios.popitem()
print('Después de popitem() (eliminando Momax):')
print(municipios)

# Vaciar diccionario
municipios.clear()
print('Después de clear():')
print(municipios)