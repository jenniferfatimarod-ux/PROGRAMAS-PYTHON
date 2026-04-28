#p142-suma-lista.py
#Funcion que recibe una lista de numeros y regresa

from typing import List

print('\033[H\033[J')

def suma_lista(lista : List[float]) -> float:
    suma = 0
    for numero in lista:
        suma+= numero
    return suma

#lista1
lista = [1.5,2.3,3.7,4.0]
resultado = suma_lista(lista)
print('Suma 1:', resultado)

#lista2}print()
print('Suma 2:')