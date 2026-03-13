#p082-compara-rendimiento-inversion.py
#Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años. El usuario
#debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos, así como
#el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final indicar qué fondo
#generó un mayor rendimiento.

print('\033[2J\033[H')

print('--- Fondo de Inversión A ---')
montoA = float(input('Monto inicial: '))
tasaA = float(input('Tasa de interés anual (%): '))

print('--- Fondo de Inversión B ---')
montoB = float(input('Monto inicial: '))
tasaB = float(input('Tasa de interés anual (%): '))

anios = int(input('Años a proyectar: '))

print('\n--- Comparación de Rendimientos Anuales ---')
print('Año | Fondo A | Fondo B')
print('-------------------------------------------')

valorA = montoA
valorB = montoB

for i in range(1, anios + 1):
    valorA = valorA * (1 + tasaA/100)
    valorB = valorB * (1 + tasaB/100)

    print(f'{i} | $ {valorA:.2f} | $ {valorB:.2f}')

print()

if valorA > valorB:
    print(f'Resultado final: El Fondo A (${valorA:.2f}) superó al Fondo B (${valorB:.2f}).')

if valorB > valorA:
    print(f'Resultado final: El Fondo B (${valorB:.2f}) superó al Fondo A (${valorA:.2f}).')

if valorA == valorB:
    print(f'Resultado final: Ambos fondos tienen el mismo rendimiento (${valorA:.2f}).')