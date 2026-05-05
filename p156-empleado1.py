#p156-empleado1.py
#Modelamos un empleado usando una clase

print('\033[H\033[J')

#Código de clase
class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    

#Programa principal

#Instanciamos la clase
empleado1 = Empleado('José Díaz', 35)
print('Nombre:', empleado1.nombre)
print('Edad:', empleado1.edad)
print(empleado1)