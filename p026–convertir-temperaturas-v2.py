#p026–convertir-temperaturas-v2.py
#Convertir grados farenheit o grados celcius

print("\033[H\033[J")
print('COVERTIDOR DE TEMPERATURA \n')

print('[1] de Farenheit a Celsius\n')
print('[2] de Celsius a Farenheit\n')

opcion = int(input('Elige una opción: '))

if opcion == 1:
    print('\nConversión a Celcius...')
    f = float(input('Dame los grados en Farenheit'))
    c = (f-32)*5/9
    print(f'{f} grados Farenheit equivale a {c:.2f} grados Celsius')
elif opcion == 2:
    print('\nConversión a Celcius...')
    c = float(input('Dame los grados en Celsius'))
    f = (c*5/9)+32
    print(f'{c} grados Celsius equivale a {f:.2f} grados Farenheit')
else:
    print('Opción invalida')
print('\nPrograma finalizado')