#p117-agregar-diccionario.py
# Crear el diccionario

print('\033[H\033[J')

ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}

# Mostrar ventas iniciales
print('Ventas iniciales:')
print(ventas)

# Agregar nuevos vendedores
ventas['Rocio'] = 2500
ventas['Mateo'] = 1567
ventas.update({'Andrea': 9567})
ventas.update({'Miguel': 1234})

# Mostrar ventas actualizadas
print('Ventas actualizadas:')
print(ventas)