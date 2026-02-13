#p025-verificar-suma.py
#dados tres numeros verifica si la suma de los dos primeros es igual al tercero

print("\033[H\033[J")
print('VERIFICADOR DE SUMA \n')
print('¿Es la suma de los dos primeros igual al tercero?\n')
n1 = int(input('Dame el primero número: '))
n2 = int(input('Dame el primero número: '))
n3 = int(input('Dame el primero número: '))

suma = n1 + n2

if suma == n3:
    print(f'Correcto, la suma de {n1} y {n2} es igual a {n3}')
else:
    print(f'No coincide, la suma de {n1} y {n2} es diferente de {n3}')

print('_'*40)
print('\n Programa terminado')
