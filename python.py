# Declarando una cadena de documentación
'''
En este archivo se recopilará toda la información sobre cómo usar Python.
'''

# Declarando Variable
nombre = "Fernando"

# Impresión de la Variable
print("Esta es la impresión de la Variable")
print(nombre)
print("Hola, soy", nombre)

# Funcion print
print("\nFunción Print")
print("Hola, soy", nombre)   # Usando separador de la coma
print(f"Hola, soy {nombre}")   # Usando Cadena Literal f
print("Hola, soy " + nombre)   # Usando Concatenación

# Funcion input
nombre = input("\n¿Cuál es tu nombre? ")
print("Hola, mi nombre es", nombre)

# Datos Básicos de Python
'''
Datos Numéricos

Los principales Datos Numéricos de Python son:
- Números Enteros (int)
- Números de Punto Flotante (float)
- Números Complejos (complex)
'''

# Números Enteros (int)
edad = 19
año_de_nacimiento = 2005
print(f"\nHola, tengo {edad} años y nací en {año_de_nacimiento}")

# Números Flotantes (float)
estatura = 1.70
peso = 100
print(f"Hola, mi estatura es de {estatura}m y peso {peso}kg")

# Números Complejos (complex)
complejo = 1 + 4j
complejo2 = complex(6, 10)

# Formateo de la salida de números
numero_cualquiera = 3.736428
print("\nMostrando 3 decimales: {:.3f}".format(numero_cualquiera))

'''
Algunas Funciones con Datos Numéricos

- float: Convierte un valor a un número decimal
- int: Convierte un valor a un entero
- min: Devuelve el valor más pequeño de uno o más valores
- max: Devuelve el valor más grande de uno o más valores
- round: Redondea un número a un número específico de dígitos decimales
- sum: Devuelve la suma de una lista de números
'''

'''
Strings

El texto de los strings debe estar encerrado en comillas simples, dobles o triples.
- Con las comillas triples podemos escribir el texto en varias líneas, tipo párrafo.
- Dentro de las comillas se pueden añadir caracteres especiales añadiendo el símbolo
backslash (\), como por ejemplo: \n, el carácter de salto de línea, o \t, el de
tabulación.
- Las cadenas no se pueden modificar.
'''

# Ejemplo
asignatura = 'Programación'
carrera = "Ingeniería Civil en Informática"
descripcion = '''La asignatura de Programación se imparte en el primer semestre, tiene como objetivo
entregar la base lógica para que cualquier estudiante comience a familiarizarse con la programación'''

# Acceder a un elemento de un string
saludo = 'Hola Mundo!'
print(saludo[0])   # 0 es la primera letra
print(saludo[1])   # 1 es la segunda letra
print(saludo[-1])   # -1 es la última letra
print(saludo[-2])   # -2 es la penúltima letra

# Concatenar
saludoparte1 = "Hola"
saludoparte2 = "Mundo!"
print(saludoparte1 + " " + saludoparte2)

# Multiplicar Cadena
palabra = "Hola"
resultado = palabra * 4
print(resultado)   # La salida en terminal será: HolaHolaHolaHola

# Función split
institucion = "Universidad de los Lagos"
print(institucion.split())

'''
Algunas funciones con strings

- len(): Devuelve la longitud de la cadena
- str(): Convierte un objeto en un string
- upper(): Devuelve una copia del string en mayúsculas
- lower(): Devuelve una copia del string en minúsculas
- split(): Divide la cadena en subcadenas utilizando un separador especificado
- join(): Une strings utilizando la cadena de texto que lo llama como separador
'''

'''
Booleanos

Es un tipo de dato que permite almacenar dos valores; True o False
'''

# Ejemplos
interruptor = True
ampolleta = False
print(interruptor)
print(ampolleta)

print(1 < 0)
print(5 == 6)
print(3 == 3)
print(10 <= 8)

# Convertir valor a bool
print(bool(0))   # El valor 0 (nada) nos da False
print(bool(1))   # El valor 1 (2, 3, 4...) nos da True
print(bool(""))   # Al no haber nada de texto, nos da False
print(bool([]))   # Al no haber ningún valor, nos da False
print(bool("False"))   # Al haber un texto, nos da True
