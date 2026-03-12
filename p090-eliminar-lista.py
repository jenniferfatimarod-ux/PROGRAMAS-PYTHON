#p090-eliminar-lista.py
#Eliminar elementos en una lista

print("\033[2J\033[H")
print('Eliminar elementos en una lista')

nums = [1,3,5,7,9,11,99,15,88,19,100]

print(f'Datos iniciales: {len(nums)} - {nums}')

print(f'\nEliminar el valor 99')
nums.remove(100)
print(f'Lista: {len(nums)} - {nums}')

print(f'\nEliminar el elemento en la pos 8')
num = nums.pop(8)
print(f'Lista: {len(nums)} - {nums} - {num}')

print(f'\nEliminar el ultimo con pop')
num = nums.pop()
print(f'Lista: {len(nums)} - {nums} - {num}')

print(f'\nEliminar todos con clear')
nums.clear()
print(f'Lista: {len(nums)} - {nums}')