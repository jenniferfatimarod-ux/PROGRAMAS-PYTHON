#p055-tabla-multiplicar-while-v2.py
#imprime todas las tablas desde el 1 hasta el 10

while True:
    print("\033[2J\033[H")
    print('Imprime las tablas de multiplicar ')

    while True:
        n = int(input('Hasta que tabla? '))
        m = int(input('Hasta que numero? '))
        if m>0 and n>0: break

    t = 1
    while t <= n:

        z = 1
        print(f'\nTabla del {t}: ')

        while z <= m:
            print(f'{t:>2} x {z:>2} = {z*t:>2}')
            z = z + 1

        t = t + 1

    if input('\nDeseas continuar (S/N): ').upper() == 'N': break

print('\nProceso terminado')