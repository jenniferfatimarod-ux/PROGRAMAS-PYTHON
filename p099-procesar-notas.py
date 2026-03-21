#p099-procesar-notas.py
#Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario
#introduzca un 0. Validar que todas las notas introducidas estén dentro del rango [0,100].
#Calcular e imprimir:
#• Cuántas notas se introdujeron.
#• La lista de notas completa.
#• La suma y el promedio de las notas.
#• La nota máxima y la nota mínima.
#• Cuántas notas y cuáles son las notas menores al promedio.

print('\033[H\033[J')
print('Procesa notas de calificaciones')

notas = []

# Leer notas
while True:
    nota = int(input('Introduzca nota (0 para detener): '))

    if nota == 0:
        break
    elif nota < 0 or nota > 100:
        print('Entrada inválida, debe ser 0-100')
    else:
        notas.append(nota)

# Resultados
print('--- Resultados ---')

cantidad = len(notas)
print('Total de notas introducidas:', cantidad)
print('Lista de notas:', notas)

suma = 0
for n in notas:
    suma += n

print('Suma de notas:', suma)

if cantidad > 0:
    promedio = suma / cantidad
else:
    promedio = 0

print('Promedio de notas:', promedio)

if cantidad > 0:
    maximo = notas[0]
    minimo = notas[0]

    for n in notas:
        if n > maximo:
            maximo = n
        if n < minimo:
            minimo = n

    print('Nota máxima:', maximo)
    print('Nota mínima:', minimo)

# Notas menores al promedio
menores = []

for n in notas:
    if n < promedio:
        menores.append(n)

print('Notas menores al promedio (', promedio, '):', len(menores))
print('Lista de notas menores al promedio:', menores)