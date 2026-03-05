#p070-conteo-descendente-for-v2.py
#imprime numeros de 100 a n con for, en decrementos de m

print("\033[2J\033[H")

print('imprime numeros descendentes del n a 1 usando for')

n = int(input('Desde donde? '))
m = int(input('Hasta donde? '))
d = int(input('Decremento? '))

for x in range(n, m-1, -d):
    print(x, end = ' ')