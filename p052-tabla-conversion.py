#p052-tabla-conversion.py
#Mostrar una tabla de conversión de peso a dolar en  un rango especifico

print("\033[2J\033[H")

tc = 19.70

while True:
    while True:
        print('Imprimiendo una tabla de conversión de peso a dolar')
        pi = int(input('Dame valor inicial: '))
        pf = int(input('Dame valor final: '))
        if pi>0 and pf>0 and pi<pf : break
        print('*')
 
    c = pi

    print(f'Peso\t\tDollar')
    print('-'*30)
    while c<= pf:
        print(f'{c:>10} - {c/tc:>10.2f}')
        c = c + 1
    print('-'*30)

    if input('\nDeseas continuar (S/N): ').upper() == 'N': break

print('\nProceso terminado')