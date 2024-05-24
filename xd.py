joel_notas = [5.64, 3.45, 4.56]
alondra_notas = [4.56, 5.64, 6.91]
paz_notas = [3.45, 4.01, 6.23]
joel_promedio = round(sum(joel_notas) / len(joel_notas), 3)
alondra_promedio = round(sum(alondra_notas) / len(alondra_notas), 3)
paz_promedio = round(sum(paz_notas) / len(paz_notas), 3)
joel_nota_min = min(joel_notas)
alondra_nota_min = min(alondra_notas)
paz_nota_min = min(paz_notas)
promedio_final = round((joel_promedio + alondra_promedio + paz_promedio) / 3, 3)
print("El promedio de Joel es de:", joel_promedio)
print("El promedio de Alondra es de:", alondra_promedio)
print("El promedio de Paz es de:", paz_promedio)
print("La nota mínima de Joel es de:", joel_nota_min)
print("La nota mínima de Alondra es de:", alondra_nota_min)
print("La nota mínima de Paz es de:", paz_nota_min)
print("El promedio final de todos los estudiantes es de:", promedio_final)