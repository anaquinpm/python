#!/usr/bin/env python3
"""name: script5.py """
import fileinput
def main():
  for line in fileinput.input():    # input(): sin argumentos este toma los argumentos del sys.argv
    if fileinput.isfirstline():     # isfirstline(): Verifica si estamos por imprimir la primer linea del archivo
      print("<Strat of file {0}>".format(fileinput.filename()))   # filename(): muestra el nombre de archivo
    if not line.startswith('##'):   # Imprime las lineas que no están comentadas
      print (line, end="")
  print(fileinput.filelineno())     # Números de lineas leidas
main()