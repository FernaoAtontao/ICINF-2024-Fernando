censo_2017 = {}
censo_2017[14] = {"Nombre de Región": "Los Ríos", "Área (Km2)": 18429, "Población  (2017)": 404432}
censo_2017[12] = {"Nombre de Región": "Magallanes", "Área (Km2)": 1382291, "Población  (2017)": 166533}

for region in censo_2017.values():
    region["Densidad"] = round(region["Población  (2017)"] / region["Área (Km2)"], 1)

censo_2017[14]["Capital"] = "Valdivia"
censo_2017[12]["Capital"] = "Punta Arenas"

censo_2017[14]["Comunas"] = ["Ranco", "Valdivia", "Río Bueno"]
censo_2017[12]["Comunas"] = ["Antártica Chilena", "Magallanes", "Tierra del Fuego"]

censo_2017[14]["Provincia"] = ("Los Ríos",)
censo_2017[12]["Provincia"] = ("Magallanes", "Antártica Chilena", "Tierra del Fuego")

censo_2017[12]["Nombre de la Región"] = "Magallanes y Antártica Chilena"

print("Diccionario del Censo 2017 con cambios:", censo_2017)

tuplas = list(censo_2017.items())
print("Lista de tuplas:", tuplas)