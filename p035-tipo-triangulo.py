#p035-tipo-triangulo.py

print("\033[2J\033[H")
print("--Clasificador de triangulos--\n")

print("Ingresa las medidas de los lados de tu triangulo\n")

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 == l2 == l3:
    print('EQUILATERO')
elif l1 == l2 or l1 == l3 or l2 ==l3:
    print('ISOCELES')
else:
    print('ESCALENO')

print('Programa terminado')