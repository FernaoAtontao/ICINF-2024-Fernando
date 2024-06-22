n = int(input("Ingrese el n de cubos a calcular: "))
primerimpar = 1
sumaimpares = 0
contadorimpares = 0 
for i in range(1, n + 1):
    sumaimpares = 0
    contadorimpares = 0
    numerosimpares = []
    while contadorimpares < i:
        sumaimpares += primerimpar
        numerosimpares.append(primerimpar)
        primerimpar += 2
        contadorimpares += 1
    print(f"{i}^3 =", end=" ")
    for j in range(len(numerosimpares)):
        if j < len(numerosimpares) - 1:
            print(numerosimpares[j], "+", end=" ")
        else:
            print(numerosimpares[j], end=" ")
    print(f"= {sumaimpares}")