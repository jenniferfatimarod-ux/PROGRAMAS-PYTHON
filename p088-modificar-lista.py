#p088-modificar-lista.py
#modificar los elementos de una lista

print("\033[2J\033[H")
print('modificar los elementos de una lista')

califs =[10,9,8.5,6.5,9.8,7,5,6.2,9.5]

print(f'Todas las calificaciones: {len(califs)} - {califs}')

print(f'\n Modificar cal 0 y 1 con 7 y 7')
califs[0]=7
califs[1]=7
print(f'Todas las calificaciones: {len(califs)} - {califs}')

print(f'\n Modificar cal 0 y 1 con 7 y 7')
califs[2:5]=[9,9,9]
print(f'Todas las calificaciones: {len(califs)} - {califs}')