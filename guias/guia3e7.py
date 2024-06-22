factorial = 1
numero = input("Ingrese un número entero no negativo para calcular su factorial: ")

if numero.isdigit() and int(numero) >= 0:
    numero = int(numero)
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es: {factorial}")
else:
    print("Error: El número debe ser un entero no negativo.")