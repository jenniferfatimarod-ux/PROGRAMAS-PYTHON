#p116-modificar-diccionario.py
# Crear el diccionario

print('\033[H\033[J')

paises = {
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica': 700
}

# Mostrar diccionario inicial
print('Diccionario inicial:')
print(paises)

# Modificar valores
paises['Brasil'] = 250
paises['Chile'] = 450
paises.update({'Bolivia': 650})
paises.update({'Jamaica': 750})

# Mostrar diccionario modificado
print('Diccionario modificado:')
print(paises)