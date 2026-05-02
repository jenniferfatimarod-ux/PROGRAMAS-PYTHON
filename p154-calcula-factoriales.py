#p154-calcula-factoriales.py
#Desarrolla un programa que calcule el factorial de cada número en una lista. Debes implementar:
#1. Una función que lea y devuelva una lista de números enteros.
#2. Una función que reciba un número entero y devuelva su factorial (ej: 5 -> 120).
#3. Una función principal que reciba la lista de números. Esta debe usar la función factorial para crear y
#devolver una nueva lista con los factoriales de cada número.
#El programa debe imprimir la lista original y la lista de factoriales.

print('\033[H\033[J')

def leer_lista():
    entrada = input('Dame los números (separados por espacio): ')
    numeros = entrada.split()
    lista = []
    
    for n in numeros:
        lista.append(int(n))
    
    return lista


def factorial(numero):
    resultado = 1
    
    for i in range(1, numero + 1):
        resultado *= i
    
    return resultado


def procesar_lista(lista):
    nueva_lista = []
    
    for num in lista:
        nueva_lista.append(factorial(num))
    
    return nueva_lista


# Programa principal
lista_original = leer_lista()
lista_factoriales = procesar_lista(lista_original)

print('La lista de números originales:', lista_original)
print('La lista con los factoriales:', lista_factoriales)
