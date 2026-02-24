#p060-promedio-suma.py
#Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, mostrar el conteo total de números, la
#suma y el promedio de la serie.
#Ejemplo de ejecución:
#Introduce números (0 para terminar):
#> 10
#> 5
#> 15
#> 0
#--------------------
#Se introdujeron 3 números.
#La suma es: 30
#El promedio es: 10.0
#¿Desea continuar (S/N)? N

print("\033[2J\033[H")
print("--Leer números introducidos por el usuario hasta que ingrese un 0--\n")
respuesta = "S"

while respuesta.upper() == "S":

    print('Introduce números (0 para terminar): ')
    z = 1
    num = 0
    suma = 0

    while True:
        z = int(input('> '))
        
        if z == 0:
            break
        
        suma += z
        num += 1

    if num > 0:
        p = suma / num
    else:
        p = 0

    print(f'\nCiclo terminado.')
    print(f'Se introdujeron {num} números.')
    print(f'La suma es: {suma}.')
    print(f'El promedio es: {p}')

    respuesta = input("\n¿Desea continuar (S/N)? ")

print("\nPrograma terminado.")