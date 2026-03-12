#p089-agregar-lista.py
#Agregar elementos a una lista

print("\033[2J\033[H")
print('Agregar elementos a una lista')

nums = [80.3,12.5,60.2,30.4]

print(f'Datos iniciales: {len(nums)} - {nums}')

print(f'\nAgregar con append 90 y 100')
nums.append(90)
nums.append(100)
print(f'Datos: {len(nums)} - {nums}')

print(f'\nInsertar el 80 en la pos 4')
nums.insert(4,80)
print(f'Datos: {len(nums)} - {nums}')

print(f'\nExtender la lista con 110,120,130')
nums.extend([110,120,130])
print(f'Datos: {len(nums)} - {nums}')