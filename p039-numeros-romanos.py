#p039-numeros-romanos.py
#Problema: Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en
#números romanos. Si el número está fuera de este rango, debe mostrar un mensaje de error.
#Ejemplo de ejecución:
#• Entrada: 4
#• Salida: IV
#• Entrada: 11
#• Salida: Error: Número inválido.

print("\033[2J\033[H")
print('NUMEROS ROMANOS')

n1 = int(input('Intruduce un numero del 1 al 10: '))

if n1 == 1:
    print(f'El número introducido {n1} en romano es I')
elif n1 == 2:
    print(f'El número introducido {n1} en romano es II')
elif n1 == 3:
    print(f'El número introducido {n1} en romano es III')
elif n1 == 4:
    print(f'El número introducido {n1} en romano es IV')
elif n1 == 5:
    print(f'El número introducido {n1} en romano es V')
elif n1 == 6:
    print(f'El número introducido {n1} en romano es VI')
elif n1 == 7:
    print(f'El número introducido {n1} en romano es VII')
elif n1 == 8:
    print(f'El número introducido {n1} en romano es VIII')
elif n1 == 9:
    print(f'El número introducido {n1} en romano es IX')
elif n1 == 10:
    print(f'El número introducido {n1} en romano es X')
else:
    print('\nOpción incorrecta')

print('\nPrograma terminado.')