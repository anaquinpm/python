#Las listas son como los arreglos en C
## Asigno una lista de 3 elemento a x
x = [1, "two", [1, 2 ,3]] #los elementos pueden ser de cualquier tipo
len (x[2])   #"largo de la lista" en la posición 2 de la variable x
x[2]    # referencia a un elemento de la lista, tomando como posición 0 el primer elemento
x[-2]   #referencia desde el ultimo elemento de la lista x. Inicia de -1 la ultima posición
## Slicing
x[:-1]  # "Desde el comienzo de la lista" hasta el elemento -1
x[1:]   # desde el elemento 1 "Hasta el final de la lista"
y = x[:]   #copio todos los elemento de la lista a la variable "y"

# Modificando listas
## x_lista[index1:index2] = listb -> causa que los elementos de la "x_lista" 
## entre index1 y index2 sean remplazados por los elementos de la "listab"
y[len(y):] = [4, 5, 6]    #agrega elementos al final de la "x_lista"
x = [3, 5, 1, 9] + [2, 4, 8]    # concatenamos listas con "+"
## y.extend([4, 5, 6])   # idem a la linea anterior pero utilizando el metodo "extend"
y.append([4, 5, 6])   # agrega como ultimo "elemento" de la lista una "lista completa"
y[:0] = [-1, 0]     # agrega los elementos al inicio de la "x_lista"
y[1:-1] = []    # elimina/agrega elemento de x_lista
y.insert(0, "hola")   # inserte en la posición n de la lista, el elemento indicado -> parecido a y[n,n]=[element]
y
del y[0:2]    ## es preferido para borrar uno varios elementos de una lista
y
x.remove(1)   # elimina la primer aparicion del elemento indicado
x.reverse()   # invierte una lista
x

# Ordenar listas
y = x[:]    # copio la lista original a una variable, para mantener el orden original de elementos
y.sort()    # la fc sort() ordena los elementos de la variable "y". La fc tb ordena listas con elemntos string 
x = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
x.sort()
x

def compare_number_of_chars(string1):
  return len(string1)
word_list = ["Python", "is", "better", "than", "C"]
word_list.sort(key=compare_number_of_chars)   ## ordena segun el numero de letras de cada palabra en la lista
word_list
## Performa más el método sort sin customizar, pudiendo llegar a los mismos resutlados combinandola con otros métodos

3 in y    # verifico si 3 es uno de los elementos de la lista "y"
3 not in y  # verifico si 3 no es un elemento de la list "y"
y.index(1)    # retorna la "posición" del elemento en la lista -> podemos testear primero si el elemento a buscar está en la list mediante "in"

y = [None] * 4    # inicializamos la lista "y" con elementos vacios
y
y = [3, 1] * 2      # idem linea anterior, pero con elemento no vacios
y

min(x)      ## las listas en al aplicamos min y max, deben ser del mismo tipo de elementos (string|int)
max(y)
y.count(3)    # n° de ocurrencias del valor 3 dentro de la lista

# Nested lists and deep copies
m = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
m[0][1]
m[1]

# podemos relizar dos tipos de copias --> shallow and deep copies
original = [[0],1]
shallow = original[:]   ##copia elemento a elemento, pero el elemento "0" es un puntero a otra lista. Si modifico el elemento original[0][0] se refleja en "shallow"
import copy
deep = copy.deepcopy(original)  ## crea elemento a elemento copias diferentes a la original. Si modifico el elemento original[0][0] "NO" se refleja en "deep"

# Tuples -> similares a la listas, pero las tuplas son inmutables
x = ('a', 'b', 'c')
# podemos utilizar metodos con los que tratamos a las listas como len, max, min, in, x[:], etc
x + x
3 * x

x, y = 1 , 3    ## declaración de dos variables en una linea de código
(x+y)   ## simplemente suma los valores como una operación matemática
(x + y,)    ## con la coma indicamos que estamos creando un tupla con un elemento que es la suma de x+y
x, y = y, x   ## realiza un swap de valores entre las varibles sin tener que  recurrir a crear una variable más
x = (1, 2, 3, 4)
a, b, *c = x    ## copia la cada elemento de x en las varibles, pero la marcado con * absorbe aquellos que no puede asignar a una única variable
c
a, *b, c = x
b

## convert tuple and list
list (tuple_var)
tuple(list_var)
s = "Hola"
list(s)   ## con list podemos descomponer un string

# Sets: conjunto de objetos sin orden, donde la unicidad de cada objeto en el conjunto es lo importancia.
## los elementos que componen el conjunto deben ser Hashables e inmutables (int, floats, strings & tuples)
x = set([1, 3, 2, 3, 5, 6, 5])
x.add(9)
x.remove(1)
x
2 in x
y = set([3, 1, 5, 4, 7, 8, 9])
x | y     ## muestra los elementos combinados de los dos conjuntos (una operación OR)
x & y     ## operación AND entre conjutnos
x, y
x ^ y     ## diferencia simetricas entre conjuntos (exceptua los elementos que se interceptan de los conjuntos)

## Frozensets -> similares a los anteriores pero estos no pueden ser modificados una vez creados
z = frozenset(y)
z.add(6)
y.add(z)
y

s = set([1, 2, 5, 1, 0, 2, 3, 1, 1, (1, 2, 3)])