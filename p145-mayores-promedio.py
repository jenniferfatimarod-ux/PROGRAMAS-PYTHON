#p145-mayores-promedio.py
#funcion que calcula el promedio de una lista y los mayores al promedio

from typing import List

print('\033[H\033[J')

def promedio_lista(numeros: List[float]) -> float:
    suma = 0
    if not numeros: return 0.0
    for numero in numeros:
        suma+=numero
    return suma/len(numeros)

def mayores_promedio(numeros: List[float], prom:float) -> List[float]:
    mayores = []
    for numero in numeros:
        if numero > prom:
            mayores.append(numero)
    return mayores

numeros = [1.5,2.3,3.7,4.0,5.5]
promedio = promedio_lista(numeros)
print(promedio)
mayores = mayores_promedio(numeros, promedio)
print(mayores)