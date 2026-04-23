# p125-segundo-examen-parcial.py

print('\033[H\033[J')

vuelos = []

while True:
    print('\n--- Registro de vuelo ---')
    
    numero_vuelo = input('Número de vuelo (enter para terminar): ')
    if numero_vuelo == '':
        break

    origen = input('Origen: ')
    destino = input('Destino: ')
    aerolinea = input('Aerolínea: ')
    pasajeros = int(input('Número de pasajeros: '))
    tarifa = float(input('Tarifa: '))

    # Diccionario con los datos del vuelo
    vuelo = {
        'numero_vuelo': numero_vuelo,
        'origen': origen,
        'destino': destino,
        'aerolinea': aerolinea,
        'pasajeros': pasajeros,
        'tarifa': tarifa
    }

    # Se agrega a la lista
    vuelos.append(vuelo)


print('\n=== DATOS CRUDOS ===')
print(vuelos)


print('\n=== TABLA DE VUELOS ===')
print(f'{'Vuelo':<10} {'Origen':<20} {'Destino':<20} {'Aerolínea':<15} {'Pasajeros':<10} {'Tarifa':<10}')

for v in vuelos:
    print(f'{v['numero_vuelo']:<10} {v['origen']:<20} {v['destino']:<20} {v['aerolinea']:<15} {v['pasajeros']:<10} {v['tarifa']:<10.2f}')


print('\n=== RESUMEN ===')

total_vuelos = len(vuelos)
print(f'Total de vuelos: {total_vuelos}')

# Vuelos por aerolínea
vuelos_por_aerolinea = {}
for v in vuelos:
    aer = v['aerolinea']
    vuelos_por_aerolinea[aer] = vuelos_por_aerolinea.get(aer, 0) + 1

print('\nVuelos por aerolínea:')
for aer, cantidad in vuelos_por_aerolinea.items():
    print(f'{aer}: {cantidad}')

# Vuelos por destino
vuelos_por_destino = {}
for v in vuelos:
    dest = v['destino']
    vuelos_por_destino[dest] = vuelos_por_destino.get(dest, 0) + 1

print('\nVuelos por destino:')
for dest, cantidad in vuelos_por_destino.items():
    print(f'{dest}: {cantidad}')

# Pasajeros
total_pasajeros = sum(v['pasajeros'] for v in vuelos)
promedio_pasajeros = total_pasajeros / total_vuelos if total_vuelos > 0 else 0

print(f'\nTotal de pasajeros: {total_pasajeros}')
print(f'Promedio de pasajeros por vuelo: {promedio_pasajeros:.2f}')

# Tarifas
total_tarifas = sum(v['tarifa'] for v in vuelos)
promedio_tarifa = total_tarifas / total_vuelos if total_vuelos > 0 else 0

print(f'\nTotal de tarifas: {total_tarifas:.2f}')
print(f'Tarifa promedio: {promedio_tarifa:.2f}')

# Más caro y más barato
if total_vuelos > 0:
    vuelo_caro = max(vuelos, key=lambda v: v['tarifa'])
    vuelo_barato = min(vuelos, key=lambda v: v['tarifa'])

    print(f'\nVuelo más caro: {vuelo_caro['numero_vuelo']} - ${vuelo_caro['tarifa']:.2f}')
    print(f'Vuelo más barato: {vuelo_barato['numero_vuelo']} - ${vuelo_barato['tarifa']:.2f}')
else:
    print('\nNo hay datos registrados.')