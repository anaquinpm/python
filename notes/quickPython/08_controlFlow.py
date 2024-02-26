def a_func():
  # código para ejecutar
def b_func():
  # código para ejecutar
def c_func():
  # código para ejecutar

dicc_fc = {
  'a' : a_func,
  'b' : b_func,
  'c' : c_func
}

x = 'a'
dicc_fc[x]()  # ejecuta la función del diccionario

x = [1 , -8, 2, -3, 9, 4]
for n in range(len(x)):   # range(start, stop [, step])
  if x[n]>0:
    print("Números positivos en el index", n)

list(range(8, 3, -2))

list = [(1, 2), (3, 4), (5, 6)]
resultado = 0
for x, y in list:
  resultado = resultado + x * y

x = [1 , -8, 2, -3, 9, 4]
for i, v in enumerate(x):
  if x[i]>0:
    print("Números positivos en el index", i)

x = [1, 2, 3, 4]
y = ["a", "b", "c"]
z = zip(x, y)
list(z)

## Comprehensions
x = [1, 2, 3, 4]
x_cuadrado_list = [item * item for item in x if item > 2]         # Comprehensions en listas
x_cuadrado_dicc = {item: item * item for item in x if item > 2}   # Comprehensions en diccionarios

### Generador de expresiones
x = [1 , 2 , 3, 4]
x_cuadrado = (item * item for item in x)    # x_cuadrado es un objeto
for valor in x_cuadrado:
  print(valor)

### Comparaciones y operadores booleanos
[2] and [3, 4]
[] and 5
[2] or [3, 4]
[] or 5
1 > 0 or []