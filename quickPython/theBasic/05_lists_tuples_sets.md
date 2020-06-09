# Lists, Tuples, Sets
[Referencia de código en python con comentarios](05_lists_tuples_sets.py)

## Listas
Es una colección de objetos ordenados.

```python
x = [1, "dos", 3]           # Creamos una lista
x = [4, [5, 6], "siete"]    # Los elementos pueden ser cualquier objeto de python
len(x)                      # len(): fc que cuenta el número de elementos de la lista
len(x[1])                   # Cuenta los elementos del objeto en la posición 1 de la lista x
```
No es necesario declarar la variable  antes de usarla ni definir su tamaño, está se expande o contrae dependiendo como la utilicemos.

## Indices de listas
Los indices indican la posición de los elementos en una lista. Estos se númeran del elemento 0 en adelante.

Los indices pueden ser `negativos` indicando que se empiezan a contar los elementos desde el dinal de la lista, pero la cuenta empieza en -1, indicando el ultimo elemento.

| Indices/Posición | "primero" | "segundo" | "tercero" | "cuarto" |
| ---------------- | --------- | --------- | --------- | -------- |
| positivos        | 0         | 1         | 2         | 3        |
| negativos        | -4        | -3        | -2        | -3       |

`Slicing` es la manera en que podemos extraer o asignar una sublista en una sola sentencia.

```python
x = [ "uno", "dos" , "tres", "cuatro"]
x[1:3]          # Muestra los elementos de indice 1 al 2 -> ["dos", "tres"]
x[-3:-1]        # ["dos","tres"]
x[:3]           # ["uno", "dos", "tres"]
x[2:]           # ["tres", "cuatro"]
x[:]            # todos los elementos de la lista. Usado para realizar copia de lista y no afectar la original.
```
En el "slicing" x[:3] al no indicar el primer index, es pedir desde el elemento 0.

Si no indicamos el segundo index, es pedir que devuelva hasta el ultimo elemento de la lista.

## Modificando listas
Con la notación con index podemos modificar un elemento de la lista o extraer elementos de ella como ya vimos.

```python
x = [1, 2, 3, 4]
x[2] = "tres"           # Asignamos el string "tres" a el elemento de indice 2 de la lista
```

Usando la notación "slice" podemos modificar/agregar/remover elementos de la lista x.

```python
x = [1, 2, 3, 4]
x[len(x):] = [5, 6, 7]  # Agregamos elementos al "final" de la lista x utilizando notación "slice"
x.extend([5, 6, 7])     # Hace lo mismo que la linea anteior
x = [1, 2, ] + [4, 5]   # "+" concatena 2 listas.

x.append("elemento")    # "append" es una fc que permite agregar "un" elemento la lista.
x.append([2, 3, 4])     # Agrega a x toda la lista, como un solo elemento [1, 2, 3, 4, [2, 3, 4]]
x[:0] = [-1, 0]         # Agregamos elementos al "inicio" de la lista

x.insert(3, "inicio")   # Insertar el elemento "inicio" en la posición "3" de la lista x. Insert maneja "indices negaticos" también.
x[3:3] = ["incio"]  # Insertamos elementos en una lista con el metodo "slice". No soporta indices negativos.

del x[1:-1]             # "del" es el método preferible para borrar listas o slices.
x[1:-1] = []            # Elimina los elementos de indice 1 al -2.

x.remove(6)             # Elimina de una lista la primera instancia de un valor dado. Si no encuentra el valor devuelve un error
                        # Antes de usar remove, podemos usar "in" para verificar que el elemento exista en la lista o hacer un catch para el error

x.reverse()             # Invierte el orden de los elementos en una lista.
```

## Ordenar listas
```python
x = [ 7, 2, 5, 1]
y = x[:]                # Copiamos la lista original
y.sort()            # sort() reordena la lista
```

Los elementos de la lista deben ser del mismo tipo para ser ordenados, la función nos indicará error si no es así.

Para mantener la lista original podemos hacer una copia, como vemos en el código anterior, o utlizamos `sorted()`.

Los elementos son organizados en orden lexicográfico.

### Ordanamiento personalizado

```python
def cuenta_letras(palabra):
  return len(palabra)

my_list = ["Hola","Python","en","progreso"]
my_list.sort(key=cuenta_letras)     # Ordenar palabras según la cantidad de caracteres del string
my_list
```
[Ejemplo](ch05/ordenando.py)

Es mejor el desempeño de "sort" sin personalizar y combinandolo con otros métodos.

