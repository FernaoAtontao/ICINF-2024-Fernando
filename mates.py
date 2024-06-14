import math

# Solicita al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcula el área del círculo
area = math.pi * radio ** 2

# Calcula el perímetro del círculo
perimetro = 2 * math.pi * radio

# Imprime los resultados del área y el perímetro
print("El área del círculo es:", area)
print("El perímetro del círculo es:", perimetro)