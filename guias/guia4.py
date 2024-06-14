# A) Ingresar el nombre y la edad de tres personas por consola y almacenarlos en un diccionario. 
# Imprimir el nombre y la edad de cada persona.

name1 = input("Ingrese el nombre de la 1° persona: ")
edad1 = int(input(f"Ingrese la edad de {name1}: "))

name2 = input("Ingrese el nombre de la 2° persona: ")
edad2 = int(input(f"Ingrese la edad de {name2}: "))

name3 = input("Ingrese el nombre de la 3° persona: ")
edad3 = int(input(f"Ingrese la edad de {name3}: "))

personas = {
    name1: edad1,
    name2: edad2,
    name3: edad3
}

print("\nDiccionario de Personas:")
print(f"{name1}: {personas[name1]} años")
print(f"{name2}: {personas[name2]} años")
print(f"{name3}: {personas[name3]} años")

# B) Agregar una nueva persona al diccionario
new_name = input("\nIngrese el nombre de una nueva persona: ")
new_edad = int(input(f"Ingrese la edad de {new_name}: "))
personas[new_name] = new_edad

# C) Eliminar una persona del diccionario
nombre_a_eliminar = input("\nIngrese el nombre de la persona a eliminar: ")
del personas[nombre_a_eliminar]

# D) Mostrar el diccionario actualizado
print("\nDiccionario actualizado:")
nombres = list(personas.keys())
edades = list(personas.values())

print(f"{nombres[0]}: {edades[0]} años")
print(f"{nombres[1]}: {edades[1]} años")
print(f"{nombres[2]}: {edades[2]} años")
