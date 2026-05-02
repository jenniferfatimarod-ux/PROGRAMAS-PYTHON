#p155-estadisticas-basicas.py
#Crea un programa que calcule estadísticas básicas (poblacionales) para una lista de números. El programa debe incluir:
#1. Una función para leer una lista de números enteros.
#2. Funciones separadas para calcular y devolver cada una de las siguientes estadísticas:
# Número mayor
# Número menor
# Media (promedio)
# Varianza poblacional
# Desviación estándar poblacional
#El programa principal debe leer la lista e imprimir todos los resultados estadísticos de forma clara.

print('\033[H\033[J')

import math


def leer_lista():
    entrada = input('Dame números (separados por espacio): ')
    numeros = entrada.split()
    lista = []
    
    for n in numeros:
        lista.append(int(n))
    
    return lista


def calcular_mayor(lista):
    return max(lista)


def calcular_menor(lista):
    return min(lista)


def calcular_media(lista):
    return sum(lista) / len(lista)


def calcular_varianza(lista):
    media = calcular_media(lista)
    suma = 0
    
    for x in lista:
        suma += (x - media) ** 2
    
    return suma / len(lista)   # poblacional


def calcular_desviacion(lista):
    varianza = calcular_varianza(lista)
    return math.sqrt(varianza)


# Programa principal
lista = leer_lista()

print('Lista de números:', lista)
print('Estadísticas:')

media = calcular_media(lista)
mayor = calcular_mayor(lista)
menor = calcular_menor(lista)
varianza = calcular_varianza(lista)
desviacion = calcular_desviacion(lista)

print('Media :', round(media, 3))
print('Mayor :', mayor)
print('Menor :', menor)
print('Varianza :', round(varianza, 3))
print('Desviación estándar:', round(desviacion, 3))