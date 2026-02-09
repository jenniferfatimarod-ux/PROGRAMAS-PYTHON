#p001-hola-mundo.py
#lee datos y envía un saludo

print ('Leyendo datos y enviando un saludo: \n')
#entrada
nombre = input ('Dame tu nombre?')
edad = int (input ('Dame tu edad?'))
peso = float(input ('Dame tu peso?'))
#salida
print (f'{nombre}bienvenido a python, tu edad es {edad}, tu peso {peso}')
print(type(nombre))
print(type(edad))
print(type(peso))