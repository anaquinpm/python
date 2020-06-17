# Crear lista con los valores positivos que encontramos en x (list comprehension)
x = [1, -4, -6, 8, -9, 2]
positives = [value for value in x if value > 0]

# Crear un generador que retorne los números impares que en contramos entre 1-100.
odd_values = (y for y in range(1, 100) if y % 2)
for odd_n in odd_values:
  print(odd_n)

# Crear un diccionarios de numeros con sus repectivos cubos, del 11 hasta el 15.
cube = {value: value**3 for value in range(11,15)}
