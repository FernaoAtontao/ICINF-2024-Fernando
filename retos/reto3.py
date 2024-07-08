Ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
Indices_calidad_de_aire = [134, 99, 245, 1000]
Indice_mas_bajo = min(Indices_calidad_de_aire)
Indice_mas_alto = max(Indices_calidad_de_aire)
Ciudad_mas_baja = Ciudades[Indices_calidad_de_aire.index(Indice_mas_bajo)]
Ciudad_mas_alta = Ciudades[Indices_calidad_de_aire.index(Indice_mas_alto)]
print(f"Ciudad con índice de calidad del aire más bajo: {Ciudad_mas_baja} ({Indice_mas_bajo})")
print(f"Ciudad con índice de calidad del aire más alto: {Ciudad_mas_alta} ({Indice_mas_alto})")
def Categoria(indice):
    if indice <= 50:
        return "Buena"
    elif indice <= 100:
        return "Moderada"
    elif indice <= 150:
        return "Dañina a la salud para grupos sensibles"
    elif indice <= 200:
        return "Dañina a la salud"
    elif indice <= 300:
        return "Muy dañina a la salud"
    else:
        return "Peligrosa"
Categoria_indice_bajo = Categoria(Indice_mas_bajo)
Categoria_indice_alto = Categoria(Indice_mas_alto)
print(f"Categoría del índice más bajo ({Indice_mas_bajo}): {Categoria_indice_bajo}")
print(f"Categoría del índice más alto ({Indice_mas_alto}): {Categoria_indice_alto}")