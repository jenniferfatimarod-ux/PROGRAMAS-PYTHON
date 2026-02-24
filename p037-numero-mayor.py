#p037-numero-mayor.py
#Problema: Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.
#Ejemplo de ejecución:
#• Entrada: 11, 30, -1
#• Salida: El número mayor es 30.

print("\033[2J\033[H")
print('DETERMINANDO CUAL ES EL NÚMERO MAYOR')

n1 = int(input('Intruduce el Número 1: '))
n2 = int(input('Intruduce el Número 2: '))
n3 = int(input('Intruduce el Número 3: '))


if n1 >n2 and n1>n3:
    print(f'El número mayor es {n1}')
elif n2 >n1 and n2>n3:
    print(f'El número mayor es {n2}')
elif n3 >n2 and n3>n1:
    print(f'El número mayor es {n3}')

print('\nPrograma terminado.')