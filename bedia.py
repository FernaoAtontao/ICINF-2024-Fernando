# Paso 1: Crear una lista para almacenar las marcas de bebidas gaseosas.
marcas_bebidas = []

# Paso 2: Pedir al usuario que ingrese las marcas de bebidas gaseosas y almacenarlas en la lista.
marca_1 = input("Ingrese el nombre de una marca de bebida gaseosa: ")
marca_2 = input("Ingrese el nombre de otra marca de bebida gaseosa: ")
marca_3 = input("Ingrese el nombre de otra marca de bebida gaseosa: ")
marca_4 = input("Ingrese el nombre de otra marca de bebida gaseosa: ")

# Paso 3: Almacenar las marcas directamente en la lista.
marcas_bebidas = [marca_1, marca_2, marca_3, marca_4]

# Paso 4: Imprimir la lista completa de marcas de bebidas gaseosas.
print("Lista completa de marcas de bebidas gaseosas:")
print(marcas_bebidas)

# Paso 5: Mostrar el nombre de la primera bebida gaseosa en la lista.
print("La primera bebida gaseosa es:", marcas_bebidas[0])

# Paso 6: Mostrar el nombre de la última bebida gaseosa en la lista.
print("La última bebida gaseosa es:", marcas_bebidas[-1])