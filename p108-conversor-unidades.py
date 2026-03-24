#p108-conversor-unidades.py
# Conversor de unidades de longitud usando diccionarios


conversiones = {
'km': 1000,
'm': 1,
'cm': 0.01,
'mm': 0.001
}

print('\033[H\033[J')
print('Conversor de unidades de longitud usando diccionarios\n')

try:
    long = int(input('Dame la longitud: '))
except -ValueError:
    print('Debe ser un número ')

while True:
    unidad = input('Unidad (km, m, cm, mm): ').lower()
    if unidad in conversiones: break

res = long * conversiones[unidad]

print(f'Una longitud de {long} {unidad} equivale a {res:.2f} metros ')