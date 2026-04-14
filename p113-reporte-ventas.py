#p113-reporte-ventas.py
#Crear una lista de diccionarios simulando un reporte de ventas

print('\033[H\033[J')

compras = []

print('\nRegistro de Transacciones')
n = int(input('Cuantas compras? '))

for i in range(1, n+1):
    print(f'\nCompra {i}')
    compra = {
        'cliente' : input('Cliente: '),
        'Producto' : input('Producto:'),
        'Cantidad' : int(input('Cantidad: ')),
        'Precio' : float(input('Precio: '))
    }
    compras.append(compra)
print(f'\nLista de compras registradas: {compras}')

clientes = {}
for compra in compras:
    cliente = compra['cliente']
    if cliente not in clientes:
        clientes[cliente] = {'Cantidad':0, 'subtotal': 0}
    clientes[cliente]['Cantidad']+=compra['Cantidad']
    clientes[cliente]['subtotal']+=compra['Cantidad']*compra['Precio']

print('\nReporte Total por cliente')
for cliente,datos in clientes.items():
    print('Cliente', cliente)
    print('Total productos:', datos['Cantidad'])
    print('Total a pagar:', datos['subtotal'])

print('\nDiccionario consolidado', clientes)