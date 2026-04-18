#p120-contar-caracteres.py

print('\033[H\033[J')

# Pedir cadena al usuario
cadena = input('Ingrese una cadena: ')

# Diccionario vacío
frecuencia = {}

# Recorrer cada caracter
for caracter in cadena:
    if caracter in frecuencia:
        frecuencia[caracter] = frecuencia[caracter] + 1
    else:
        frecuencia[caracter] = 1

# Mostrar resultado
print('Resultado:')
print(frecuencia)