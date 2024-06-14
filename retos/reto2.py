nombre_estudiante = input("Ingrese el nombre del estudiante: ")
asignaturas = []
nombre_asignatura1 = input("Ingrese el nombre de la asignatura 1: ")
nota_lab1_1 = float(input("Ingrese la nota del Laboratorio N°1 de la asignatura 1: "))
nota_lab2_1 = float(input("Ingrese la nota del Laboratorio N°2 de la asignatura 1: "))
nota_lab3_1 = float(input("Ingrese la nota del Laboratorio N°3 de la asignatura 1: "))
promedio_ponderado1 = round((nota_lab1_1 * 0.3) + (nota_lab2_1 * 0.5) + (nota_lab3_1 * 0.2), 1)
info_asignatura1 = (nombre_asignatura1, {nota_lab1_1, nota_lab2_1, nota_lab3_1}, promedio_ponderado1)
asignaturas.append(info_asignatura1)
nombre_asignatura2 = input("Ingrese el nombre de la asignatura 2: ")
nota_lab1_2 = float(input("Ingrese la nota del Laboratorio N°1 de la asignatura 2: "))
nota_lab2_2 = float(input("Ingrese la nota del Laboratorio N°2 de la asignatura 2: "))
nota_lab3_2 = float(input("Ingrese la nota del Laboratorio N°3 de la asignatura 2: "))
promedio_ponderado2 = round((nota_lab1_2 * 0.3) + (nota_lab2_2 * 0.5) + (nota_lab3_2 * 0.2), 1)
info_asignatura2 = (nombre_asignatura2, {nota_lab1_2, nota_lab2_2, nota_lab3_2}, promedio_ponderado2)
asignaturas.append(info_asignatura2)
nombre_asignatura3 = input("Ingrese el nombre de la asignatura 3: ")
nota_lab1_3 = float(input("Ingrese la nota del Laboratorio N°1 de la asignatura 3: "))
nota_lab2_3 = float(input("Ingrese la nota del Laboratorio N°2 de la asignatura 3: "))
nota_lab3_3 = float(input("Ingrese la nota del Laboratorio N°3 de la asignatura 3: "))
promedio_ponderado3 = round((nota_lab1_3 * 0.3) + (nota_lab2_3 * 0.5) + (nota_lab3_3 * 0.2), 1)
info_asignatura3 = (nombre_asignatura3, {nota_lab1_3, nota_lab2_3, nota_lab3_3}, promedio_ponderado3)
asignaturas.append(info_asignatura3)
estudiante = {nombre_estudiante: asignaturas}
clave_estudiante = list(estudiante.keys())[0]
print("Nombre del Estudiante: " + clave_estudiante)
datos_asignaturas = estudiante[clave_estudiante]
asignatura1 = datos_asignaturas[0]
print("Asignatura: " + asignatura1[0])
print("Notas de Laboratorio: " + str(asignatura1[1]))
print("Promedio Ponderado: " + str(asignatura1[2]))
asignatura2 = datos_asignaturas[1]
print("Asignatura: " + asignatura2[0])
print("Notas de Laboratorio: " + str(asignatura2[1]))
print("Promedio Ponderado: " + str(asignatura2[2]))
asignatura3 = datos_asignaturas[2]
print("Asignatura: " + asignatura3[0])
print("Notas de Laboratorio: " + str(asignatura3[1]))
print("Promedio Ponderado: " + str(asignatura3[2]))