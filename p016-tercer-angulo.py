#p016-tercer-angulo.py

#Escribe un programa que determine el tercer ángulo de un triángulo. El programa debe pedir al usuario que ingrese
#las medidas de dos ángulos del triángulo. Utiliza la siguiente fórmula para encontrar el ángulo faltante:
#• angulo3 = 180 – (angulo1 + angulo2)

import math as mt

print("\033[H\033[J")
print('CALCULANDO EL TERCER ÁNGULO DE UN TRIÁNGULO\n')

angulo1 = float(input('Introduce la medida del ángulo 1: '))
angulo2 = float(input('Introduce la medida del ángulo 2: '))

angulo3 = 180-(angulo1 + angulo2)

print(f'El tercer ángulo del triangulo es: {angulo3:.2f}')