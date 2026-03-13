#p084-cuadro-hueco-caracter.py
#El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se
#dibujará. Luego, deberá imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar
#el contorno del mismo.

print('\033[2J\033[H')

lado = int(input('¿De qué tamaño será el lado del cuadrado? '))
caracter = input('¿Qué carácter quieres usar? ')

for i in range(1, lado + 1):
    for j in range(1, lado + 1):
        if i == 1 or i == lado or j == 1 or j == lado:
            print(caracter, end=' ')
        else:
            print(' ', end=' ')
    print()