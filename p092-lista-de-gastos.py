#p092-lista-de-gastos.py
#Llevar el control de una lista de gatos

print("\033[2J\033[H")
print('Control de gastos')

gastos = [450.50,120.00,85.90,230.00,55.75]
limite_gasto = 100.00

while True:
    print('---Menú de gestión de gastos---')
    print('1. Ver todos los gastos')
    print('2. Agregar un nuevo gasto')
    print('3. Modificar un gasto existente')
    print('4. Eliminar un gasto (por reembolso o error)')
    print('5. Ver resumen y total de gastos')
    print('6. Salir')
    opcion = int(input('Elige una opción (1-6): '))

    if opcion == 1:
        print(f'\nTodos los gatos: {gastos}')
    elif opcion == 2:
        nuevo_gasto = float(input('Nuevo gasto?: '))
        gastos.append(nuevo_gasto)
    elif opcion == 3:
        pos = int(input('Posisción del gasto a modificar? : '))
        gastos[pos] = float(input('Nuevo valor?: '))
    elif opcion == 4:
        gasto_eliminar = float(input('Gasto a eliminar?: '))
        gastos.remove(gasto_eliminar)
    elif opcion == 5:
        total_gastado = 0
        print('\nGastos del mes')
        for gasto in gastos:
            total_gastado += gasto
            if gasto > limite_gasto:
                print(f'Gasto excede limite {gasto}')
            else:
                print(f'Gasto nomrla: {gasto}')
        print(f'Total gastado: {total_gastado}')
    elif opcion == 6:
        print('\nGracias por utilizar este sistema')
        break
    else:
        print('\nOpcion NO VALIDA')
