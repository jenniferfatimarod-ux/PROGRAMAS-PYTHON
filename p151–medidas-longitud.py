#p151–medidas-longitud.py
#Desarrolla un programa que funcione como un conversor de unidades de longitud. El programa debe mostrar un
#menú y utilizar dos funciones separadas:
#1. Una función para convertir pulgadas a centímetros (fórmula: $cm = pulgadas \times 2.54$).
#2. Una función para convertir metros a pies (fórmula: $pies = metros \times 3.281$).
#El programa debe solicitar los datos al usuario según la opción elegida y mostrar el resultado.

print('\033[H\033[J')

def pulgadas_a_cm(pulgadas):
    return pulgadas * 2.54

def metros_a_pies(metros):
    return metros * 3.281


while True:
    print('*** Conversor de Unidades ***')
    print('1. Pulgadas a Centímetros')
    print('2. Metros a Pies')
    print('3. Salir')
    
    opcion = input('Elige una opción: ')
    
    if opcion == '1':
        pulgadas = float(input('Introduce la cantidad en pulgadas: '))
        resultado = pulgadas_a_cm(pulgadas)
        print(pulgadas, 'pulgadas equivalen a', resultado, 'centímetros.\n')
    
    elif opcion == '2':
        metros = float(input('Introduce la cantidad en metros: '))
        resultado = metros_a_pies(metros)
        print(metros, 'metros equivalen a', resultado, 'pies.\n')
    
    elif opcion == '3':
        print('Saliendo del programa...')
        break
    
    else:
        print('Opción no válida. Intenta de nuevo.\n')