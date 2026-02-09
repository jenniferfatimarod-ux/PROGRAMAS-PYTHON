#p005-calculador-imc.py
#Calcular el IMC de una persona

print('Calculando el indice de masa corporal (IMC)')

peso_kg = float(input('Dame tu peso en kilogramos:'))
altura_m = float (input ('Dame tu alñtura en metros: '))

# ** eleva un numero a una potencia
imc = peso_kg /(altura_m **2)

print(f'Si tienes un peso de {peso_kg} y una altura de {altura_m} tu IMC es {imc:.f}')

