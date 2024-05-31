#Aqui esta definiendo cosas/Inicializar los precios unitarios de cada fruta y las cantidades en formato de número entero.

manzana = (100)
pera = (250)
durazno = (300)
totalmanzana = (150)
totalpera = (80)
totaldurazno = (120)

#imprime Obtener e imprimir el total a pagar por cada tipo de fruta comprada

print ("Precio unitario de cada fruta. Manzana:", manzana, "Pera:", pera, "Durazno:", durazno)
cantidadmanzana = int(input ("Cuantas manzanas deseas comprar (limite 150)?: "))
cantidadpera = int(input ("Cuantas peras deseas comprar (limite 80)?: "))
cantidaddurazno = int(input ("Cuantos duraznos deseas comprar (limite 120)?: "))

#Se me olvido como podia poner el limite para que si superase ese limite se repitiera hasta que respete el limite

total = (100 * (cantidadmanzana))
totala =  (250 * (cantidadpera))
totalaa = (300 * (cantidaddurazno))
print ("Total a pagar por comprar cada fruta: Manzana", total, "Pera", totala, "Durazno:", totalaa,)

#La suma total a pagar por la compra de las manzanas y peras.

manpera = (100 * (cantidadmanzana)) + (250 * (cantidadpera))
print ("Suma del total a pagar por especificamente las manzañas y peras:",total,"+", totala,"=",manpera)

#El valor máximo entre los tres totales utilizando la función correspondiente en Python.

print ("El valor maximo entre los tres totales", (int(manzana * 150) + (int(pera * 80)) + (int(durazno * 120))))

#El valor mínimo entre los tres totales utilizando la función correspondiente en Python.

print ("El valor mínimo entre los tres totales", manzana + pera + durazno)

#Me quede en blanco con las funciones min y max perdon. El promedio del precio unitario de todas las frutas.

promedio = (total + totala + totalaa) / 3
print("El promedio del precio unitario de todas las frutas.", promedio)

#Ya me dio depresion.