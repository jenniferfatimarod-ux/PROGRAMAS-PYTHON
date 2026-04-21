#p123-conjunto-personas.py

print('\033[H\033[J')

# Listas de nombres
lista1 = ['Juan', 'Maria', 'Pedro', 'Jose', 'Rocio']
lista2 = ['Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther']

# Crear conjuntos
A = set(lista1)
B = set(lista2)

# Mostrar conjuntos
print('Conjunto A:', A)
print('Conjunto B:', B)

# Operaciones
print('\nUnion (A | B):', A | B)
print('Interseccion (A & B):', A & B)
print('Diferencia (A - B):', A - B)
print('Diferencia simetrica (A ^ B):', A ^ B)

# Verificaciones
print('\n¿{Pablo, Mateo} es subconjunto de B?:', {'Pablo', 'Mateo'}.issubset(B))
print('¿A es superconjunto de {Reynaldo, Angelica}?:', A.issuperset({'Reynaldo', 'Angelica'}))
print('¿"Pedro" esta en A?:', 'Pedro' in A)
print('¿"Lilia" no esta en B?:', 'Lilia' not in B)