#p056-contador-vocales.py
#Cuenta vocales y consonantes en una frase

print("\033[2J\033[H")
print('Cuenta vocales y consonantes ')

frase = input('Introduce la frase: ').lower()
indice = 0
v = c = o = 0
while indice < len(frase):
    #print(frase[indice])
    caracter = frase[indice]
    if 'a' <= caracter <= 'z':
        if caracter in 'aeiou':
            v = v + 1
        else:
            c = c + 1
    else:
        o = o + 1    

    indice += 1
print('\nAnalisis de la frase')
print(f'Vocales: {v}')
print(f'Consonantes: {c}')
print(f'Otros: {o}')
print(f'\n# de caracteres frase: {len(frase)} \n"{frase}"')