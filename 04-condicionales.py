#GUIA RÁPIDA CONDICIONALES EN PYTHON
#Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

from colorama import init, Fore
init()

#CONDICIONAL IF
print(Fore.GREEN + '################ 01 - UTILIZANDO IF y ELSE ################')

licencia = False
edad = 19
automovil = False

#¿Estará correcto este código?                                                  - Código Incorrecto  
print(Fore.YELLOW +'\n>>> Testeando los comparadores y el IF')
if licencia:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia')
else:
    print(Fore.WHITE + 'No tengo licencia para conducir')


#Sucede que la variable licencia se esta comparando con True,
#y se debe asignar directamente, es decir no se ocupa el ==, sino solamente el igual (=)

print(Fore.YELLOW + '\n>>> Utilizando el primer condicional IF')
if licencia:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia\n')
else:
    print(Fore.WHITE + 'No tengo licencia para conducir\n')
print("Este print esta fuera del else")


print(Fore.YELLOW + '>>> Utilizando el segundo condicional IF')
if edad:
    print(Fore.WHITE + 'Puedo conducir porque soy mayor de edad\n')
else:
    print(Fore.WHITE + 'No puedo conducir soy menor de edad\n')
    

print(Fore.YELLOW + '>>> Utilizando el tercer condicional IF')
if edad >= 18:
    print(Fore.WHITE + 'Puedo conducir porque soy mayor de edad\n')
else:
    print(Fore.WHITE + 'No puedo conducir soy menor de edad\n')


print(Fore.GREEN + '################ 02 - UTILIZANDO IF, ELIF y ELSE ################')
if licencia and edad >= 18:
    print(Fore.WHITE + 'Puedo conducir porque soy mayor de edad y tengo licencia')
elif automovil:
    print(Fore.WHITE + 'Tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print(Fore.WHITE + 'No puedo conducir no tengo ni la edad, ni licencia ni automovil')


