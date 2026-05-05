#p157-empleado2.py
#Modelamos un empleado
print('\033[H\033[J')

#Código de clase
class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo 
        self.casado = casado

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {'Mujer' if self.sexo=='M' else 'Hombre'}, Casado: {'Casado' if self.casado else 'No casado'}'
   

#Programa principal
empleado1 = Empleado('Juan Díaz', 35, 'H', True)
print(f'Nombre: {empleado1.nombre}')
print(f'Edad: {empleado1.edad}')
print(f'Sexo: {empleado1.sexo}')
print(f'Casado: {empleado1.casado}')
print(empleado1)

emp2 = Empleado('Rocio Espinoza',15,'M',False)
print('Nombre: ', emp2.nombre)
print('Edad : ', emp2.edad)
print('Sexo : ', emp2.sexo)
print('Casado: ', emp2.casado)
print(emp2)

emp3 = Empleado('Rebeca Soto',22,'M',True)
print('Nombre: ', emp3.nombre)
print('Edad : ', emp3.edad)
print('Sexo : ', emp3.sexo)
print('Casado: ', emp3.casado)
print(emp3)

pedad = ( empleado1.edad + emp2.edad + emp3.edad) / 3
print(f'El promedio de la edad de los empleados es {pedad}')