#p071-arriba-abajo.py
#Conteo arriba y abajo segun decia el usuario

while True:
    print("\033[2J\033[H")

    print('[1] Imprimir los números de 1 a n for (arriba)')
    print('[2] Imprimir los números de n a 1 for (abajo)')
    op = int(input('Elige? '))

    if op == 1:
        print('\nNumeros de 1 a n ')
        n = int(input('Hasta donde? '))
        for x in range(1, n+1):
            print(x, end = ' ')

    elif op == 2:
        print('\nNumeros de n a 1 ')
        n = int(input('Desde donde? '))
        for x in range(n, 0, -1):
            print(x, end = ' ')

    else:
        print('\nOpción invalida')

    if input('\nDeseas Consinuar (S/N)? ').upper()== 'N': break

print ('\n proceso terminado ')