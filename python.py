
print()

'''En este Archivo se recopilara toda la
informacion sobre como usar Python'''


# Declarando Variable
nombre = "Fernando"

# Impresión de la Variable
print("Esta es la impresión de la Variable")
print()
print(nombre)
print("Hola, soy", nombre)


print()
print()


# Funcion print
nombre = "Fernando"
print("Funcion Print")
print()
print("Hola, soy", nombre)   # Usando separador de la coma
print(f"Hola, soy {nombre}")   # Usando Cadena Literal f
print("Hola, soy " + nombre)   # Usando Concatencion


print()
print()


# Funcion input
nombre = input("¿Cual es tu nombre? ")
print("Hola, mi nombre es", nombre)


print()
print()


# Datos Basicos de Python

'''
Datos Númericos

Los principales Datos Númericos de Python son:
- Números Enteros (int)
- Números de Punto Flotante (float)   # Los números en coma flotante son números con decimales (números reales)
- Números Complejos (complex)   # Cuando los números imaginarios se combinan con los números reales obtenemos lo que se conoce como números complejos
'''

# números Enteros (int)
edad = 19
año_de_nacimiento = 2005

print(f"Hola, tengo {edad} y naci en {año_de_nacimiento}")

print()

# números Flotantes (float)
estatura = 1.70
peso = 100

print(f"Hola, mi estatura es de {estatura}m y peso {peso}kg")

print()

# números Complejos (complex)
complejo = 1 + 4j
complejo2 = complex(6,10)

print()

# Formateo de la salida de números
numero_cualquiera = 3.736428

print("Mostrando 3 decimales: {:.3f}".format(numero_cualquiera))   # Cambiando el {:.3f} por {:.2f} daria como resultado la impresión del numero con solo dos decimales

print()

'''
Algunas Funciones con Datos Númericos


float - Convierte un valor a un número decimal

int - Convierte un valor a un entero

min - Devuelve el valor más pequeño de uno o más valores

max - Devuelve el valor más grande de uno o más valores

round - Redondea un número a un número específico de dígitos decimales

sum - Devuelve la suma de una lista de números
'''


print()
print()


'''
Strings

El texto de los strings, debe estar encerrado en comillas simples, dobles o triples.
- Con las comillas triples podemos escribir el texto en varias líneas, tipo párrafo.
- Dentro de las comillas se pueden añadir caracteres especiales añadiendo el símbolo
backslash ( \ ), como por ejemplo: \n, el carácter de salto de línea, o \t, el de
tabulación.
- Las cadenas no se pueden modificar.
'''

# Ejemplo
asignatura = 'Programacion'
carrera = "Ingenieria Civil en Informatica"
descripcion = '''La asignatura de Programacion se imparte en el primer semestre, tiene como objetivo
entregar la base logica para que cualquier estudiante comience a familiarizarse con la programacion'''


# Acceder a un elemento de un string
saludo = 'Hola Mundo!'
print(saludo[0])   # 0 es la primera letra
print(saludo[1])   # 1 es la segunda letra

# Con números negativos contara hacia atras
print(saludo[-1])   # -1 es la ultima letra
print(saludo[-2])   # -2 es la penultima letra


print()


# Concatenar
saludoparte1 = "Hola"
saludoparte2 = "Mundo!"

print(saludoparte1 + " " + saludoparte2)


print()


# Multiplicar Cadena
palabra = "Hola"
resultado = palabra * 4
print(resultado)   # La salida en terminal sera: HolaHolaHolaHola


print()


# Funcion split
institucion = "Universidad de los Lagos"

print(institucion.split())


print()


'''
Algunas funciones con strings


len() - Devuelve la longitud de la cadena

str() - Convierte un objeto en un string

upper() - Devuelve una copia del string en mayúsculas

lower() - Devuelve una copia del string en minúsculas

split() - Divide la cadena en subcadenas utilizando un separador especificado

join() - Une strings utilizando la cadena de texto que lo llama como separador
'''


print()


'''
Booleanos

Es un tipo de dato que permite almacenar dos valores; True o False
'''

# Ejemplos
interruptor = True
ampolleta = False
print(interruptor)
print(ampolleta)

print()

print(1 < 0)
print(5 == 6)
print(3 == 3)
print(10 <= 8)


print()


# Convertir valor a bool

print(bool(0))   # El valor 0 (nada) nos da False
print(bool(1))   # El valor 1 (2, 3, 4...) nos da True
print(bool(""))   # Al no haber nada de texto, nos da False
print(bool([]))   # Al no haber ningun valor, nos da False
print(bool("False"))   # Al haber un texto, nos da True



print()