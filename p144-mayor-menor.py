#p144-mayor-menor.py
#Leer datos y calcular el mayo y el menor usando funciones

from typing import List

print('\033[H\033[J')

def captura () -> List [float]:
    datos = []
    while True:
        entrada = input ('Numero: ')
        if entrada.lower() == 'fin':break
        try:
            numero = float (entrada)
            datos.append(numero)
        except:
            print('Error')
    return datos

def mayor (lista: List[float]) -> float:
    m = lista[0]
    for n in lista:
        if n>m :
            m = n
    return m

def menor (lista: List[float]) -> float:
    m = lista[0]
    for n in lista:
        if n<m :
            m = n
    return m

numeros = captura()

print(numeros)
print(f'El mayor es: {mayor(numeros)}')
print(f'El menor es: {menor(numeros)}')