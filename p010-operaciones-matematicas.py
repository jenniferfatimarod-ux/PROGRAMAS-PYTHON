#p010-operaciones-matematicas.py
#Demuestra el uso de los diferentes operadores aritmeticos

print("\033[H\033[J")#imprime una secuencia ANSI que borra la pantalla
print("="*50)
print("CALCULADORA DE OPERACIONES ARITMETICAS")
print("="*50)

x= float (input ('Dame el valor de x: '))
y= float (input ('Dame el valor de y: '))

print(f'Los valores de X y Y son: {x} y {y}')
print("-"*50)

#Mostrar resultados 
print(f'Suma:           {x:>6} + {y:>6} = {x + y:>10.2f}')
print(f'Resta:          {x:>6} - {y:>6} = {x - y:>10.2f}')
print(f'Multiplicación: {x:>6} * {y:>6} = {x * y:>10.2f}')
print(f'División:       {x:>6} / {y:>6} = {x / y:>10.2f}')
print(f'Modulo:         {x:>6} % {y:>6} = {x % y:>10.2f}')
print(f'Exponente:      {x:>6} ** {y:>6} = {x ** y:>10.2f}')
print(f'División E:     {x:>6} // {y:>6} = {x // y:>10.2f}')

print('-' * 50)