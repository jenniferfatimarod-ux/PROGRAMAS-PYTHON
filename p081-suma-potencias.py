#p081-suma-potencias.py
#Suma de las potencias de un numero X desde x^1...x^n

print("\033[2J\033[H")
print('Suma de las potencias de un numero X desde x^1...x^n')

x = int(input('x: '))
n = int(input('n: '))

print(f'Calculando la serie S = {x}^1 + ... + {x}^{n}')

s = 0

for i in range(1, n+1):
    ta = 1

    for j in range(i):
         ta = ta * x

    print(f'{x}^{i} ',end='')
    print(' + ' if i!=n else '', end ='')
    s = s + ta

print(f'= {s}')