# Programa para gestionar inventario y analizar descripciones de productos de una bodega de suministros de oficina

# Función para validar que la descripción tenga al menos 40 caracteres
def validar_descripcion(descripcion):
    if len(descripcion) < 40:
        return False
    return True

# Ingreso de descripciones de productos
producto1 = input("Ingrese la descripción del primer producto (debe tener al menos 40 caracteres): ")
while not validar_descripcion(producto1):
    producto1 = input("La descripción debe tener al menos 40 caracteres. Ingrese nuevamente: ")

producto2 = input("Ingrese la descripción del segundo producto (debe tener al menos 40 caracteres): ")
while not validar_descripcion(producto2):
    producto2 = input("La descripción debe tener al menos 40 caracteres. Ingrese nuevamente: ")

# Ingreso de precio y cantidad disponible de cada producto
precio1 = int(input("Ingrese el precio en CLP del primer producto: "))
cantidad1 = int(input("Ingrese la cantidad disponible del primer producto: "))

precio2 = int(input("Ingrese el precio en CLP del segundo producto: "))
cantidad2 = int(input("Ingrese la cantidad disponible del segundo producto: "))

# Operaciones
# Transformar descripciones a mayúsculas
producto1 = producto1.upper()
producto2 = producto2.upper()

# Unir palabras de las descripciones con espacio en blanco como separador
palabras_producto1 = producto1.split()
descripcion_producto1 = ' '.join(palabras_producto1)

palabras_producto2 = producto2.split()
descripcion_producto2 = ' '.join(palabras_producto2)

# Calcular valor total del inventario para cada producto
valor_total_producto1 = precio1 * cantidad1
valor_total_producto2 = precio2 * cantidad2

# Calcular valor total del inventario de todos los productos
valor_total_inventario = valor_total_producto1 + valor_total_producto2

# Calcular precio promedio entre los productos
precio_promedio = (precio1 + precio2) / 2

# Mostrar resultados
print("\n=== Resultados de la Gestión del Inventario ===")
print(f"Valor total del inventario del primer producto: {valor_total_producto1} CLP")
print(f"Valor total del inventario del segundo producto: {valor_total_producto2} CLP")
print(f"Valor total del inventario de todos los productos: {valor_total_inventario} CLP")
print(f"Precio promedio entre los productos: {precio_promedio} CLP")