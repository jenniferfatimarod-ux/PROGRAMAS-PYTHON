#p062-conversion-temperaturas.py
#El usuario debe introducir una temperatura inicial y una final en grados Celsius. El programa mostrará la conversión
#a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.
#Ejemplo de ejecución:
#Introduce la temperatura inicial en °C: 5
#Introduce la temperatura final en °C: 8
#--------------------
#5°C = 41.0°F
#6°C = 42.8°F
#7°C = 44.6°F
#8°C = 46.4°F
#¿Desea continuar (S/N)? N

print("\033[2J\033[H")
print("--Conversión de Celsius a Fahrenheit--\n")

respuesta = "S"

while respuesta.upper() == "S":

    inicio = int(input("Introduce la temperatura inicial en °C: "))
    final = int(input("Introduce la temperatura final en °C: "))

    c = inicio
    while c <= final:
        f = (c * 9/5) + 32
        print(f"{c}°C = {f:.1f}°F")
        c += 1

    respuesta = input("¿Desea continuar (S/N)? ")

print("\nPrograma terminado.")