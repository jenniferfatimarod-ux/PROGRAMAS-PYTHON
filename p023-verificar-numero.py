#p023-verificar-numero.py
#verificar si un número entero es positivo, negativo o cero

print("\033[H\033[J")
print('VERIFICANDO SI UN NUMERO ENTERO ES POSITIVO, NEGATIVO O CERO \n')

numero = int(input('Dame un número entero: '))

if numero > 0:
    print ('Número positivo👍')

if numero < 0:
    print ('Número negativo😊')

if numero == 0:
    print ('Tu número es cero😁')

print('\n Programa terminado')