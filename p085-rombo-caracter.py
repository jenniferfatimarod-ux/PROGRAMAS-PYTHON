#p085-rombo-caracter.py
#Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo.
#El programa deberá dibujar el rombo utilizando el carácter que el usuario elija.

print('\033[2J\033[H')

n = int(input('Dame un número impar para la altura: '))
caracter = input('¿Qué carácter quieres usar? ')

mitad = n // 2

for i in range(0, mitad + 1):
    for j in range(0, mitad - i):
        print(' ', end='')
    for j in range(0, 2 * i + 1):
        print(caracter, end='')
    print()

for i in range(mitad - 1, -1, -1):
    for j in range(0, mitad - i):
        print(' ', end='')
    for j in range(0, 2 * i + 1):
        print(caracter, end='')
    print()