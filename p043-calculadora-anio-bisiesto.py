#p043-calculadora-anio-bisiesto.py
#Problema: Escribe un programa que determine si un año, ingresado por el usuario, es bisiesto. Un año es bisiesto
#si cumple una de las siguientes condiciones:
#1. Es divisible por 4, pero no es divisible por 100.
#2. Es divisible por 400.
#El programa debe indicar claramente si el año es bisiesto o no.
#Ejemplos de ejecución:
#• Entrada: 2024
#• Salida: El año 2024 es bisiesto. (Porque es divisible por 4 pero no por 100).
#• Entrada: 1900
#• Salida: El año 1900 no es bisiesto. (Porque es divisible por 100 pero no por 400).
#• Entrada: 2000
#• Salida: El año 2000 es bisiesto. (Porque es divisible por 400).
#• Entrada: 2023
#• Salida: El año 2023 no es bisiesto. (Porque no es divisible por 4).

print("\033[2J\033[H")
print('Calculadora de año bisiesto')

a = int(input('Ingrese el año: '))
b = a % 4
c = a % 100
d = a % 400

if b == 0 and c!=0:
  print(f'El año {a} es bisiesto. (Porque es divisible por 4 pero no por 100).')
elif c == 0 and d!=0:
  print(f' El año {a} no es bisiesto. (Porque es divisible por 100 pero no por 400).')
elif  d == 0:
  print(f'El año {a} es bisiesto. (Porque es divisible por 400).')
elif b != 0:
  print(f'El año {a} no es bisiesto. (Porque no es divisible por 4).')
  
else:
  print('Opción incorrecta')

print('\nPrograma terminado.')