Por ejemplo sort tiene  un parametro `reverse" que al darle el valor de `True` invierte la lista, pero este ordenamiento personalizado es más lento que si usamos la función sort() y luego reverse().

```python
x = [1, 2, 3, 4, 5]
y = sorted(x,reverse=True)          # sorted() devuelve una lista ordenada respecto de "x" y la almacenamos en "y". "x" no es modificada
```

### Operador "in"
Con el operador `in` podemos chequear si un valor se encuentra en una lista, retornando un valor booleano (True/False). De igual manera para `not in`.

```python
10 in [3, 5, 2, 10]     # devuelve "True"
4 not in [3, 5, 2, 10]  # devuelve "True"
```

### Inicializando listas con el operador "*"
Hay situaciones en donde creamos lista que son de tamaño fijo, de tal manera de no generar un overhead de moverla en memoria agregar elementos en ella usando por ejemplo "append", podemos crearla con el tamaño deseado.

```python
x = [None] * 4      # lista con 4 elementos que apuntan al objeto None
y = [1, 2] * 4      # [1, 2, 1, 2, 1, 2, 1, 2] -> repite los elementos las veces que le indiquemos
```

### Mínimos y máximos en una lista
Generalmente se utiliza en listas que contienen números, pero se puede usar con cualquier tipo de objetos, que contengan elementos del mismo tipo.

```python
min([4, 2, 6, 7])       # devulve elemento de menor valor -> 2
max ([3, 7, "perro"])   # devuelve ERROR por contener diferentes tipós de elementos.
```

### Buscando el indice de un elemento
`index()` devuelve la posición en que se encuentra un valor en una lista y si no lo encuentra devuelve ERROR.

```python
x = [1 , 43 ,"perro", 39]
x.index(43)                 # devuelve la posición "1"
x.index(2)                  # ERROR
```

### Contando ocurrencias
```python
x = [1, 2, 1, 2, 2, 4, 2, 6]
x.count(2)                      # 4
```

## Listas anidadas y "deep copies"
Podemos representar matrices bidimensionales mediante `listas anidades`.

```python 
 x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 x[0][2]                                # 3
 x[1]                                   # [4, 5, 6]
```

Como elementos de una lista pueden ser objetos, que pueden estar referenciado desde otra variable, debemos tener en cuenta al modificarlas cambiamos el valor de las variables que las referencian.

```python
x = ["uno"]
y = [x, 2]          # [["uno"], 2]
x[0] = 1            # modifico un elemento de la lista "x"
y                   # [[1], 2]  -> Vemos como se refleja la modificación de "x" al ser un elemento de "y"
```

Al relizar copias de lista debemos tener en cuenta lo anterior, de tal manera que surge la forma de hacer dos tipos de copias:

```python
original = [["cero"], 1]
""" shallow copy """
shallow = original[:]           # Copia elemento a elemento. Pero el elemento "0" es un puntero a otra lista, por lo que pasará lo que vimos anteriormente.
""" Deep copy """
import copy
deep = copy.deepcopy(original)  # Crea elemento a elemento copias distintas de "original". Si modifico original[0][0] no se refleja en "depp"
```

## Tuplas
Son estructuras similares a las listas, una secuencia de valores asigandas a una variable, pero `inmutables`.

Esta se pueden utilizar como indice en los `diccionarios`

```python
x = ('a', 'b', 'c')     # Declaración de una tupla
""" Los métodos como len, count, min, max, etc., pueden ser utilizados.
x + x                   # ('a', 'b', 'c', 'a', 'b', 'c')
x * 3                   # devuelve una tupla con los elementos de x repetidos tres veces
y = (1 + 2,)            # Para indicar que es una tupla de un elemento, necesitamos la coma del final, despues del elemento de indice 0
```

Si uno de los elemento de una tupla apunta a una lista, está si se puede modificar.

### Packing and unpacking tuples
```python
(a, b, c, d) = (1, 2, 3, 4)     # Asignacion de valores a las variables que contine una tupla
a, b, c, d = 1, 2, 3, 4         # Se puede hacer este tipo de asignación sin los parentesis
x, y = y, x                     # Realiza un swap de valores entre variables, sin necesidad de crear un tercera
var = (1, 2, 3, 4)
a, b, *c = var                  # Copia cada elemento de var en las varibles, pero la marcada con * absorbe aquellas que no pueden asignarse a una variable.
a, *b, c = var                  # a=1, b=[2, 3], c=4
a, b, c, d, *e                  # a=1, b=2, c=3, d=4, e=[]
```

### Convertir lista a tuplas y viceversa
```python
list(tuple_var)
tuple(list_var)
list("hola")        # Descompone cada caracter en un elemento de una lista -> ['h','o','l','a']
```
Cualquier secuencia en python puede ser tratada como una tupla o lista, como vemos en el último comando.

## Sets (conjuntos)
Es una colección de objetos desordenados, donde la `unicidad` de cada **objeto** en el conjunto es lo importante.

Cada objeto que lo compone debe ser `Hashable` e `Inmutable` (int, floats, strings y tuples). 
```python
x = set ([1, 5 ,4 , 3, 5, 1])   # Se puede crear un set a partir de cualquier secuencia.
print(x)                        # {1, 3, 4, 5} -> Se remueven los duplicados en la lista inicial (unicidad)
x.add(6)                        # add(elemento): agraga un elemento al "set"
x.remove(1)                     # remove(elemento): elimina el elemento del "set"
5 in x                          # in: verifica la existencia de un elemento en el "set"
y = set([1, 7, 5, 2])           # Declaramos un nuevo "set"
x | y                           # |: Unión de los conjuntos-> {1, 2, 3, 4, 5, 7}
x & y                           # &: Intersección entre conjuntos -> {1, 5}
x, y                            # tupla de los conjuntos "x" e "y"
x ^ y                           # ^ Diferencia simétrica entre conjuntos (exceptua los elementos que se interceptan de los conjuntos)
```
Como los "sets" no son "hashable" ni "inmutables", no pueden ser elementos de otro "set".

### Frozensets
Similar los anteriores, pero estos NO pueden ser modificados una vez creados. Esto permite que puedan ser elementos de otro "set".

```python
z = frozenset(y)
```

## [Ejemplo de lo visto](ch05/lab_temp.py)
