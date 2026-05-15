#p161-control-libros.py
# Sistema de Control de Préstamos de Libros

print('\033[H\033[J')

# --------------------------------------------
# Clase Prestamo
# --------------------------------------------
class Prestamo:

    def __init__(self, libro, dias, tarifa_diaria):
        self.libro = libro
        self.dias = dias
        self.tarifa_diaria = tarifa_diaria
        self.total = dias * tarifa_diaria

    def __str__(self):
        return (f"-> Libro: {self.libro} "
                f"Días: {self.dias} "
                f"Tarifa/Día: $ {self.tarifa_diaria:.2f} "
                f"Total: $ {self.total:.2f}")


# --------------------------------------------
# Clase Usuario
# --------------------------------------------
class Usuario:

    def __init__(self, id_usuario, nombre, correo, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.prestamos = list()

    def agregarPrestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def totalTarifas(self):
        total = 0
        for prestamo in self.prestamos:
            total += prestamo.total
        return total

    def __str__(self):
        return (f"Usuario -> [Nombre: {self.nombre} "
                f"ID: {self.id_usuario} "
                f"Correo: {self.correo} "
                f"Tel: {self.telefono}]")

# --------------------------------------------
# Clase Biblioteca
# --------------------------------------------
class Biblioteca:

    def __init__(self, nombre, domicilio, encargado):
        self.nombre = nombre
        self.domicilio = domicilio
        self.encargado = encargado
        self.usuarios = list()

    def agregarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def totalPrestamos(self):
        total = 0
        for usuario in self.usuarios:
            total += len(usuario.prestamos)
        return total

    def totalImportePrestamos(self):
        total = 0
        for usuario in self.usuarios:
            total += usuario.totalTarifas()
        return total

    def __str__(self):
        return (f"[Nombre: {self.nombre} "
                f"Domicilio: {self.domicilio} "
                f"Encargado: {self.encargado}]")

# --------------------------------------------
# Función principal
# --------------------------------------------
def main():

    # Crear biblioteca
    biblioteca = Biblioteca(
        "Biblioteca Mauricio Magdaleno",
        "Calle Grillo 100, Col. Centro",
        "Dra. Leticia Ramírez"
    )

    # Crear usuarios
    u1 = Usuario("USR-2026-X", "Salvador Novo",
                 "snovo@cultura.gob.mx", "4921112233")

    u2 = Usuario("USR-2026-Y", "Amparo Dávila",
                 "amparo@unam.mx", "4922223344")

    u3 = Usuario("USR-2026-Z", "Juan Rulfo",
                 "jrulfo@literatura.mx", "4923334455")

    u4 = Usuario("USR-2026-W", "Elena Garro",
                 "egarro@escritores.org", "4924445566")

    # Agregar préstamos a usuarios
    u1.agregarPrestamo(Prestamo("Laberinto de la Soledad", 6, 11.50))
    u1.agregarPrestamo(Prestamo("Pedro Páramo", 4, 14.00))

    u2.agregarPrestamo(Prestamo("Balún Canán", 8, 9.50))
    u2.agregarPrestamo(Prestamo("Oficio de Tinieblas", 5, 12.00))
    u2.agregarPrestamo(Prestamo("Árbol de Literatura", 3, 18.00))

    u3.agregarPrestamo(Prestamo("El Llano en Llamas", 10, 7.50))

    # Agregar usuarios a biblioteca
    biblioteca.agregarUsuario(u1)
    biblioteca.agregarUsuario(u2)
    biblioteca.agregarUsuario(u3)
    biblioteca.agregarUsuario(u4)

    # ----------------------------------------
    # Reporte
    # ----------------------------------------

    print("=" * 90)
    print("REPORTE DE CONTROL DE PRÉSTAMOS:")
    print(f"Biblioteca -> {biblioteca}")
    print("=" * 90)

    print(f"Total de usuarios registrados : {len(biblioteca.usuarios)}")
    print(f"Total de préstamos activos : {biblioteca.totalPrestamos()}")

    print("-" * 90)
    print("--- Catálogo de Usuarios Registrados ---")

    for usuario in biblioteca.usuarios:
        print(usuario)

    print("\n--- Detalle de Préstamos por Lector ---")

    for usuario in biblioteca.usuarios:

        print(f"{usuario.id_usuario} - {usuario.nombre} | "
              f"Costo Acumulado del Lector: "
              f"${usuario.totalTarifas():.2f}")

        for prestamo in usuario.prestamos:
            print(prestamo)

    print("=" * 90)
    print("IMPORTACIÓN TOTAL RECAUDADA POR LA BIBLIOTECA: "
          f"${biblioteca.totalImportePrestamos():.2f}")
    print("=" * 90)


# --------------------------------------------
# Inicio del programa
# --------------------------------------------
if __name__ == "__main__":
    main()