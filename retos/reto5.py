n = int(input("Ingresa un numero: "))
a, b = 0, 1
f = []
while a <= n:
    f.append(a)
    a, b = b, a + b
print(f)