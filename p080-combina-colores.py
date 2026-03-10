#p080-combina-colores.py
#genera combinaciones de colores a partir de una lista

print("\033[2J\033[H")
print("genera combinaciones de colores a partir de una lista\n")

colores = input ('Ingresa colores separados por coma: ').strip().split(',')

print(f'{len(colores)} - {colores}')

for c1 in colores:
    for c2 in colores:
        if c1 != c2:
         print(f'{c1} - {c2}')