#p002-area-circulo.py
#Caulcular el área de un circulo

import math #importa el modulo de funciones mátematicas

print('Calculando el área de un Circulo \n\n')

print ('Dame el radio?')
radio = float (input())

area = math.pi * math.pow(radio,2)

print (f'El circulo de radio {radio:.2f} tiene un area de{area:.f}')

