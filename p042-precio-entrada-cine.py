#p042-precio-entrada-cine.py
#Problema: Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del
#cliente. El programa debe solicitar la edad y mostrar el precio correspondiente, siguiendo estas reglas:
#• Menores de 5 años: Entran gratis.
#• Niños (5 a 12 años): Pagan $5.
#• Adultos (13 a 64 años): Pagan $10.
#• Tercera edad (65 años o más): Pagan $7.
#Ejemplos de ejecución:
#• Entrada: Edad: 4
#• Salida: Tu entrada es gratis.
#• Entrada: Edad: 10
#• Salida: El precio de tu entrada es de $5.
#• Entrada: Edad: 35
#• Salida: El precio de tu entrada es de $10.

print("\033[2J\033[H")
print('Bienvenido a la taquilla del cine')
print('Menores de 5 años: Entran gratis.')
print('Niños (5 a 12 años): Pagan $5.')
print('Adultos (13 a 64 años): Pagan $10.')
print('Tercera edad (65 años o más): Pagan $7.')
e = int(input('Edad: '))

if e<5:
  print(f'Tu edad es {e}, entras gratis.')
elif e>=5 and e<=12:
  print(f'Tu edad es {e}, el precio de tu entrada es de $5.')
elif e>=13 and e<=64:
  print(f'Tu edad es {e}, el precio de tu entrada es de $10.')
elif e>=65:
  print(f'Tu edad es {e}, el precio de tu entrada es de $7.')
else:
  print('Opción incorrecta')

print('\nPrograma terminado.')