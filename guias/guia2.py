# A) Ingresar las fechas de vencimiento (día, mes, año) de tres productos por consola, y almacenarlas en tuplas.
d1 = int(input("Ingrese el día de vencimiento del 1° producto: "))
m1 = int(input("Ingrese el mes de vencimiento del 1° producto: "))
a1 = int(input("Ingrese el año de vencimiento del 1° producto: "))
fecha1 = (d1, m1, a1)

d2 = int(input("\nIngrese el día de vencimiento del 2° producto: "))
m2 = int(input("Ingrese el mes de vencimiento del 2° producto: "))
a2 = int(input("Ingrese el año de vencimiento del 2° producto: "))
fecha2 = (d2, m2, a2)

d3 = int(input("\nIngrese el día de vencimiento del 3° producto: "))
m3 = int(input("Ingrese el mes de vencimiento del 3° producto: "))
a3 = int(input("Ingrese el año de vencimiento del 3° producto: "))
fecha3 = (d3, m3, a3)


fechas = [fecha1, fecha2, fecha3]

new_fechas = sorted(fechas)

print("\nOrden de las fechas de vencimiento de menor a mayor:")
print(f"Fecha N°1: {new_fechas[0][0]}/{new_fechas[0][1]}/{new_fechas[0][2]}")
print(f"Fecha N°2: {new_fechas[1][0]}/{new_fechas[1][1]}/{new_fechas[1][2]}")
print(f"Fecha N°3:{new_fechas[2][0]}/{new_fechas[2][1]}/{new_fechas[2][2]}")
