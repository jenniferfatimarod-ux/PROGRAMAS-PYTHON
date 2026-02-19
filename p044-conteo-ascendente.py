#p044-conteo-ascendente.py
#Contador hacia arriba

print("\033[2J\033[H")
print("--Contador ascendente--\n")

z=1

while z<=100:
    print(z, end=' ')
    z=z+1

print(f'\nCiclo terminado: {z}')