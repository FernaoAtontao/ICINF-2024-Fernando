# Paso 1: Crear una lista para almacenar las fechas de vencimiento
fechas_vencimiento = []

# Paso 2: Pedir al usuario que ingrese las fechas de vencimiento y almacenarlas en la lista como tuplas
dia_1 = int(input("Ingrese el día de la primera fecha de vencimiento: "))
mes_1 = int(input("Ingrese el mes de la primera fecha de vencimiento: "))
año_1 = int(input("Ingrese el año de la primera fecha de vencimiento: "))
fecha_1 = (dia_1, mes_1, año_1)

dia_2 = int(input("Ingrese el día de la segunda fecha de vencimiento: "))
mes_2 = int(input("Ingrese el mes de la segunda fecha de vencimiento: "))
año_2 = int(input("Ingrese el año de la segunda fecha de vencimiento: "))
fecha_2 = (dia_2, mes_2, año_2)

dia_3 = int(input("Ingrese el día de la tercera fecha de vencimiento: "))
mes_3 = int(input("Ingrese el mes de la tercera fecha de vencimiento: "))
año_3 = int(input("Ingrese el año de la tercera fecha de vencimiento: "))
fecha_3 = (dia_3, mes_3, año_3)

# Paso 3: Almacenar las fechas directamente en la lista
fechas_vencimiento = [fecha_1, fecha_2, fecha_3]

# Paso 4: Ordenar las fechas de menor a mayor
fechas_vencimiento.sort()

# Paso 5: Imprimir las fechas ordenadas
print("Fechas de vencimiento ordenadas de menor a mayor:")
print(f"{fechas_vencimiento[0][0]}/{fechas_vencimiento[0][1]}/{fechas_vencimiento[0][2]}")
print(f"{fechas_vencimiento[1][0]}/{fechas_vencimiento[1][1]}/{fechas_vencimiento[1][2]}")
print(f"{fechas_vencimiento[2][0]}/{fechas_vencimiento[2][1]}/{fechas_vencimiento[2][2]}")
