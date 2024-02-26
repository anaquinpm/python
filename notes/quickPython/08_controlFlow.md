# Control flow

## While loop

```Python
while condition:
  body         # lineas de código
else:          # opcional y usualmente no utilizada
  post-code    # lineas de código
```

`Condition` es una expesión booleana que mientras sea **True** itera sobre el `body` hasta que resulte **False** y ejecute el código en `else`.

Los niveles en la indentación indican como los bloques de código se van a ejecutar.

En el **body** podemos usar la sentencias especiales:

- `Break`: termina el loop y salta el **else** también.
- `Continue`: pasa a la siguiente iteración del loop.

## Sentencia If-Else-Else

```Python
if condition1:
  body1
elif condition2:
  pass
else:
  body3
```

Hay situaciones especiales en donde en el body no necesitamos hacer nada, pero es necesaria una línea como minimo en él, por lo que usamos la sentencia `pass`

### Python no tiene sentencia Switch

Podemos usar `if anidados` para tal caso o un `diccionario de funciones`

```Python
##---------Diccionario de funciones para utilizar como switch
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
dicc_fc[x]()  # ejecuta la función a la que apunta el diccionario
```

[code](08_controlFlow.py)

## For loop

Este obtiene los valores de cualquier objeto iterable (valores secuenciales).

```Python
for item in sequence:
  body
else:                     # Raramente usada
  post-code
```

Podemos usar sentencia `Continue` y `Break` como ya vimos.

### Funcion **range**

Produce una secuencia de números según los aparametros que le indiquemos:

```python
 range(n) = 0, 1, 2 ... n-2, n-1
 range([start,] stop [, step])
```

Recorrer una secuencia de valores utilizando for y range.

```Python
x = [1 , -8, 2, -3, 9, 4]
for n in range(len(x)):
  if x[n]>0:
    print("Números positivos en el index", n)
```

[code](08_controlFlow.py)

`Range` produce un objeto que genera enteros a demanda, aunque pareciera que genera una lista. Esto es util cuando tenemos que generar una secuencia muy grande, `performando` mucho más que creando una lista, ya que no esta almacenado en memoria la lista con los enteros.

Podemos generar una secuencia regresiva colocando [range] con un valor negativo

```Python
list(range(8, 3, -2))   #List fuerza a verlo como una lista en este Ejemplo y no se usa al programar
```

[code](08_controlFlow.py)

### Tuple unpacking

Es una forma más simple y limpia de asignar valores de una secuencia de tuplas.

```Python
list = [(1, 2), (3, 4), (5, 6)]
resultado = 0
for x, y in list:
  resultado = resultado + x * y
```

[code](08_controlFlow.py)

### Función enumarate

Combinando "tuple unpaking" con la fc `enumarete` podemos recorrer el index y valor a la vez.
> enumerate(x) devuelve la tupla (index, item)

```Python
x = [1 , -8, 2, -3, 9, 4]
for i, v in enumerate(x):
  if v > 0:
    print(f"Número positivo en el index {i}")
```

[code](08_controlFlow.py)

El código realiza lo mismo que el ejemplo con range, pero este es mas limpio y facil de entender.

### Función zip

Combina 2 o más iterables creando tuplas hasta que llega a agotar el de menor tamaño.

```Python
x = [1, 2, 3, 4]
y = ["a", "b", "c"]
z = zip(x, y)
list(z)
```

[Repaso de if y loops](08_LoopsIf.py)

## List and dictionary comprehensions

Es una linea de código de un loop `for` que crea una nueva lista o diccionario de una secuencia.

```Python
new_list = [expresion1 for variable in old_list if expresion2]          # Lista
new_list = {expresion1:expresion2 for variable in list if expresion3}   # Diccionario

x = [1, 2, 3, 4]
x_cuadrado_list = [item * item for item in x if item > 2]         # Comprehensions en listas
x_cuadrado_dicc = {item: item * item for item in x if item > 2}   # Comprehensions en diccionarios
```

[code](08_controlFlow.py)

### Generador de expresiones

Este es similar a una `list comprehension`, pero este genera un ubjeto el cual depués lo podemos _iterar_ mediante un **loop for**.

- **Ventaja**: la lista no se genera en memoria, logrando poco overhead al procesar grandes listas.

```Python
x = [1 , 2 , 3, 4]
x_cuadrado = (item * item for item in x)    # x_cuadrado es un objeto
for valor in x_cuadrado:
  print(valor)
```

[code](08_controlFlow.py)

[**EJEMPLOS**](08_comprehensions.py)

## Sentencias, bloques e indentación

Vimos que python utiliza la indentación para definir los bloques de como se construye el control de flujo del programa que estamos escribiendo.
Hay casos especiales en donde podemos escribir varias sentencias en una misma linea.

```Python
x = 1; y = 2; z = 3
if x > 0 : y = 1; z = 10
else: y = -1
print(x, y, z)      # 1 1 10
```

Para no tener problemas es recomendable para indentar usar espacios y no tabs.

## Valores y expresiones booleanas

La mayoria de objetos en Python pueden ser usados en expresiones que retornen True o False

| data type  | False | True                  |
| ---------- | ----- | --------------------- |
| numeros    | 0     | cualquier otro número |
| string     | ""    | cualquier otra cadena |
| list       | []    | lista no vacía        |
| diccionary | {}    | diccionario no vacío  |
| set        | ()    | set no vacío          |
| None       | None  | nunca                 |

Hay otros tipos de objetos que pueden ser evaluados de la misma manera que no cubre la tabla, pero siguen el mismo criterio, son `False` cuando son **0** o estan **vacíos**.

### Comparaciones y operadores booleanos

- **Normal operators**: <, <=, >, >=, ==, !=
- **Secuencias** (list, tuples, strings, dictionaries): in, not in, is, is not.
- **Combinación de expresiones**: and, or, not

Los operadores `and` y `or` devuelven objetos. **And** devuelve el primer objeto Falso que evalua y **Or** devuelve el primer objeto True y para su ejecución.

- `==` y `!=` nos permite comparar el **contenido** de los _operandos_.
- `is` e `is not` evalua si los _operandos_ son los mismos **tipos de objetos.**

## [Ejemplo: Contar parrafos, palabras y caracteres](08_word_count.py)

```Python
#!/usr/bin/env python3
""" Leer un archivo y devolver el número de lineas, palabras y caracteres
    Similar al comando 'wc' de UNIX
"""
line_count, word_count, char_count = 0, 0, 0
with open('word_count.tst') as lines:
  for line in lines:
    line_count += 1
    words = line.split()
    word_count += len(words)
    char_count += len(line.strip(",.\t\n "))

print("El archivo tiene {0} lineas, {1} palabras, {2} caracteres".format(line_count, word_count, char_count))
```
