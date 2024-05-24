print("Ingrese las notas de Joel: ")
n1_joel = float(input("Nota N°1: "))
n2_joel = float(input("Nota N°2: "))
n3_joel = float(input("Nota N°3: "))

print("\nIngrese las notas de Alondra:")
n1_alondra = float(input("Nota 1: "))
n2_alondra = float(input("Nota 2: "))
n3_alondra = float(input("Nota 3: "))

print("\nIngrese las notas de Paz:")
n1_paz = float(input("Nota 1: "))
n2_paz = float(input("Nota 2: "))
n3_paz = float(input("Nota 3: "))

#Promedio de cada estudiante
prom_joel = round((n1_joel + n2_joel + n3_joel)/3, 3)
prom_alondra = round((n1_alondra + n2_alondra + n3_alondra)/3, 3)
prom_paz = round((n1_paz + n2_paz + n3_paz)/3, 3)

#Nota mínima de cada estudiante
min_joel = min(n1_joel, n2_joel, n3_joel)
min_alondra = min(n1_alondra, n2_alondra, n3_alondra)
min_paz = min(n1_paz, n2_paz, n3_paz)

#Promedio final de todos los estudiantes
prom_final = round((prom_joel + prom_alondra + prom_paz) / 3, 3)

print(f"\nPromedio de Joel: {prom_joel}")
print(f"Nota mínima de Joel: {min_joel}")
print(f"\nPromedio de Alondra: {prom_alondra}")
print(f"Nota mínima de Alondra: {min_alondra}")
print(f"\nPromedio de Paz: {prom_paz}")
print(f"Nota mínima de Paz: {min_paz}")
print(f"\nPromedio final de todos los estudiantes: {prom_final}")
