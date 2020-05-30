#!/usr/bin/env python3
"""" buscar la temperatura promedio, mínima, máxima, mediana"""
# Determinar cuales son las ocurrencias de temperaturas que ocurrieron una sola vez


# Función que utiliza una variable dictionary para contar las ocurrencias.
def alone(lista_tmp):
  tmps = set(lista_tmp)             # Con sets convierto la "lista" en un "set" donde elimino los elementos repetidos y usarlo como indice
  ocurrencias = {}                  # Creo un "dictionary" donde voy a colocar las ocurrencias de los valores
  unicas = []                       # Lista de valores con ocurrencias únicas

  for x in tmps:                    # Inicializo el diccionario con los indices a buscar y pongo a 0 sus ocurrencias.
    ocurrencias[x]=0
  for tmp in lista_tmp:             # Recorro la lista que contiene las temperaturas elemento a elemento
    ocurrencias[tmp]+=1             # y sumo la ocurrencia de cada valor en el diccionario
  for y in ocurrencias:             # En este for vamos averificar aquellos valores que ocurrieron una sola vez
    if ocurrencias[y] == 1:
      unicas.append(y)
  print ("Estas son las ocurrencias por cada número:\n", ocurrencias)
  return unicas

temperatures = []                   # Creamos lista donde vamos a colocar todos los datos a procesar
with open('lab.txt') as infile:
  for row in infile:
    temperatures.append(int(float(row.strip())))

tmp_max = max(temperatures)
print ("La remperatura máxima: ", tmp_max)
tmp_min = min(temperatures)
print ("La remperatura mínima: ", tmp_min)
tmp_avr = sum(temperatures)/len(temperatures)       # Promedio o media aritmética
print ("La remperatura promedio: ", tmp_avr)

# Calculo de la Mediana según el número de elementos que contenga la muestra
mid = int(len(temperatures)/2) 
if 0 == mid%2:                                      # Si es par, de hace un promedio de los elementos centrales
    mid_down = temperatures[int(mid)]
    mid_up = temperatures[int(mid)+1]
    tmp_med = (mid_down + mid_up)/2
else:                                              # Si es impar, la Mediana es el dato central del conjunto
    tmp_med = temperatures[mid]
print ("La remperatura mediana: ", tmp_med)

unicas = alone (temperatures)
print("Las temperaturas que solo ocurrieron una sola vez en el periodo:\n",unicas)