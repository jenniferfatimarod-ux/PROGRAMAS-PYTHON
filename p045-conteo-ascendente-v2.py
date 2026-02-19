#p045-conteo-ascendente-v2.py
#Contador hacia arriba versión 2

print("\033[2J\033[H")
print("--Contador ascendente--\n")
print("--Números de 0 a n--\n")

n=int(input('Ingrese el limite: '))
m=int(input('Ingrese el avance: '))
z=0

while z<=n:
    print(z, end=' ')
    z=z+m

print(f'\nCiclo terminado: {z}')
