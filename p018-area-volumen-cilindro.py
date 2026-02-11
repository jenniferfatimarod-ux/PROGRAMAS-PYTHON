#p018-area-volumen-cilindro.py

#Crea un programa que calcule el área y volumen de un cilindro. Pide al usuario que ingrese el radio y la altura del
#cilindro. Las fórmulas para el cálculo de área y de volumen son:
#• Area = PI * radio * (radio + alto)
#• Volumen = PI * (Radio * Radio) * Altura

import math as mt

print("\033[H\033[J")
print('CALCULANDO EL ÁREA Y VOLUMEN DE UN CILINDRO\n')

radio = float(input('Introduce el radio del cilindro: '))
altura = float(input('Introduce la altura del cilindro: '))

area = 2*mt.pi * radio * (radio + altura)
volumen = mt.pi * (radio * radio) * altura

print(f'El área del cilindro es: {area:.2f}')
print(f'El volumen del cilindro es: {volumen:.2f}')
