#p054-tabla-multiplicar-while-v1.py
#imprime una tabla t desde 1 hasta n

while True:
    print("\033[2J\033[H")
    print('Imprime una tabla t desde 1 hasta n')

    while True:
        t = int(input('Tabla: '))
        n = int(input('Hasta donde: '))
        if t>0 and n>0: break

    z = 1
    while z <= n:
        print(f'{z:>2} x {t:>2} = {z*t:>2}')
        z = z + 1

    if input('\nDeseas continuar (S/N): ').upper() == 'N': break

print('\nProceso terminado')