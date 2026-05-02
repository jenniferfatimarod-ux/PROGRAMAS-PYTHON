#p150-dia-semana.py
#Escribe un programa con una función que reciba un número entero entre 1 y 7. La función debe devolver el día
#de la semana correspondiente en texto (ej: 1 = "Lunes", 7 = "Domingo"). El programa principal debe pedir el
#número al usuario, llamar a la función y mostrar el nombre del día.

print('\033[H\033[J')

def obtener_dia(numero):
    dias = {
        1: 'Lunes',
        2: 'Martes',
        3: 'Miércoles',
        4: 'Jueves',
        5: 'Viernes',
        6: 'Sábado',
        7: 'Domingo'
    }
    
    if numero in dias:
        return dias[numero]
    else:
        return None


# Programa principal
num = int(input('Introduce un número del 1 al 7: '))

resultado = obtener_dia(num)

if resultado:
    print('El día es:', resultado)
else:
    print('Error: El número debe estar entre 1 y 7.')