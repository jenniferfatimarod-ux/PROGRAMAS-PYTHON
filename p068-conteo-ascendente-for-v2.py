#p068-conteo-ascendente-for-v2.py
#imprime numeros de 1 a n usando for con incrementos de m

print("\033[2J\033[H")

print('imprime numeros del 1 a n usando for')

p = int(input('Desde donde? '))
n = int(input('Hasta donde? '))
i = int(input('Ingremento? '))

for h in range(p, n+1, i):
    print(h, end = ' ')