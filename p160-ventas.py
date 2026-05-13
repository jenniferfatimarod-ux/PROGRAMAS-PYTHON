#p160-ventas.py
#Simular un sistema de control de ventas

print('\033[H\033[J')

class venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = self.cantidad * self.precio

    def __str__(self):
        return f'Articulo: {self.articulo:<15} Cantidad:{self.cantidad:>10.2f} Precio:{self.precio:>10.2f} Total:{self.total:>10,.2f}'


class cliente:
    def __init__(self, rfc, nombre, domicilio, correo):
        self.rfc = rfc
        self.nombre = nombre
        self.domicilio = domicilio
        self.correo = correo
        self.ventas = list()

    def agregarventa(self, venta):
        self.ventas.append(venta)

    def totalventas(self):
        total = 0
        for v in self.ventas:
            total += v.total
        return total

    def __str__(self):
        return f'Cliente [Nombre:{self.nombre:<20} RFC: {self.rfc:<12} Domicilio: {self.domicilio:<20} Correo: {self.correo:<20}]'


class tienda:
    def __init__(self, nombre, domicilio, propietario):
        self.nombre = nombre
        self.domicilio = domicilio
        self.propietario = propietario
        self.clientes = list()

    def agregarcliente(self, cliente):
        self.clientes.append(cliente)

    def totalgeneral(self):
        total = 0
        for c in self.clientes:
            total += c.totalventas()
        return total

    def __str__(self):
        return f'Nombre: {self.nombre} Domicilio: {self.domicilio} Propietario: {self.propietario}'


def main():

    # Todo
    mitienda = tienda(
        nombre='Ferretaria las Lomas',
        domicilio='Av Luis Moya 345',
        propietario='Carlos Castaneda'
    )

    # Agregar Clientes a la tienda
    mitienda.agregarcliente(
        cliente(
            rfc='JELI120240',
            nombre='Felipe Calderon',
            domicilio='Las Lomas 123',
            correo='calde@msn.com'
        )
    )

    mitienda.agregarcliente(
        cliente(
            rfc='PEÑA121250',
            nombre='Enrique Peña',
            domicilio='5 de Mayo 321',
            correo='quique@gmail.com'
        )
    )

    mitienda.agregarcliente(
        cliente(
            rfc='AMLO101145',
            nombre='Andres Lopez',
            domicilio='Palacio Nacional 321',
            correo='peje@yahoo.com'
        )
    )

    mitienda.agregarcliente(
        cliente(
            rfc='GELA666666',
            nombre='Xochitl Gelatinas',
            domicilio='Danone 123',
            correo='xochitl@precidencia.gob.mx'
        )
    )

    # Agregar Ventas a los clientes
    mitienda.clientes[0].agregarventa(
        venta(articulo='Martillo', cantidad=10, precio=60.5)
    )

    mitienda.clientes[0].agregarventa(
        venta(articulo='Pala', cantidad=2, precio=1170.55)
    )

    mitienda.clientes[1].agregarventa(
        venta(articulo='Clavo', cantidad=2.5, precio=160.34)
    )

    mitienda.clientes[1].agregarventa(
        venta(articulo='Cinta de Aislar', cantidad=5, precio=71.34)
    )

    mitienda.clientes[1].agregarventa(
        venta(articulo='Pinzas', cantidad=10, precio=650.33)
    )

    mitienda.clientes[2].agregarventa(
        venta(articulo='Thiner', cantidad=50, precio=65.00)
    )

    print(f'\nREPORTE DE VENTAS: {mitienda}\n')

    print('\nCLIENTES:')
    for c in mitienda.clientes:
        print(c)

    print('\nVENTAS DE CADA CLIENTE: ')
    for c in mitienda.clientes:
        print(f'\n{c.rfc} - {c.nombre} - {c.totalventas():,.2f}')

        for v in c.ventas:
            print(f'{v}')

    print('TOTAL DE VENTAS GENERAL: ')
    print(f'{mitienda.totalgeneral():,.2f}')


if __name__ == '__main__':
    main()
    
# # Programa principal
# v1 = venta('Martillo',10,100)
# v2 = venta('Pala', 5, 300)
# v3 = venta('Flexometro', 2, 400)

# c1 = cliente('CARC71156', 'Carlos', 'Av. México', 'castro@hotmail.com')
# c1.agregarventa(v1)
# c1.agregarventa(v2)
# c1.agregarventa(v3)
# print(c1)
# print(c1.ventas[0])
# print(c1.ventas[1])
# print(c1.ventas[2])
# print(c1.totalventas())