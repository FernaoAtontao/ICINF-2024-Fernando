descripcion_articulo = (input("Aqui escribe una wea de mas de 50 caracteres:"))
es_larga = len(descripcion_articulo) >= 50
primeros_10_caracteres = descripcion_articulo[:10]
print("Descripción del artículo:", descripcion_articulo)
print("¿La descripción es larga?", es_larga)
print("Primeros 10 caracteres:", primeros_10_caracteres)
