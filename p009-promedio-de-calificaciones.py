#p009-promedio-de-calificaciones.py
#Calcula el promedio de tres calificaciones in gresadad por el usuario

#entrada
print('Dame 3 calificacionnes separadas por un espacio')
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3)

#calculaer promedio
suma=cal1+cal2+cal3
promedio =suma/3

#mostrar resultados
print(f'Las calificaciones fueron: {cal1} {cal2} {cal3}')
print(f'La suma de las calificaciones es, : {suma}')
print(f'El promedio de las calificaciones es: {promedio}')

