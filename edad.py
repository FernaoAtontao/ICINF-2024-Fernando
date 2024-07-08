'''
< 0 no existente
<= 12 niño
<= 17 adolecente
<= 64 adulto
<= 120 abuelo
>= 120 el diablo
'''

edad = int(input("ingrese la edad de una persona: "))
if edad < 0 or edad >= 120:
    categoria = "Edad invalida"
elif edad <= 12:
    categoria = "Niño"
elif edad <= 17:
    categoria = "Adolecente"
elif edad <= 64:
    categoria = "Adulto"
else:
    categoria = "Viejo"
print(f"La persona es: {categoria}")