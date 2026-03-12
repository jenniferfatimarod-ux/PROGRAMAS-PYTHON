#p087-acceder-lista.py
#Acceder a los elementos de una lista

print("\033[2J\033[H")
print('Acceder a los elemenos de una lista')

meds = [10,20,30,40,60,70,10,20,99]

print('\nLongitud y contenido de la lista')
print(f'Cuantas mediciones son: {len(meds)}')
print(f'Todas las mediciones: {meds}')

print('\nAcceder por indice positivo')
print(f'Primera y ultima medición: {meds[0]} - {meds[8]}')

print('\nAcceder por indice negativo')
print(f'Primera y ultima medición: {meds[-9]} - {meds[-1]}')

print('\nAcceder un rango de valores de la lista')
print(f'\nDel 2 al 6: {meds[2:6]}')

print(f'\nPor saltos')
print(f'Las primeras 3 {meds[:3]}')
print(f'Las ultimas 3 {meds[6:]}')