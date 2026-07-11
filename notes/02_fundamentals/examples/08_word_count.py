#!env python3
""" Leer un archivo y devolver el número de lineas, palabras y caracteres
    Similar al comando 'wc' de UNIX
""" 
line_count, word_count, char_count = 0, 0, 0
with open('08_word_count.tst') as lines:
  for line in lines:
    line_count += 1
    words = line.split()
    word_count += len(words)
    char_count += len(line.strip(",.\t\n "))

print("El archivo tiene {0} lineas, {1} palabras, {2} caracteres".format(line_count, word_count, char_count))