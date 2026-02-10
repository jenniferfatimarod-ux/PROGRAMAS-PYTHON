#p012-funcion-matematematicas-equacion.py
#Evaluar la función de f(x, y) = 3x^2 + √(x2 + y2) + e^(ln(x))
#usando operadores de exponenciación y la función pow
print("\033[H\033[J")
import math as mt

print('Evaluar la expresión: f(x, y) = 3x^2 + √(x2 + y2) + e^(ln(x))')
x = float(input('Dame X: '))
y = float(input('Dame Y: '))

fxy = 3 * mt.pow(x,2)+ mt.sqrt(mt.pow(x,2) + mt.pow(y,2)) + mt.exp (mt.log(x))

print(f'El resultado de f({x},{y})={fxy:.2f}')

