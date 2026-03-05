"""
Objetivo: Realizar un programa que administre las ventas de un cine
Nombre del Alumno: Jennifer Fátima Rodríguez Dávila
Matrícula: 36174322
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adultos = 0
total_tercera = 0
total_academicos = 0

total_hombres = 0
total_mujeres = 0

total_asistentes = 0
total_rechazados = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos = 0
ingresos_tercera = 0
ingresos_academicos = 0

ingresos_totales = 0.0

# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERA_EDAD = 60.0
PRECIO_ACADEMICO = 70.0

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":

    print("\n--- Nueva Venta ---")
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero!
    
    edad = int(input("Introduce la edad del comprador: "))
    

    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    if edad > 13:
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        tipo = input("Introduce el tipo de comprador(Estudiante, Adulto, Tercera Edad o Académico): ").lower()
        sexo = input("Introduce el sexo comprador (Hombre/Mujer): ").lower()
        print(f"¡Bienvenido(a)! Venta registrada: Edad: {edad}, Sexo: {sexo} Tipo: {tipo}")
        
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        total_asistentes += 1
        suma_edades += edad
        # Incrementa el contador de sexo correspondiente (hombre o mujer).
        if sexo == "hombre":
            total_hombres += 1
        elif sexo == "mujer":
            total_mujeres += 1
        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        # Suma el costo del boleto a los ingresos totales.
        if tipo == "estudiante":
            total_estudiantes += 1
            ingresos_estudiantes += PRECIO_ESTUDIANTE
        elif tipo == "adulto":
            total_adultos += 1
            ingresos_adultos += PRECIO_ADULTO
        elif tipo == "tercera edad":
            total_tercera += 1
            ingresos_tercera += PRECIO_TERCERA_EDAD
        elif tipo == "academico":
            total_academicos += 1
            ingresos_academicos += PRECIO_ACADEMICO
        
    else:
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()
        print("ACCESO DENEGADO: El comprador es menor de 13 años.")
        # ... (incrementa el contador de personas rechazadas)
        total_rechazados += 1

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0
if total_asistentes > 0:
    promedio_edad = suma_edades / total_asistentes # (calcula el promedio aquí)
else:
    promedio_edad = 0

ingresos_totales = ingresos_estudiantes + ingresos_adultos + ingresos_tercera + ingresos_academicos
# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
# Imprime todos los totales de asistentes por tipo y sexo.
print(f"Total de Estudiantes: {total_estudiantes}")
print(f"Total de Adultos: {total_adultos}")
print(f"Total de Tercera Edad: {total_tercera}")
print(f"Total de Académicos: {total_academicos}")
print("-------------------------------")
print(f"Total de Hombres: {total_hombres}")
print(f"Total de Mujeres: {total_mujeres}")
print("-------------------------------")
print(f"Total de Asistentes: {total_asistentes}")
print(f"Promedio de edad de asistentes: {promedio_edad:.2f} años")
print(f"Personas rechazadas por edad: {total_rechazados}")

print("\n--- Reporte de Ingresos ---")
# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.
print(f"Ingresos por Estudiantes: ${ingresos_estudiantes:.2f}")
print(f"Ingresos por Adultos: ${ingresos_adultos:.2f}")
print(f"Ingresos por Tercera Edad: ${ingresos_tercera:.2f}")
print(f"Ingresos por Académicos: ${ingresos_academicos:.2f}")
print("-------------------------------")
print(f"TOTAL RECAUDADO: ${ingresos_totales:.2f}")

print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
if ingresos_totales < 1500:
    print("La función generó BAJAS ganancias.")
elif 1500 <= ingresos_totales <= 3500:
    print("La función generó ganancias MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")

"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

R: preguntaría que día de la semana es, si responde martes haría el descuento, en los demás días de la 
semana no haría descuento, utilizando un if y else.
 Lo agregaría en la parte que pregunta por su tipo de comprador y sexo.

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

R: Depende si pusiste el acumudador "total_ingresos" dentro del if, elif porque al principio lo puse ahí y no funcionaba 
correctamente, es mejor ponerlo al final, antes de realizar el reporte final, y así suma los ingresos totales correspondientes a cada tipo de comprador.

"""