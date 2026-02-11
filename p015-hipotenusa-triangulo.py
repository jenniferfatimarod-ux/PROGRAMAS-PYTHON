#p015-hipotenusa-triangulo.py

#Crea un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo. El programa debe solicitar
#al usuario que ingrese la longitud de los dos lados (catetos) del triángulo. Para el cálculo, utiliza la siguiente
#fórmula: • hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

import math as mt

print("\033[H\033[J")
print('CALCULANDO LA HIPOTENUSA DE UN TRIANGULO RECTANGULO\n')

cateto1 = float(input('Introduce la longitud del Cateto 1: '))
cateto2 = float(input('Introduce la longitud del Cateto 2: '))

hipotenusa = mt.sqrt(cateto1*cateto1 + cateto2*cateto2)

print(f'La hipotenusa del triangulo rectangulo es: {hipotenusa:.2f}')