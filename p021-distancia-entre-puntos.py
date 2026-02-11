#p021-distancia-entre-puntos.py

#Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano. El programa debe pedir al usuario
#que ingrese las coordenadas (x,y) del punto A y las coordenadas (x,y) del punto B. Utiliza la siguiente fórmula para
#calcular la distancia:

import math as mt
print("\033[H\033[J")
print('CALCULANDO LA DISTANCIA ENTRE DOS PUNTOS\n')

ax = int(input('Introduce X del punto A: '))
ay = int(input('Introduce Y del punto A: '))
bx = int(input('Introduce X del punto B: '))
by = int(input('Introduce Y del punto B: '))

d = mt.sqrt((bx-ax)**2 + (by-ay)**2)

print(f'La distancia entre los dos puntos es: {d:.4f}')