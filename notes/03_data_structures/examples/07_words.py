"""  Contando palabras """
parrafo = "Probando como hacemos con python para contar palabras"
ocurrencias={}
for palabra in parrafo.split():
  ocurrencias[palabra]= ocurrencias.get(palabra, 0) + 1
for palabra in ocurrencias:
  print("La palabra ", palabra, "ocurrio", ocurrencias[palabra], "veces en el parrafo")
