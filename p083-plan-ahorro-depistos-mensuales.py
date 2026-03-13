#p083-plan-ahorro-depistos-mensuales.py
#El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, un depósito mensual fijo,
#una tasa de interés mensual (porcentaje), y el número total de meses del plan. El programa debe mostrar una
#tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, y el saldo final. El interés se calcula
#sobre el saldo inicial antes de sumar el nuevo depósito.

print('\033[2J\033[H')

saldo = float(input('Monto inicial de ahorro: '))
deposito = float(input('Depósito mensual: '))
tasa = float(input('Tasa de interés mensual (%): '))
meses = int(input('Número de meses a simular: '))

print('\n--- Plan de Ahorro Detallado ---')

for i in range(1, meses + 1):
    saldo_inicial = saldo
    interes = saldo_inicial * (tasa / 100)
    saldo = saldo_inicial + interes + deposito

    print(f'Mes {i}: Saldo Inicial: ${saldo_inicial:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo:.2f}')

print(f'\nAl final de {meses} meses, tendrás ${saldo:.2f}')