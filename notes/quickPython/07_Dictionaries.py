""" Seleccionar el código a ejecutar en algún IDE """
y={}
y["cero"] = 3.14    ##Podemos crear arbitrariamente una posición
y[1] = 'Goodbye'
y[1] + ', Friend.'
y[2] = 2
y["cero"] * y[2]

espanol_a_ingles = {'rojo': 'red', 'verde': 'green', 'azul': 'blue'}
len(espanol_a_ingles)         # numero de elementos
list(espanol_a_ingles.keys())   # valores de las keys
list(espanol_a_ingles.values()) # obtener los valores
list(espanol_a_ingles.items())  # obtener los pares key-value
del espanol_a_ingles['azul']    # elimina un item

'rojo' in espanol_a_ingles        # verificamos que el "key" exista. Retorna True/False
print(espanol_a_ingles.get('azul', 'Sin traducción'))       # si no existe el key devuelve None por defecto, si tiene segundo argumento la fc. devuelve ese valor
print(espanol_a_ingles.setdefault('azul','Sin traducción')) # si no existe el key, lo crea y los setea al valor default (2° argumento)

x ={0: 'cero', 1: 'uno'}
y = x.copy()          #shallow copy
y
z = x.deepcopy()      #deep copy
h = {1: 'Uno', 2: 'Dos'}
x.update(h)           # actualiza a x con los pares key-values de h

matrix = [[3, 0, -2, 11],[0, 9, 0 , 0],[0, 7, 0, 0],[0, 0, 0, -5]]    # cada elemento representa un fila
elemento = matrix[2][1]   ## matrix[file][columna], en este caso nos arroja 7

matrix = {(0, 0): 3, (0, 2): -2, (0, 3): 11, (1, 2): 9, (2, 2): 7, (3, 3): -5}
# if (fila, columna) in matrix:
#   elemento = matrix[(fila, columna)]
# else:
#   elemento = 0
elemento = matrix.get((fila, columna), 0)   # mejor usar el metodo de diccionarios "get"

cache_calculo={}
def Calculando(a, b, c):
  if (a, b, c) in cache_calculo:
    return cache_calculo[(a, b, c)]
  else:
    ## operaciones para devolver resultado
    cache_calculo[(a, b, c)] = resultado
    return resultado
