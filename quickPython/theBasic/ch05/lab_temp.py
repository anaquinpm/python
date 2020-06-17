#!/usr/bin/env python3
"""" buscar la temperatura promedio, mínima, máxima, mediana"""
# Determinar cuales son las ocurrencias de temperaturas que ocurrieron una sola vez


""" Función que utiliza una variable dictionary para contar las ocurrencias. """
def alone():
  tmps = set(temperatures)          # Convierto la "lista" en un "set", eliminando así los elementos repetidos y usaandolo como indice
  ocurrencias = {}                  # Creo un "dictionary" donde voy a colocar las ocurrencias de los valores
  unicas = []                       # Lista de valores con ocurrencias únicas

  for x in tmps:                    # Inicializo el diccionario con los indices a buscar.
      ocurrencias[x]=0
  for tmp in temperatures:          # Recorro la lista que contiene las temperaturas
    ocurrencias[tmp]+=1             # y sumo la ocurrencia de cada valor en el diccionario
  for y in ocurrencias:             # Identificar valores que ocurrieron una sola vez
    if ocurrencias[y] == 1:
      unicas.append(y)
  print ("Estas son las ocurrencias por cada número:\n", ocurrencias)
  return unicas

"""" Calculo de la Mediana según el número de elementos que contenga la muestra """
def mediana():
  mid = len(temperatures)/2                           # La mediana se calcula, o no, según el n° de muestras
  if mid.is_integer():                                # Si mid es entero, se hace un promedio de los 2 elementos centrales
      mid_down = temperatures[int(mid)]               # "int" nos asegura que no tengamos coma en el indice 
      mid_up = temperatures[int(mid)+1]
      tmp_med = (mid_down + mid_up)/2
  else:                                               # Si mid no es entero, la Mediana es el dato central del conjunto
      tmp_med = temperatures[int(mid)+1]
  return tmp_med

temperatures = []                   # Creamos lista donde vamos a colocar todos los datos a procesar
with open('lab.txt') as infile:
  for row in infile:
    temperatures.append(int(float(row.strip())))

print("Cantidad de datos aevaluar: ", len(temperatures))
tmp_max = max(temperatures)
print ("La remperatura máxima: ", tmp_max)
tmp_min = min(temperatures)
print ("La remperatura mínima: ", tmp_min)
tmp_avr = sum(temperatures)/len(temperatures)       # Promedio o media aritmética
print ("La remperatura promedio: ", tmp_avr)

print ("La remperatura mediana: ", mediana())
unicas = alone ()
print("Las temperaturas que solo ocurrieron una sola vez en el periodo:\n",unicas)
