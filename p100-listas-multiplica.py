#p100-listas-multiplica.py
#Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las
#dos listas correspondientes. Imprimir las tres listas.

print('\033[H\033[J')

lista_a = []
lista_b = []
lista_c = []

print('Introduzca 5 números para la Lista A:')
for i in range(5):
    num = int(input('Número: '))
    lista_a.append(num)

print('Introduzca 5 números para la Lista B:')
for i in range(5):
    num = int(input('Número: '))
    lista_b.append(num)

# Multiplicar elementos
for i in range(5):
    resultado = lista_a[i] * lista_b[i]
    lista_c.append(resultado)

# Resultados
print('--- Resultados ---')
print('Lista A:', lista_a)
print('Lista B:', lista_b)
print('Lista C (A * B):', lista_c)