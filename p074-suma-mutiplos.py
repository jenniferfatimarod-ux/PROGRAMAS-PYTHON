#p074-suma-mutiplos.py
#imprime multiplos m en el rango de 1 a n

while True:
    print("\033[2J\033[H")
    print('imprime multiplos m en el rango de 1 a n')

    n = int(input('Hasta donde? '))
    m = int(input('Qué multiplos? '))
    c = s = 0

    for i in range(1, n+1):
        if i % m == 0:
            print(i, end = ' ')
            c=c+1
            s=s+i

    print(f'\nLos multiplos de {m} en el rango de 1 a {n} fueron {c}')
    print(f'\nLa suma de los múltiplos es: {s:,.2f}')

    if input('\nDeseas Consinuar (S/N)? ').upper()== 'N': break

print ('\n proceso terminado ')