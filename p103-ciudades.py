#p103-ciudades.py
#Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:
#• Cuántos elementos tiene la lista.
#• La lista completa.
#• La lista ordenada en orden descendente.
#• Cuántas ciudades inician con una letra consonante y sus nombres.

print('\033[H\033[J')

ciudades = []

# Leer ciudades
while True:
    ciudad = input('Introduzca nombre de ciudad ($ para detener): ')
    
    if ciudad == '$':
        break
    else:
        ciudades.append(ciudad)

# Resultados
print('--- Resultados ---')

print('Total de ciudades introducidas:', len(ciudades))
print('Lista original:', ciudades)

# Lista ordenada descendente
ordenada = sorted(ciudades, reverse=True)
print('Lista ordenada descendente:', ordenada)

# Ciudades que inician con consonante
vocales = 'aeiouAEIOU'
consonantes = []

for c in ciudades:
    if c[0] not in vocales:
        consonantes.append(c)

print('Ciudades que inician con consonante:', len(consonantes))
print('Lista de ciudades con consonante inicial:', consonantes)