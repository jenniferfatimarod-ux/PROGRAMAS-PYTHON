#p101-mes-día-nombre.py
#Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra
#lista. Asumir 28 días para febrero. Imprimir el nombre del mes y la cantidad de días del mes correspondiente (ej.
#marzo, 30).

print('\033[H\033[J')

# Listas predefinidas
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

dias = [31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31]

# Entrada del usuario
numero = int(input('Introduzca un número de mes (1-12): '))

# Validación
if numero < 1 or numero > 12:
    print('Número inválido')
else:
    # Ajuste de índice (lista empieza en 0)
    indice = numero - 1

    print('--- Resultados ---')
    print('Mes:', meses[indice])
    print('Días:', dias[indice])