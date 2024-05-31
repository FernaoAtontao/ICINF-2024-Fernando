#Ingresar un breve resumen del artículo igual o menor a 60 caracteres. Solicitar este breve resumen por terminal.

resumen = input("Ingrese un breve resumen del artículo (60 caracteres o menos): ")

#Crear una variable booleana que almacene True si la longitud de la variable que almacena el resumen es igual o menor a 60 caracteres y False en caso contrario.

resumenvalido = len(resumen) <= 60

#Imprimir la longitud de caracteres del breve resumen del artículo Convertir el resumen en mayúsculas utilizando la función de Python adecuada.
#Mostrar los últimos diez caracteres del resumen. Unir las palabras del resumen con un guión (-) como separador utilizando la función correcta.

print("Longitud del resumen:", len(resumen))
print("Resumen en mayúsculas:", resumen.upper())
print("Últimos 10 caracteres:", resumen[-10:])
print("Resumen con guión como separador:", "-".join(resumen.split()))

#Me voy a morir solo :)