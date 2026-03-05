#p072-suma-pares-impares.py
#imprime la suma de pares o impares en un rango determinado

print("\033[2J\033[H")
print('imprime la suma de pares o impares en un rango determinado')

n = int(input('Dame el valor final? '))

cp = ci = ''
sp = si = 0

for i in range(1,n+1):
    if i % 2 == 0:
        cp = cp + ' ' + str(i)
        sp = sp + i
    else:
        ci = ci + ' ' + str(i)
        si = si + i

print('\nResumen: ')
print(f'\nLos pares: {cp} Suma: {sp}')
print(f'\nLos impares: {ci} Suma: {si}')