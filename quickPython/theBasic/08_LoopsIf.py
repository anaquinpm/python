""" Remover los elementos negativos de la lista """
x = [1, 3, -5, 0, -1, 3, -2]
for i, n in enumerate(x):
  if n < 0:
    del x[i]
print(x)

""" Contar los numeros negativos """
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
count = 0
for tuple in y:
  for v in tuple:
    if v < 0:
      count += 1
print(f"'y' tiene {count} numeros impares")

""" Dado un número entero evaluar en diferentes categorias según su peso """
x = int(input("ingrese un numero: "))
if x < -5:
  print("Very Low")
elif x < 0:
  print("low")
elif x==0:
  print("neutral")
elif x < 5:
  print("High")
else:
  print("Very High")
