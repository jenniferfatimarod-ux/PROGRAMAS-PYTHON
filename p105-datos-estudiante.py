#p105-datos-estudiante.py
#Gestionar los datos de un estudiante usando un diccionario

print('\033[H\033[J')
print('Gestión de estudiantes')

estudiante = {'nombre':'Juan Perez', 
              'edad':'45',
              'emial':'jperez@msn.com',
              'carrera':'Ing.Sistemas'}

print(f'Diccionario: {estudiante} - {len(estudiante)}')

estudiante['calificación'] = 9.5
estudiante['email'] = 'juanp@gmail.com'

print(f'Diccionario: {estudiante} - {len(estudiante)}')

print('\nLas llaves:')
for k in estudiante.keys(): print(k,end=' ')

print('\nLos valores:')
for v in estudiante.values(): print (v,end=' ')

print('\n\nllaves y valores:')
for k, v in estudiante.items(): print(f'{k:<10} : {v}')