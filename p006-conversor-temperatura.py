#p006-conversor-temperatura.py
#convertir temperatura de grados Celsius a farehait

print ('Convirtiendo grados Celcius a grados Farenheit: \n')

celcius = float(input ('Ingresa la temperatura en Celcius: '))

farenheit = (celcius * 9/5) + 32

print (f'{celcius:.2f} grados celcius, equivale a {farenheit:.2f} grados farenheit')
