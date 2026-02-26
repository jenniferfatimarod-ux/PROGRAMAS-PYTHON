"""
Programa: p065-repaso-primer-parcial.py
Objetivo: Calcular y registrar las ventas de una papelería
Autor: Carlos Castañeda
Fecha: Jueves 26 de febrero de 2026
"""
print("\033[2J\033[H")
print("---------------------------\n")
print("Papelería La Malena, SA de CV.\n")
print("Sistema de ventas de copias\n")
print("---------------------------\n")

ventas = subtotal  = 0
c_c = c_o = c_d = c_p = 0
t_c = t_o = t_d = t_p = 0

while True:
    ventas = 1
    print(f'Venta {ventas}')
    tipo = input ('Tipo de copia (C)carta $3, (O)oficio $4, (D)doble Of $6, (P)plano $12: ').upper()

    if tipo not in "CODP":
        print('Error: Tipo de copia no valido. Intenta de nuevo')
        ventas -= 1
        continue

    c = int(input('Cantidad?: '))

    if tipo == 'C':
        c_c += c
        t_c += c * 3

    elif tipo == 'O':
        c_o += c
        t_o += c * 4

    elif tipo == 'D':
        c_d += c
        t_d += c * 6

    elif tipo == 'P':
        c_p += c
        t_p += c * 12

    if input('Otra venta (S/N)?').upper() != 'S': break
total_c = c_c + c_d + c_o + c_p
total_d = t_c + t_d + t_o + t_p

if total_c >= 50:
    total_d *= 0.9

print('---------------------------------------------')
print('Resumen diario de ventas')
print('---------------------------------------------')
print(f'Ventas realizadas: {ventas}')
print('---------------------------------------------')
print(f'Carta\t\t: {c_c:2d} - ${t_c:8.2f}')
print(f'Oficio\t\t: {c_o:2d} - ${t_o:8.2f}')
print(f'Doble oficio\t\t: {c_d:2d} - ${t_d:8.2f}')
print(f'Plano\t\t: {c_p:2d} - ${t_p:8.2f}')
print(f'Total ventas\t: {total_c:2d} - ${total_d:8.2f}')

mensaje = ""
if total_d >150:
    mensaje = "Venta superada"
elif total_d >=50:
    mensaje = "Venta frecuente"
else:
    mensaje = "Venta moderada"
print(f'Esta venta es una: {mensaje}')