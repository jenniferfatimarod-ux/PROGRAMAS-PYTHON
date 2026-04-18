#p119-procesar-diccionario.py

print('\033[H\033[J')

# Listas
nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

# Crear diccionario
nomina = dict(zip(nombres, sueldos))

# Mostrar diccionario
print('Diccionario de nomina:')
print(nomina)

# Iterar llaves
print('--- Iterando Llaves (keys) ---')
for llave in nomina.keys():
    print(llave)

# Iterar valores
print('--- Iterando Valores (values) ---')
for valor in nomina.values():
    print(valor)

# Iterar llave y valor accediendo por llave
print('--- Iterando Llave y Valor (accediendo por llave) ---')
for llave in nomina:
    print(llave, '->', nomina[llave])

# Iterar con items
print('--- Iterando Llave y Valor (items) ---')
for elemento in nomina.items():
    print(elemento)

# Calculos
suma = sum(nomina.values())
promedio = suma / len(nomina)

print('--- Calculos ---')
print('Suma total de sueldos:', suma)
print('Promedio de sueldos:', promedio)