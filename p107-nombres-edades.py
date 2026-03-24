#p107-nombres-edades.py
#Gestionar nombres y edades usando un diccionario

print('\033[H\033[J')
print('Gestionar nombres y edades usando un diccionario')

datos = {}
while True:
    nombre = input('Dame el nombre: ')
    if nombre == '': break
    datos[nombre] = int(input('Edad: '))

print(f'Nombres y edades: {datos} - {len(datos)}')

s=0
for n, e in datos.items():
    print(f'{n:<20} - {e:3}')
    s += e

print(f'Suma edades: {s}, Promedio edades: {s/len(datos)}')