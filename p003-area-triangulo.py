#p003-area-triangulo.py
#Caluclar el area de un triangulo

print('Calculando el área de un triángulo\n')

print ('Dame la base y la altura separadas por un Enter')

base, altura = int (input()), int(input ())

area = (base * altura)/ 2

print (f'El triangulo de base {base:.2f} y altura {altura:.2f} tiene un área de {area:.2f}')

