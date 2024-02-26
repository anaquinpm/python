#!/usr/bin/env python3
in_file = open("leyendo.txt", 'r')          # Abrimos un archivo para escritura
lineas = in_file.readlines()                # Lee línea a línea el objeto
in_file.close()                             # Cerramos el archivo
out_file  = open("escribiendo.txt",'w')     # Escribe desde cero el archivo exista o no.
out_file.writelines(lineas)                 # escribe la lista de strings "lineas" en el objeto. 
out_file.close()
