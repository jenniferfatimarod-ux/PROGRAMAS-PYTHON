#p061-suma-200.py
#Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, mostrar cuántos
#números se introdujeron y la suma final.
#Ejemplo de ejecución:
#Suma actual: 0. Introduce un número: 70
#Suma actual: 70. Introduce un número: 80
#Suma actual: 150. Introduce un número: 55
#--------------------
#Meta de 200 alcanzada.
#Suma final: 205
#Total de números introducidos: 3
#¿Desea continuar (S/N)? N

print("\033[2J\033[H")
print("--Sumar números hasta alcanzar 200 o más--\n")

respuesta = "S"

while respuesta.upper() == "S":

    suma = 0
    contador = 0

    while suma < 200:
        num = int(input(f"Suma actual: {suma}. Introduce un número: "))
        suma += num
        contador += 1

    print("Meta de 200 alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de números introducidos: {contador}")

    respuesta = input("¿Desea continuar (S/N)? ")

print("\nPrograma terminado.")