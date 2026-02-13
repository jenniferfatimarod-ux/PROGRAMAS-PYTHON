#p024-verificar-numero-v2.py
#verificar si un número entero es positivo, negativo o cero
#Usando if esle

print("\033[H\033[J")
print('VERIFICANDO SI UN NUMERO ENTERO ES POSITIVO, NEGATIVO O CERO \n')

numero = int(input('Dame un número entero: '))

if numero > 0:
    print ('Número positivo👍')
elif numero < 0:
    print ('Número negativo😊')
else:
    print ('Tu número es cero😁')

print('\n Programa terminado')
