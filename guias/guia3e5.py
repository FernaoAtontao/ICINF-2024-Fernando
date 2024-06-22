import random
numerosaleatorios = [random.randint(40, 350) for _ in range(20)]
digitobuscado = int(input("Ingresa un dígito para buscar en la lista: "))
ocurrencias = sum(str(numero).count(str(digitobuscado)) for numero in numerosaleatorios)
print(f"Lista de números aleatorios: {numerosaleatorios}")
print(f"El dígito {digitobuscado} aparece {ocurrencias} veces en la lista.")
