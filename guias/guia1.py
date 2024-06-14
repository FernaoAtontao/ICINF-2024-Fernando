#A) Ingresar 4 nombres de marcas de bebida por consola y almacenarlos en una lista
bebida1 = input("Ingrese la marca de la 1° bebida: ")
bebida2 = input("Ingrese la marca de la 2° bebida: ")
bebida3 = input("Ingrese la marca de la 3° bebida: ")
bebida4 = input("Ingrese la marca de la 4° bebida: ")

# Lista de bebidas
bebidas = [bebida1, bebida2, bebida3, bebida4]

# B) Imprimir la lista completa
print("\nLista completa de bebidas gaseosas:")
print(bebidas)

# C) Mostrar el primer y último nombre de las bebidas de la lista
print(f"\nPrimera bebida de la lista: {bebidas[0]}")
print(f"Última bebida de la lista: {bebidas[-1]}")
