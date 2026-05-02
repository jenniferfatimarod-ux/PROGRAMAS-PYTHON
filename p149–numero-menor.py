#p149–numero-menor.py
#Crea un programa que incluya una función. Dicha función debe solicitar 3 números enteros al usuario y devolver el menor.

print('\033[H\033[J')

def obtener_menor():
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    n3 = int(input("Introduce el tercer número: "))
    
    menor = min(n1, n2, n3)
    return menor

# Programa principal
resultado = obtener_menor()
print("El número menor es:", resultado)