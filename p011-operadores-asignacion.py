#p011-operadores-asignacion.py
#Demuestra el uso de operadores de asignación

print("\033[H\033[J")
print('='*40)
print('OPERADORES DE ASIGNACIÓN EN PYTHON')
print('='*40)

#operador de asignación básico
x=10
print(f'X = {x}')

#aplicar diferentes operadores de asignación
x += 5 ; print(f'x += 5 -> x = {x}')
x -= 3 ; print(f'x -= 3 -> x = {x}')
x *= 2 ; print(f'x *= 2 -> x = {x}')
x /= 4 ; print(f'x /= 4 -> x = {x}')
x **= 2 ; print(f'x **= 2 -> x = {x}')
x %= 5 ; print(f'x %= 5 -> x = {x}')
x //= 2 ; print(f'x //= 2 -> x = {x}')

print('='*40)