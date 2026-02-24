#p058-impares-ascendente.py
#Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.
#Ejemplo de ejecución:
#Introduce un número límite: 9
#Números impares: 1, 3, 5, 7, 9
#La suma de los impares es: 25
#¿Desea continuar (S/N)? N

print("\033[2J\033[H")
respuesta = "S"

while respuesta.upper() == "S":

    print("--Imprimiendo números impares de manera ascendente--\n")

    n = int(input('Introduce un número límite: '))
    z = 1
    suma = 0

    while z <= n:
        print(z, end=' ')
        suma += z
        z += 2

    print(f'\nCiclo terminado. La suma es: {suma}')

    respuesta = input("\n¿Desea continuar (S/N)? ")

print("\nPrograma terminado.")