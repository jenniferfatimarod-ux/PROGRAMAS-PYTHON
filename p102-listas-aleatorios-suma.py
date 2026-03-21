#p102-listas-aleatorios-suma.py
#Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de
#los correspondientes de las listas A y B, solo si AMBOS elementos son impares; de lo contrario, el elemento de
#la tercera lista será 0. Imprimir las 3 listas.

print('\033[H\033[J')

import random

lista_a = []
lista_b = []
lista_c = []

# Generar listas aleatorias
for i in range(10):
    lista_a.append(random.randint(1, 20))
    lista_b.append(random.randint(1, 20))

print('--- Listas Generadas ---')
print('Lista A:', lista_a)
print('Lista B:', lista_b)

# Crear lista C
for i in range(10):
    if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
        suma = lista_a[i] + lista_b[i]
        lista_c.append(suma)
    else:
        lista_c.append(0)

print('--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---')
print('Lista C:', lista_c)