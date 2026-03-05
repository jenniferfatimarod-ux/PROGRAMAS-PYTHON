#p073-suma-promedio-numeros.py
#Suma de n número introducidos por usuario usando for

while True:
    print("\033[2J\033[H")
    print('Suma de n número introducidos por usuario usando for')

    cuantos = int(input('Cuantos numeros? '))
    suma = 0
    cad = ''

    for i in range(1, cuantos+1):
        n = float(input(f'Número{i}/{cuantos}? '))
        suma = suma + n
        cad = cad + ' ' + str(n)

    print(f'Los numeros son: {cad}')
    print(f'La suma es: {suma}')
    print(f'El promedio es: {suma/cuantos}')

    if input('\nDeseas Consinuar (S/N)? ').upper()== 'N': break

print ('\n proceso terminado ')