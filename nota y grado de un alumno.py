"""
Ejercicio resuelto a:
	Programa en python que calcula el promedio de 5 calificaciones 
	de un alumno. Al usuario debe solicitarle: nombre completo, 
	grado, grupo, nombre de las materias y la calificación de cada una.
@author parzibyte
"""

# Definir una constante
# https://parzibyte.me/blog/2019/01/16/constantes-python/
MATERIAS = 1

# Pedir datos del alumno
# https://parzibyte.me/blog/2018/10/17/leer-imprimir-datos-python-input-print/
nombre = input("Nombre completo: ")
grado = input("Grado: ")
grupo = input("Grupo: ")

# Hacer un ciclo, pedir datos y sumar la calificación
contador = 1
sumatoria = 0
while contador <= MATERIAS:
    nombre_materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(nombre_materia)))
    # Sumar la calificación a la sumatoria
    sumatoria = sumatoria + calificacion
    # Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1

# Hacer cálculos e imprimir resultados
promedio = sumatoria / MATERIAS
print("""***** Resultados *****
Alumno: {} | {} {}
*******************************
* Promedio: {}
*******************************
""".format(nombre, grupo, grado, promedio))