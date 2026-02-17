#p032-aceptar-estudiante.py
#controla el acceso a la uni en base a dos condiciones

print("\033[2J\033[H")
print("--Programa de aceptación de estudiantes--\n")

nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

if edad < 18:
    print(f'Lo sentimos {nombre} solo permitimos mayores de 18 años')
else:
    print('Ingresa 2 calificaciones separadas por enter: ')
    cal1 = float(input())
    cal2 = float(input())
    if cal1<8 or cal2<8:
        print('Lo sentimos {nombre}, se requieren calificaciones mayores a 8')
    else:
        print(f'{nombre} BIENVENIDO a la universidad')

print('\n Proceso terminado')