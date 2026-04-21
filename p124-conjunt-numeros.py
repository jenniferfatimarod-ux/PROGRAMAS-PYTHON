#p124-conjunt-numeros.py

print('\033[H\033[J')

# Listas de numeros
lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

# Crear conjuntos
A = set(lista1)
B = set(lista2)
C = set(lista3)

# Mostrar conjuntos
print('Conjunto A:', A)
print('Conjunto B:', B)
print('Conjunto C:', C)

# Operaciones
print('\nUnion (A | B):', A | B)
print('Union (B | C):', B | C)
print('Diferencia (A - C):', A - C)
print('Diferencia simetrica (B ^ C):', B ^ C)
print('Interseccion (B & C):', B & C)

# Verificaciones
print('\n¿A es subconjunto de B?:', A.issubset(B))
print('¿C es subconjunto de A?:', C.issubset(A))
print('¿100 esta en A?:', 100 in A)
print('¿60 esta en A, B y C?:', 60 in A and 60 in B and 60 in C)
print('¿900 no esta en C?:', 900 not in C)