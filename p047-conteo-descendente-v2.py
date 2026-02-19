#p047-conteo-descendente-v2.py
#Contador hacia abajo versión 2

print("\033[2J\033[H")
print("--Contador descendente--\n")

z=int(input('Ingrese el número mayor: '))
n=int(input('Ingrese el decremento: '))

while z>=1:
    print(z, end=' ')
    z=z-n

print(f'\nCiclo terminado: {z}')

