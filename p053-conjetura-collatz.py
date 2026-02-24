#p053-conjetura-collatz.py
#Calculo de conjetura de Collatz

while True:
    print("\033[2J\033[H")
    print('Imprime la conjetura de Collatz')

    while True:
        n = int(input('Dame un número: '))
        if n>1: break

    p = 0
    while True:
        if n == 1: break
        print(n,end = ' ')
        p+=1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

    print (n,end = ' ')
    print(f'\nPasos para llegar a 1: {p}')

    if input('\nDeseas continuar (S/N): ').upper() == 'N': break

print('\nProceso terminado')