# Diccionarios (Dictionaries)
Son arrays **asociativos** o **maps** implementados con Hash Tables.

- Los `keys` del diccionario pueden ser cualquier objeto de Python (enteros, strings, etc) indicando donde podemos encontrar el valor buscado.
- `Almacena` cualquier tipo de objeto de Python.
- Los `valores` en el diccionario `NO` están implicitamente `ordenados` respecto de otros.
  - Si es importante el orden, podemos usar
    - `ordered dictionary`, el cual es una subclase del **modulo collections**
    - Otra estructura de datos (ej: lista) para explicitar el orden.

```python
y={}
y["cero"] = 3.14    ## Podemos crear arbitrariamente una posición
y[1] = 'Goodbye'
y[1] + ', Friend.'
y[2] = 2
y["cero"] * y[2]    
```

[code](07_Dictionaries.py)

Los diccionarios son una forma de mapear un conjunto de datos arbitrarios a otro asociado pero igualmente arbitrario conjunto de datos.

[Ejemplo: Ingresar nombre y edades de personas. Elegir el nombre de quien quiero saber la edad](07_name.py)

## Otras operaciones con diccionarios

Definir un diccionario como **par key-value**.

```python
espanol_a_ingles = {'rojo': 'red', 'verde': 'green', 'azul': 'blue'}
len(espanol_a_ingles)           # numero de elementos
list(espanol_a_ingles.keys())   # valores de las keys
list(espanol_a_ingles.values()) # obtener los valores
list(espanol_a_ingles.items())  # obtener los pares key-value
del espanol_a_ingles['azul']    # elimina un item
```
[code](07_Dictionaries.py)

**Listamos** los resultados de los metodos que aplicamos al diccionario, porque estos devuelven `views` que se comportan como **`secuencias`** que se _**actualizan dinamicamente**_ y quizas no es un comportamiento deseado, por ejemplo cuando estamos en un "_for_".

```python
'rojo' in espanol_a_ingles                                  # verificamos que el "key" exista. Retorna True/False
print(espanol_a_ingles.get('azul', 'Sin traducción'))       # si no existe el key devuelve 'None' por defecto, si tiene segundo argumento la fc. devuelve ese valor
print(espanol_a_ingles.setdefault('azul','Sin traducción')) # si no existe el key, lo crea y los setea al valor default (2° argumento)
```
[code](07_Dictionaries.py)

Podemos realizar copias de diccionarios de dos maneras diferentes

```python
x ={0: 'cero', 1: 'uno'}
y = x.copy()          #shallow copy
y
z = x.deepcopy()      #deep copy
h = {1: 'Uno', 2: 'Dos'}
x.update(h)           # actualiza a x con los pares key-values de h
```
[code](07_Dictionaries.py)

## Contando palabras

```python
## Contando palabras
parrafo = "Probando como hacemos con python para contar palabras"
ocurrencias={}
for palabra in parrafo.split():
  ocurrencias[palabra]= ocurrencias.get(palabra, 0) + 1
for palabra in ocurrencias:
  print("La palabra ", palabra, "ocurrio", ocurrencias[palabra], "veces en el parrafo")
```
[code](07_words.py)

Al ser común el contar palabras, en el modulo `collections` tenemos una clase `Counter`.

## ¿Que usar como 'Keys'
Puede usarce cualquier objeto `inmutable` y `hashable`.

| Python type | Inmutable | Hashable                        | Dictionary Key |
| ----------- | --------- | ------------------------------- | -------------- |
| int         | yes       | yes                             | yes            |
| float       | yes       | yes                             | yes            |
| boolean     | yes       | yes                             | yes            |
| complex     | yes       | yes                             | yes            |
| str         | yes       | yes                             | yes            |
| bytes       | yes       | yes                             | yes            |
| bytearray   | no        | no                              | no             |
| list        | no        | no                              | no             |
| tuple       | yes       | Sometimes(sin objetos mutables) | Sometimes      |
| set         | no        | no                              | no             |
| frozenset   | yes       | yes                             | yes            |
| dictionary  | no        | no                              | no             |

## Matrices dispersas
Podemos representar matrices por medio de una lista:
```Python
matrix = [[3, 0, -2, 11],[0, 9, 0 , 0],[0, 7, 0, 0],[0, 0, 0, -5]]    # cada elemento representa un fila
elemento = matrix[2][1]   ## matrix[file][columna], en este caso nos arroja 7
```
`Sparse matrices`: son aquellas donde solo se almacenan los elementos no nulos.

La representamos usando un diccionario con tuplas como keys.
```Python
matrix = {(0, 0): 3, (0, 2): -2, (0, 3): 11, (1, 2): 9, (2, 2): 7, (3, 3): -5}
# if (fila, columna) in matrix:
#   elemento = matrix[(fila, columna)]
# else:
#   elemento = 0
elemento = matrix.get((fila, columna), 0)   # mejor usar el metodo de diccionarios "get"
```
[code](07_Dictionaries.py)

Para trabajar con matrices también mirar `packete NumPy`

## Diccionarios como caches
Si tuvieramos una función que toma 3 argumentos para realizar un determinado calculo, podemos usar una matriz como cache para no realizar el mismo calculo reiteradas veces.

```Python
cache_calculo={}    # diccionario como variable global para almacenar resultados previos.
def Calculando(a, b, c):
  if (a, b, c) in cache_calculo:
    return cache_calculo[(a, b, c)]
  else:
    ## aquí van operaciones para devolver "resultado"
    cache_calculo[(a, b, c)] = resultado
    return resultado
```
[code](07_Dictionaries.py)