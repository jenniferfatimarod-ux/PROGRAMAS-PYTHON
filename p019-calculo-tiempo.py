#p019-calculo-tiempo.py

#Diseña un programa que tome una cantidad de horas como un número entero. El programa debe calcular y mostrar
#el equivalente de ese tiempo en:
#• Días (considerando que 1 día tiene 24 horas)
#• Minutos (considerando que 1 hora tiene 60 minutos)
#• Segundos (considerando que 1 minuto tiene 60 segundos)

print("\033[H\033[J")
print('CALCULANDO DIAS, MINUTOS Y SEGUNDOS DE UNA CANTIDAD DE HORAS\n')

horas = float(input('Introduce la cantidad de horas: '))

dias = horas / 24
minutos = horas * 60
segundos = horas *60*60

print(f'El tiempo: {horas:.2f} horas equivale a:\n '
          f'Días:      {dias:.2f} \n'
          f'Minutos:   {minutos:.2f} \n'
          f'Segundos:  {segundos:.2f} \n')