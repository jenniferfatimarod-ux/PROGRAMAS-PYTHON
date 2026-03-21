#p104-lista-impares.py
#Leer un entero n. Llenar una lista con los primeros n números impares.
#Calcular e imprimir:
#• La suma y el promedio de los números.
#• Los números que son divisibles entre 3 y su suma.
#• Pedir un elemento a buscar en la lista original e indicar si está y en qué posición (índice).

print('\033[H\033[J')

# Leer n
n = int(input('Introduzca la cantidad de números impares (n): '))

impares = []

# Generar los primeros n números impares
numero = 1
for i in range(n):
    impares.append(numero)
    numero += 2

print('--- Generación de Lista ---')
print('Lista de los primeros', n, 'números impares:', impares)

# Cálculos
suma = 0
for x in impares:
    suma += x

promedio = suma / n if n > 0 else 0

print('--- Cálculos ---')
print('Suma de los números:', suma)
print('Promedio de los números:', promedio)

# Divisibles entre 3
div3 = []
suma_div3 = 0

for x in impares:
    if x % 3 == 0:
        div3.append(x)
        suma_div3 += x

print('--- Divisibles entre 3 ---')
print('Números divisibles entre 3:', div3)
print('Suma de los números divisibles entre 3:', suma_div3)

# Búsqueda
buscar = int(input('Introduzca elemento a buscar: '))

encontrado = False

for i in range(len(impares)):
    if impares[i] == buscar:
        print('Result: El elemento', buscar, 'está en la lista en la posición (índice)', i)
        encontrado = True
        break

if not encontrado:
    print('Result: El elemento', buscar, 'no está en la lista')