#p051-adivina-numero.py
#Permite al usuario adivinar un numero al azar

import random
print("\033[2J\033[H")
print("Permite al usuario adivinar un numero al azar\n")

n = random.randint(1,50)
ci = 0
while True:
    i = int(input('Adivina el numero: '))
    ci+=1
    if i<n:
        print(f'Demasiado bajo ')
    elif i>n:
        print('Demasiado alto')
    else:
        print(f'Adininaste {n}')
        print(f'Usaste {ci} intentos')
        break
print('\nTermina el juego')