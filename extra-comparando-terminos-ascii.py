#Comparando términos númericos (ASCII)
print("Comparando Números")

palabra = "AAAA"
for ch in palabra:
    print(ch + ' = ' + str(ord(ch)))

palabra1 = "aaaa"
for ch1 in palabra1:
    print(ch1 + ' = ' + str(ord(ch1)))

print(palabra == palabra1)