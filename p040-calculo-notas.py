#p040-calculo-notas.py
#Problema: Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. Basado en el
#promedio, el programa deberá mostrar uno de los siguientes mensajes:
#• Menor a 6: "Quedas reprobado"
#• Desde 6 hasta menos de 7: "Pasas de panzazo"
#• Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
#• Desde 8 hasta menos de 9: "Excelente, sigue así"
#• Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena"
#Ejemplo de ejecución:
#• Entrada: 10, 9, 8, 7, 6
#• Salida: Tu promedio es 8.0. Excelente, sigue así.

print("\033[2J\033[H")
print('Calculando tu promedio')

n1 = int(input('Intruduce tu calificación 1: '))
n2 = int(input('Intruduce tu calificación 2: '))
n3 = int(input('Intruduce tu calificación 3: '))
n4 = int(input('Intruduce tu calificación 4: '))
n5 = int(input('Intruduce tu calificación 5: '))

p = (n1+n2+n3+n4+n5)/5

if p < 6:
    print(f'Tu promedio es {p}. Estás reprobado :(')
elif p>=6 and p<7:
    print(f'Tu promedio es {p}. Pasas de panzazo!')
elif p>=7 and p<8:
    print(f'Tu promedio es {p}. Muy bien, puedes mejorar!')
elif p>=8 and p<9:
    print(f'Tu promedio es {p}. Excelente, sigue así!')
elif p>=8 and p<10:
    print(f'Tu promedio es {p}. Perfecto, tu esfuerzo valió la pena!')
else:
    print('\nOpción incorrecta')

print('\nPrograma terminado.')