#p014-funciones-trigonometricas.py
#demostrar el uso de las funciones trigonometricas

import math as mt

print("\033[H\033[J")
print('DEMOSTRAR EL USO DE FUNCIONES TRIGONOMETRICAS\n')

angulo = 90 #grados
radianes = mt.radians(angulo) #convierte a radianes

seno =mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

grados = mt.degrees(radianes) #convierte a grados

salida = ('Resumen de funciones \n'
          f'Seno : {seno:.4f} \n'
          f'Coseno : {coseno:.4f} \n'
          f'Tangente : {tangente:.4f} \n'
          f'El angulo {angulo:.4f} grados, en radianes equivale a {radianes:.4f} \n'
          f'El angulo {radianes:.4f} radianes, en grados equivale a {grados:.4f} grados \n'
          )

print(salida)
