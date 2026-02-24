#p059-pares-descendente.py
#Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.
#Ejemplo de ejecución:
#Introduce un número límite (menor a 100): 92
#Números pares: 100, 98, 96, 94, 92
#La suma de los pares es: 480
#¿Desea continuar (S/N)? N

print("\033[2J\033[H")
respuesta = "S"

while respuesta.upper() == "S":

    print("--Imprimiendo números pares de manera descendente de 100 a n--\n")

    n = int(input('Introduce un número límite (menor a 100): '))
    z = 100
    suma = 0

    while z >= n:
        print(z, end=' ')
        suma += z
        z -= 2

    print(f'\nCiclo terminado. La suma es: {suma}')

    respuesta = input("\n¿Desea continuar (S/N)? ")

print("\nPrograma terminado.")