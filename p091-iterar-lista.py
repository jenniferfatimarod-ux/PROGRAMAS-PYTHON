#p091-iterar-lista.py
#iterar por los elementos de una lista

print("\033[2J\033[H")
print('iterar por los elementos de una lista')

nums = [2,4,6,8,10,12,14,16]

print(f'Datos iniciales: {len(nums)} - {nums}')

print(f'\n\n1. Iteración por elementos')
for n in nums:
    print(n,end=' ')

print(f'\n\n2. Iteración por indice')
for i in range(len(nums)):
    print(nums[i],end=' ')

print(f'\n\n3. Iteración por elemento y sumar 2')
for n in nums:
    print(n+2,end=' ')

print(f'\n\n4. Iteración por indice y sumar 10, se modifica')
print(f'Datos iniciales: {nums}')
for i in range(len(nums)):
    nums[i] = nums[i]+10
print(f'Datos finales: {nums}')

