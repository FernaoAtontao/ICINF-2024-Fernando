# A) Crear tres sets diferentes con los nombres de tres animales en cada uno: aves, animales terrestres y animales acuáticos
aves = {"Águila", "Pato", "Canario"}
animales_terrestres = {"León", "Elefante", "Nutria"}
animales_acuaticos = {"Pato", "Delfín", "Nutria"}

# Impresion de Sets
print("\n############ SETS DE ANIMALES INICIAL ############")
print(f"Aves: {aves}")
print(f"Animales Terrestres: {animales_terrestres}")
print(f"Animales Acuáticos: {animales_acuaticos}")

# B) Agregar un nuevo animal a cada set utilizando la función correspondiente en Python, y mostrar los sets actualizados
aves.add("Loro")
animales_terrestres.add("Tigre")
animales_acuaticos.add("Tiburón")


print("\n############ SETS DE ANIMALES ACTUALIZADOS ############")
print(f"Aves: {aves}")
print(f"Animales Terrestres: {animales_terrestres}")
print(f"Animales Acuáticos: {animales_acuaticos}")

# C) Encontrar y mostrar los animales que pueden pertenecer a más de una categoría utilizando la función correspondiente
interseccion_aves = aves.intersection(animales_terrestres)
interseccion_terrestres = aves.intersection(animales_acuaticos)
interseccion_acuaticos = animales_terrestres.intersection(animales_acuaticos)

print("\n############ ANIMALES QUE PERTENECEN A MÁS DE UNA CATEGORÍA ############")
print(f"Aves y Animales Terrestres: {interseccion_aves}")
print(f"Aves y Animales Acuáticos: {interseccion_terrestres}")
print(f"Animales Terrestres y Animales Acuáticos: {interseccion_acuaticos}")
