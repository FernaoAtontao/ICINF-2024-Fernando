"""Este es un 
comentario multiliea"""

# 1. Declaración de Variables
name = "Fernando"
apellido = "Briones"
edad = 19

# 2. Impresión de Variable (Print Clásico)
print("Hola soy", name)

# 3. Impresión de Variable (Cadenas Literales - f-string)
print(f"Hola mi nombre es {name} y tengo {edad} años")

# 4. Impresión de Variable (Concatenación)
print("Hola mi nombre es " + name + " " + apellido + " y tengo " + str(edad) + " años")

# 5. Declarando Variables Númericas
estatura = 1.71 #declarando número real
n_comp = 5 + 4j
n_comp2 = complex(5,4)

# 6. Formatos de Salida Númerica (Flotantes)

pi = 3.14159
print("PI: ", round(pi,4)) #ocupando función Round
print(f"PI: {pi:.2f}") #ocupando formato con f-string

# 7. Variables en una sola linea (no muy recomendado)
pais, region, ciudad, codigo_postal = "Chile", "Los Lagos", "Castro", 5700000
print(pais + region + ciudad + str(codigo_postal) )

# 8. Utilizando Input

year = input("¿En que año naciste?")
print("El año de nacimiento ingresado es: " , year)