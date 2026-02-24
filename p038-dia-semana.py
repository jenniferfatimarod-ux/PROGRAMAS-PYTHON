#p038-dia-semana.py
#Problema: Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana
#correspondiente, considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango,
#debe mostrar un mensaje de error.
#Ejemplo de ejecución:
#• Entrada: 2
#• Salida: Lunes
#• Entrada: 8
#• Salida: Error: Día inválido.

print("\033[2J\033[H")
print('DETERMINANDO DIA DE LA SEMANA')

n1 = int(input('Intruduce un numero del 1 a 7: '))

if n1 == 1:
    print(f'El número introducido {n1} es DOMINGO')
elif n1 == 2:
    print(f'El número introducido {n1} es LUNES')
elif n1 == 3:
    print(f'El número introducido {n1} es MARTES')
elif n1 == 4:
    print(f'El número introducido {n1} es MIERCOLES')
elif n1 == 5:
    print(f'El número introducido {n1} es JUEVES')
elif n1 == 6:
    print(f'El número introducido {n1} es VIERMES')
elif n1 == 7:
    print(f'El número introducido {n1} es SABADO')
else:
    print('\nOpción incorrecta')
print('\nPrograma terminado.')