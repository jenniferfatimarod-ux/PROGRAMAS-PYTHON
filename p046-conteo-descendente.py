#p046-conteo-descendente.py
#Contador hacia abajo

print("\033[2J\033[H")
print("--Contador descendente--\n")
print("--Números de 100 a 1--\n")

#n=int(input('Ingrese el limite: '))
z=100

while z>=1:
    print(z, end=' ')
    z=z-1

print(f'\nCiclo terminado: {z}')
