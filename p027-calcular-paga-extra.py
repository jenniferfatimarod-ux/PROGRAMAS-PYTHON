#p027-calcular-paga-extra.py
#Calcula la paga de un trabajador considerando horas extras

print("\033[H\033[J")
print('CALCULANDO LA PAGA DE UN TRABAJADOR CONSIDERANDO QUE LAS HORAS EXTRAS SE PAGAN AL DOBLE \n')

print('Dame los datos del trabajador: \n')

nombre = input('Nombre:')
horas = int(input('Horas: '))
paga_horas = float(input('Paga por hora: '))

horas_normales = 40
paga_normal = horas_normales * paga_horas

horas_extra = paga_extra = 0
if horas > 40:
    horas_extra = horas - 40
    paga_extra = horas_extra * (paga_horas*2)
    total = paga_normal + paga_extra
else:
    total = paga_normal

print('Calculo completado')
print(f'\n El trabajador {nombre}, trabajó {horas} horas con una paga de {paga_horas} pesos')
print(f'{nombre} trabajó {horas_extra} horas extra')
print(f'Paga normal: ${paga_normal:13,.2f}')
print(f'Paga extra: ${paga_extra:13,.2f}')
print(f'Paga total: ${total:13,.2f}')