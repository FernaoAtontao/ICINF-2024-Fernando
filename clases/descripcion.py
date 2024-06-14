descripcion = "Este lapiz azul es de tinta"

# Muestra los primeros 50 caracteres si excede esa longitud se trunca la cadena
descripcion = descripcion[:50]

# Se verifica si la longitud es mayor a 50 caracteres
longitud = len(descripcion) > 50 #longitud es True o False (Booleano)
print(type(longitud))

# Los primeros 10 caracteres de la descripción
descrip_10 = descripcion[:10]

print(f"\nDescripción: {descripcion}")
print(f"¿El tamaño de la cadena descripción es mayor a 50 caracteres? {longitud}")
print(f"Los primeros 10 caracteres de la descripción: {descrip_10}")
