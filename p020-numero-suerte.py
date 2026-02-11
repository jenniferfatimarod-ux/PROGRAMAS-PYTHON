#p020-numero-suerte.py

#Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos. A partir
#de este dato, el programa debe:
#• Mostrar cada uno de los dígitos individuales del año. Por ejemplo, si el año es 1995, debe mostrar "1", "9",
#"9", "5".
#• Calcular y mostrar la suma de los dígitos individuales del año. Siguiendo el ejemplo anterior, la suma sería
#1 + 9 + 9 + 5 = 24.


print("\033[H\033[J")
print('CALCULANDO TU NÚMERO DE LA SUERTE\n')

naci = int(input('Introduce tu año de nacimiento: '))

num1 = naci // 1000 #numero 1
num2 = (naci % 1000) // 100 #numero 2
num3 = (naci % 100) //10 #numero 3
num4 = (naci % 10) #numero 4

numsu = num1 + num2 + num3 + num4

print(num1, num2, num3, num4)
print(f'Tu número de la suerte es: {numsu}')