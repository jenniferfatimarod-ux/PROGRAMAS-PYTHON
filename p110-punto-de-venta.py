#p110-punto-de-venta.py
# Simulación de un punto de venta usando diccionarios

print('\033[H\033[J')
print('Simulación de un punto de venta usando diccionarios\n')

menu = {
'taco': 18.50,
'burrito': 45.00,
'quesadilla': 35.00,
'refresco': 20.00,
'agua': 15.00
}

print('Bienvenido al taco contento')
print('Este es nuestro menú:')
for a, p in menu.items():
    print(f'- {a:<12}: ${p:.2f}')

orden = {}
tot = 0
while True:
    p = input('Que deseas ordenar? FIN para terminar ').lower()
    if p == 'fin':break
    if p not in menu:
        print('Error: no tenemos ese producto')
        continue
    cant = int(input('Cantidad: '))
    orden[p] = orden.get(p,0) + cant

for a, c in orden.items():
    st = menu[a]*c
    print(f'{c} x {a:<12}: ${st:.2f}')
    tot+=st

print(f'Total: {tot}')