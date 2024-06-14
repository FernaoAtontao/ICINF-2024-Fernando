#Importando una biblioteca de Python
import math

# 1. NÚMEROS
print("################## 01.NÚMEROS ##################\n")
estatura = 1.70
peso = 123

# POTENCIA
imc = peso / (estatura ** 2)
print(imc) # Imprimiendo el IMC con decimales
print(math.trunc(imc)) # Imprimiendo la variable IMC truncando

# 2. STRINGS
print("################## 02.STRINGS ##################\n")

institucion = "Universidad de Los Lagos"
asignatura = 'Programación'
descripcion = """Asignatura de primer semestre
de la carrera de Ingeniería Civil en Informática"""

# Imprimir la posición de un caracter en una cadena de texto
print(institucion[-2])

# Concatenación
resultado = print(institucion + " " + asignatura)

# Multiplicación de un String por un Número
salida = print(institucion * 4)

# Función Split en Strings
print(institucion.split())

print(len(institucion))

# 3. BOOLEANOS
print("################## 03.BOOLEANOS ##################\n")
ampolleta = False
interruptor = True

# Utilizando la función Type
print(type(ampolleta),type(interruptor))
print(type(imc))
print(type(peso))

# Salidas Booleanas
print(1 <= 0)
print(100 >= 10)
print(19 == 19)

#Utilizando la función Bool
print(bool(0))
print(bool(1))

# 4. LISTAS
print("################## 04.LISTAS ##################\n")

# Declarando e Inicializando Listas
ciudades = ["Castro", "Queilen", "Ancud", "Quellón", "Chonchi"]
varios = ["Nicolas", 20, True]

# Otra forma de incializar listas
#list("Python", "Ruby")
print(ciudades)
print(type(ciudades))