#p064-verificar-palindromo.py
#Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. Un número es palíndromo si se
#lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).
#Ejemplo de ejecución:
#Introduce un número para verificar si es palíndromo: 121
#El número 121 es un palíndromo.
#¿Desea continuar (S/N)? S
#Introduce un número para verificar si es palíndromo: 123
#El número 123 no es un palíndromo.
#¿Desea continuar (S/N)? N

print("\033[2J\033[H")
print("--Verificar si un número es palíndromo--\n")

respuesta = "S"

while respuesta.upper() == "S":

    num = input("Introduce un número para verificar si es palíndromo: ")

    if num == num[::-1]: #num[::-1] voltea el número
        print(f"El número {num} es un palíndromo.")
    else:
        print(f"El número {num} no es un palíndromo.")

    respuesta = input("¿Desea continuar (S/N)? ")

print("\nPrograma terminado.")