#p152-suma-pares-impares.py
#Crea un programa que sume números pares o impares dentro de un rango especificado. El programa debe tener
#una función que reciba tres parámetros: un número de inicio, un número de fin y una letra ('P' o 'I').
#• Si la letra es 'P', la función debe devolver la suma de todos los números pares en ese rango (incluyendo
#los límites).
#• Si la letra es 'I', la función debe devolver la suma de todos los números impares en el rango.
#El programa principal debe mostrar un menú, pedir los datos al usuario y mostrar el resultado de la suma.

print('\033[H\033[J')

def suma_en_rango(inicio, fin, tipo):
    suma = 0
    
    for i in range(inicio, fin + 1):
        if tipo == 'P' and i % 2 == 0:
            suma += i
        elif tipo == 'I' and i % 2 != 0:
            suma += i
    
    return suma


# Programa principal
print('*** Suma en Rango ***')

inicio = int(input('Introduce el número inicial: '))
fin = int(input('Introduce el número final: '))
tipo = input('¿Qué deseas sumar? (P)ares o (I)mpares: ').upper()

resultado = suma_en_rango(inicio, fin, tipo)

if tipo == 'P':
    print('La suma de los números pares entre', inicio, 'y', fin, 'es:', resultado)
elif tipo == 'I':
    print('La suma de los números impares entre', inicio, 'y', fin, 'es:', resultado)
else:
    print('Error: opción no válida.')