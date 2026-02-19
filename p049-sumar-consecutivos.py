#p049-sumar-consecutivos.py
#Sumar numeros hasta 5000

print("\033[2J\033[H")
print("Cuantos boletos tengo que hacer para juntar 5000\n")

n=int(input('Cuanto quieres recaudar: '))
b = 0
d = 0

while b<200:
    b=b+1
    d=d+b
    print(b, end=' ')

    if d>=n:
      print('Listo')
      break

print(f'\nCiclo terminado: Boletos {b}, {d}')