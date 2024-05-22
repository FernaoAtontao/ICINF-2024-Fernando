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
print("Promedio de Joel:", joel_promedio)
print("Promedio de Alondra:", alondra_promedio)
print("Promedio de Paz:", paz_promedio)
print("Nota mínima de Joel:", joel_nota_min)
print("Nota mínima de Alondra:", alondra_nota_min)
print("Nota mínima de Paz:", paz_nota_min)
print("Promedio final de todos los estudiantes:", promedio_final)