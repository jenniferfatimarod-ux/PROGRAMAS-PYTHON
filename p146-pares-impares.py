#p146-pares-impares.py
#funcion que regresa pares e impares

from typing import List, Tuple

print('\033[H\033[J')

def pares_impares (numeros: List[int]) -> Tuple[List[int], List[int]]:
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
pares, impares = pares_impares(numeros)
print (pares)
print(impares)