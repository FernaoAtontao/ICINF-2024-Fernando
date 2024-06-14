# Paso 1: Crear sets para almacenar las categorías de animales
aves = {"Aguila", "Pato", "Canario"}
terrestres = {"León", "Elefante", "Nutria"}
acuaticos = {"Pato", "Delfín", "Nutria"}

# Paso 2: Mostrar los sets originales
print("Sets originales:")
print("Aves:", aves)
print("Terrestres:", terrestres)
print("Acuáticos:", acuaticos)

# Paso 3: Agregar un nuevo animal a cada set
aves.add("Loro")
terrestres.add("Tigre")
acuaticos.add("Ballena")

# Paso 4: Mostrar los sets actualizados
print("Sets actualizados:")
print("Aves:", aves)
print("Terrestres:", terrestres)
print("Acuáticos:", acuaticos)

# Paso 5: Encontrar y mostrar los animales que pueden pertenecer a más de una categoría
animales_comunes = aves & terrestres & acuaticos
print("Animales en más de una categoría:", animales_comunes)
