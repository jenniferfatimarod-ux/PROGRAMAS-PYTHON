#p034-tipo-angulo.py
#muestra el tipo de angulo en base a su medidad o su magnitud

print("\033[2J\033[H")
print("--Clasificador de angulos--\n")

angulo = int(input('Dame un angulo en grados: '))

if angulo >= 0 and angulo <=360:
    if angulo < 90:
       print('AGUDO')
    elif angulo == 90:
       print('RECTO')
    elif angulo < 180:
        print('OBTUSO')
    elif angulo == 180:
        print('LLANO')
    elif angulo < 360:
        print('CONCAVO')
    else:
        print('COMPLETO')
else:
    print(f'Angulo fuera de rango')

print('programa terminado')