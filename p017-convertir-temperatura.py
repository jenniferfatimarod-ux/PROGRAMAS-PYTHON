#p017-convertir-temperatura.py

#Desarrolla un programa que convierta una temperatura de grados Celsius a grados Fahrenheit. El programa debe
#solicitar al usuario una temperatura en Celsius y luego mostrar el resultado en Fahrenheit. La fórmula para la
#conversión es: • farenheit = (celcius × 9/5) + 32

print("\033[H\033[J")
print ('CONVIRTIENDO GRADOS CELCIUS A GRADOS FAHRENHEIT: \n')

celcius = float(input ('Ingresa la temperatura en Celcius: '))

fahrenheit = (celcius * 9/5) + 32

print (f'{celcius:.2f} grados celcius, equivale a {fahrenheit:.2f} grados fahrenheit')

print ('CONVIRTIENDO GRADOS FAHRENHEIT A GRADOS CELCIUS: \n')
f = float(input ('Ingresa la temperatura en fahrenheit: '))

c = (f - 32) / 1.8

print (f'{f:.2f} grados fahrenheit, equivale a {c:.2f} grados celcius')