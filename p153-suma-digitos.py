#p153-suma-digitos.py
#Escribe un programa que procese una lista de números. Debes implementar lo siguiente:
#1. Una función que lea y devuelva una lista de números enteros (puedes reusar la hecha en clase).
#2. Una función que reciba un número entero y devuelva la suma de sus dígitos individuales (ej: 1971 ->
#1+9+7+1 = 18).
#3. Una función principal que reciba la lista de números. Esta debe usar la función anterior para crear y
#devolver una nueva lista que contenga la suma de los dígitos de cada número original.
#El programa debe imprimir la lista original y la nueva lista con las sumas.

print('\033[H\033[J')

def leer_lista():
    entrada = input('Dame los números (separados por espacio): ')
    numeros = entrada.split()
    lista = []
    
    for n in numeros:
        lista.append(int(n))
    
    return lista


def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma


def procesar_lista(lista):
    nueva_lista = []
    
    for num in lista:
        nueva_lista.append(suma_digitos(num))
    
    return nueva_lista


# Programa principal
lista_original = leer_lista()
lista_sumas = procesar_lista(lista_original)

print('La lista de números original :', lista_original)
print('La lista con las suma de dígitos de los números:', lista_sumas)