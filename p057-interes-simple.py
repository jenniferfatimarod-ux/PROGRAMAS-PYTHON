#p057-interes-simple.py
#calculadora de interés simple (calcula años necesarios para una meta de ahorro)

print("\033[2J\033[H")
print('calcula años necesarios para una meta de ahorro')

ci = float(input('Capital inicial: '))
ti = float(input('Tasa anual(%): '))
ma = float(input('Meta de ahorro: '))

ca = ci
anio = 0
iaf = ci * (ti/100)

while ca <= ma:
    print(f'{anio} {ca} - {iaf}')
    ca = ca + iaf
    anio = anio + 1

print(f'Para alcanzar ${ma:,.2f} necesitas {anio}')
print (f'Monto final: %{ca:,.2f}')