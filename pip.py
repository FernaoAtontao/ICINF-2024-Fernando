import math 

estatura = 1.70
peso = 70

# Calcula el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Redondea el IMC a dos decimales
imc_redondeado = round(imc, 2)

print(imc_redondeado)
