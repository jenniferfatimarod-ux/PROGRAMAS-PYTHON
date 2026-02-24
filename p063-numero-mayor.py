#p063-numero-mayor.py
#Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, el programa deberá mostrar cuál fue el
#número más grande de todos los introducidos.
#Ejemplo de ejecución:
#Introduce números (0 para terminar):
#> 25
#> 101
#> 49
#> 88
#> 0
#--------------------
#El número mayor fue: 101
#¿Desea continuar (S/N)? N

print("\033[2J\033[H")
print("--Leer una serie de números hasta que el usuario ingrese un 0--\n")

respuesta = "S"

while respuesta.upper() == "S":

    print("Introduce números (0 para terminar):")

    maximo = None  # Para guardar el número mayor
    while True:
        num = int(input("> "))
        
        if num == 0:
            break
        
        if maximo is None or num > maximo:
            maximo = num

    if maximo is not None:
        print(f"El número mayor fue: {maximo}")
    else:
        print("No se introdujeron números.")

    respuesta = input("¿Desea continuar (S/N)? ")

print("\nPrograma terminado.")