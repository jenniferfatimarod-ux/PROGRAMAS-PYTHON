#p031-2da-ley-de-newton.py
#Calcular los valores de fuerza, masa y aceleración 
#utilizando la segunda Ley de Newton

print("\033[2J\033[H")
print("--Calculadora de la 2da LEY DE NEWTON--\n")
print('[F] Fuerza      - f = m * a')
print('[M] Masa        - m = f / a')
print('[A] Aceleración - a = f * m')

op = input('Opción: ').upper()

if op == 'F':
    print('\nCalculando la Fuerza...')
    m = float(input('Masa? '))
    a = float(input('Aceleración? '))
    f = m * a
    print(f'La Fuerza es: {f:.2f}')
elif op == 'M':
    print('\nCalculando la Masa...')
    f = float(input('Fuerza? '))
    a = float(input('Aceleración? '))
    m = f / a
    print(f'La Fuerza es: {m:.2f}')
elif op == 'A':
    print('\nCalculando la Aceleración...')
    m = float(input('Masa? '))
    f = float(input('Fuerza? '))
    a = f * m
    print(f'La Aceleración es: {a:.2f}')
else:
    print('**Opción invalida**')

print('\nProceso terminado')