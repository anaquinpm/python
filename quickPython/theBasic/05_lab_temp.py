# buscar la temperatura promedio, mínima, máxima, media
# determinar cuales son las ocurrencias de temperaturas que ocurrieron una sola vez

temperatures = []
## funcion que utiliza una variable dictionary para contar las ocurrencias.
def ocurrencias_unicas(lista_tmp):
  tmps = list(set(lista_tmp))   ## con sets convierto la "lista" en un "set" donde elimino los elementos repetidos
  ocurrencias = {}    ## creo la variable dictionary
  unicas = []         ## lista de valores que solo tienen una ocurrencias_unicas

  for x in tmps:
    ocurrencias[x]=0
  for tmp in lista_tmp:     
    ocurrencias[tmp]+=1
  for y in ocurrencias:
    if ocurrencias[y] == 1:
      unicas.append(y)
  print (ocurrencias)
  return unicas

with open('05_lab.txt') as infile:
  for row in infile:
    temperatures.append(int(float(row.strip())))
tmp_max = max(temperatures)
tmp_min = min(temperatures)
tmp_avr = sum(temperatures)/len(temperatures)
tmp_med = (tmp_max+tmp_min)/2

unicas = ocurrencias_unicas (temperatures)
print(unicas)