#p022-resistencia-equivalente-paralelo.py

#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.
#El programa debe solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias (R1, R2, R3 y R4).
#Luego, debe calcular la resistencia total usando la siguiente fórmula:

import math as mt
print("\033[H\033[J")
print('CALCULANDO LA RESISTENCIA TOTAL DE CUATRO RESISTENCIAS EN PARALELO\n')

r1 = float(input('Introduce el valor de R1: '))
r2 = float(input('Introduce el valor de R2: '))
r3 = float(input('Introduce el valor de R3: '))
r4 = float(input('Introduce el valor de R4: '))

rt = 1 / ((1/r1)+(1/r2)+(1/r3)+(1/r4))

print(f'La resistencia total en paralelo es: {rt}')