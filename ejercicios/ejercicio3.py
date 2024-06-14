# Ejercicio 3: Gestión de inventario en una bodega de suministros de oficina

# Ingresar la descripción y el precio de los productos
descripcion_producto1 = input("Ingrese la descripción del primer producto (mínimo 40 caracteres): ")
descripcion_producto2 = input("Ingrese la descripción del segundo producto (mínimo 40 caracteres): ")

precio_producto1 = int(input("Ingrese el precio del primer producto en CLP: "))
precio_producto2 = int(input("Ingrese el precio del segundo producto en CLP: "))

cantidad_producto1 = int(input("Ingrese la cantidad disponible del primer producto: "))
cantidad_producto2 = int(input("Ingrese la cantidad disponible del segundo producto: "))

# Transformar las descripciones a mayúsculas
descripcion_producto1 = descripcion_producto1.upper()
descripcion_producto2 = descripcion_producto2.upper()

# Unir las palabras de cada descripción con un espacio en blanco como separador
descripcion_producto1 = ' '.join(descripcion_producto1.split())
descripcion_producto2 = ' '.join(descripcion_producto2.split())

# Calcular el valor total del inventario para cada producto
valor_total_producto1 = precio_producto1 * cantidad_producto1
valor_total_producto2 = precio_producto2 * cantidad_producto2

# Calcular el valor total del inventario de todos los productos
valor_total_inventario = valor_total_producto1 + valor_total_producto2

# Calcular el precio promedio entre los productos
precio_promedio = (valor_total_producto1 + valor_total_producto2) / 2

# Mostrar resultados
print("\nValor total del inventario del primer producto:", valor_total_producto1)
print("Valor total del inventario del segundo producto:", valor_total_producto2)

print("\nValor total del inventario de todos los productos:", valor_total_inventario)
print("Precio promedio entre los productos:", precio_promedio)
