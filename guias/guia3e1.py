parrafo = """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion
democratica."""
cantidad = parrafo.lower().count("universidad")
palabras = ("universidad",) * cantidad
print(f"La palabra universidad se repite {cantidad} veces.")
print(f"Palabras encontradas: {palabras}")