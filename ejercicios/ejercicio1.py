# Ejercicio 1: Variables y Datos Primitivos en Python

# Ingresar las notas de los estudiantes
nota_joel_1 = float(input("Ingrese la nota 1 de Joel: "))
nota_joel_2 = float(input("Ingrese la nota 2 de Joel: "))
nota_joel_3 = float(input("Ingrese la nota 3 de Joel: "))

nota_alondra_1 = float(input("Ingrese la nota 1 de Alondra: "))
nota_alondra_2 = float(input("Ingrese la nota 2 de Alondra: "))
nota_alondra_3 = float(input("Ingrese la nota 3 de Alondra: "))

nota_paz_1 = float(input("Ingrese la nota 1 de Paz: "))
nota_paz_2 = float(input("Ingrese la nota 2 de Paz: "))
nota_paz_3 = float(input("Ingrese la nota 3 de Paz: "))

# Calcular promedio de cada estudiante
promedio_joel = round((nota_joel_1 + nota_joel_2 + nota_joel_3) / 3, 3)
promedio_alondra = round((nota_alondra_1 + nota_alondra_2 + nota_alondra_3) / 3, 3)
promedio_paz = round((nota_paz_1 + nota_paz_2 + nota_paz_3) / 3, 3)

# Mostrar promedio de cada estudiante
print("\nPromedio de cada estudiante:")
print("Joel:", promedio_joel)
print("Alondra:", promedio_alondra)
print("Paz:", promedio_paz)

# Calcular nota mínima de cada estudiante
nota_minima_joel = min(nota_joel_1, nota_joel_2, nota_joel_3)
nota_minima_alondra = min(nota_alondra_1, nota_alondra_2, nota_alondra_3)
nota_minima_paz = min(nota_paz_1, nota_paz_2, nota_paz_3)

# Mostrar nota mínima de cada estudiante
print("\nNota mínima de cada estudiante:")
print("Joel:", nota_minima_joel)
print("Alondra:", nota_minima_alondra)
print("Paz:", nota_minima_paz)

# Calcular promedio final de todos los estudiantes
promedio_final = round((promedio_joel + promedio_alondra + promedio_paz) / 3, 3)

# Mostrar promedio final de todos los estudiantes
print("\nPromedio final de todos los estudiantes:", promedio_final)
