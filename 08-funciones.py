#GUIA RÁPIDA BUCLESS/CICLOS EN PYTHON
#Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos


#01-DECLARANDO LA PRIMERA FUNCIÓN
print("################## 01-DECLARANDO UNA FUNCIÓN SIMPLE ##################")

def mi_primera_funcion():
    print("Esta es mi primera función")


mi_primera_funcion()

#02-DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS
print("\n################## 02-DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS ##################")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()
print(concatenar(lista1,lista2))

#03-DECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS
print("\n################## 03-DECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS ##################")

def multiplicacion (num1,num2):
    return num1*num2

#multiplicacion()
print(multiplicacion(50,50))


#04-EJEMPLO DE UNA FUNCIÓN
print("\n################## 04-FUNCIONES SUMA Y RESTA (POR TECLADO) ##################")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

#Se llama a la función Suma
resultado = suma(a, b)
print("La suma es de:", resultado)

#Se llama a la función resta
resultado2 = resta(a, b)
print("La resta es de:", resultado2)


#05-PASANDO PARAMETROS POR VALOR
print("\n################## 05-PASANDO PARÁMETROS POR VALOR ##################")
def modificar_numero(x):
    x = 10  #Modifica el valor de la variable local 'numero'

x = 5
print("Antes de llamar a la función:", x)  #Imprime 5
modificar_numero(x)
print("Después de llamar a la función:", x)  #Imprime 5


#06-PASANDO PARAMETROS POR REFERENCIA
print("\n################## 06-PASANDO PARÁMETROS POR REFERENCIA ##################")

#Paso por referencia (objetos mutables)
def op_lista(lista):
    lista.append(4)  #Modificando la lista original

numeros = [1, 2, 3]
op_lista(numeros)  #La lista se pasa por referencia
print(numeros)  #se imprime [1, 2, 3, 4]


#Paso por nombre de argumento
def saludar(nombre, mensaje):
    print(mensaje + " " + nombre)

saludar(mensaje="Hola,", nombre="Juan")  #Argumentos pasados por nombre



