#p115-crear-acceder-diccionario.py
# Crear el diccionario

print('\033[H\033[J')

dias = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo'
}

# Mostrar diccionario inicial
print('Diccionario inicial:')
print(dias)

# Acceder a elementos
print('Accediendo a elementos:')
print('Llave 1 (con []):', dias[1])
print('Llave 7 (con []):', dias[7])
print('Llave 5 (con get()):', dias.get(5))
print('Llave 7 (con get()):', dias.get(7))

# Mostrar diccionario final
print('Diccionario final:')
print(dias)