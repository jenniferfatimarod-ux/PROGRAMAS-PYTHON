#p004-paga-trabajador.py
#calcula la paga de un trabajador

print ('Calculando la paga de un trabajador')

nombre = input ('nombre >')
horas = int(input('Horas trabajadas >'))
paga = float (input('Paga x horas >'))

tasa = 0.3
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print ('Resumen de pagos: \n')
print (f'El trabajador {nombre}, trabajó {horas} horas, con una paga de {paga}, impuesto de {tasa}%')
print (f'Paga Bruta: {pagabruta}')
print (f'Impuesto: {impuesto}')
print (f'Paga Neta: {paganeta}')