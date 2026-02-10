#p013-funciones-matematicas-precios.py
#demostrar el ueso de funciones matemáticas para redondeo

import math as mt

print("\033[H\033[J")
print('DEMOSTRANDO EL USO DE FUNCIONES DE REDONDEO')

precio = 15.653
print(f'Precio : {precio}')
print(f'Arriba : {mt.ceil(precio)}')
print(f'Abajo : {mt.floor(precio)}')
print(f'Truncar: {mt.trunc(precio)}')
print(f'Normal : {round(precio)}')
print(f'2 Deci : {round(precio,2)}')


