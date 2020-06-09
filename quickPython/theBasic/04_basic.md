# Lo Básico en Python

## Indentación y bloques de structuras.
En python usamos los `espacios` e indentación parra detereminar los bloques de las estructuras.

```python
n=5
while n > 0:
  n -=1         # si  la linea no estuviera indentada no pertenecería al loop while
```

## Comentarios
El simbolo `#` nos indica el comienzo de un comentario, de tal manera que no es ejecutada. La excepción es cuando se encuentra dentro de un **"string"**.

```python
# Este es un comentario al inicio
n=4     ## comentario en la misma linea de código
coment="#En este string si vemos el simbolo"
```

## Variables y asignaciones
Las variables se crean automaticamente en con su primera asignación.

```python
x = 5       # Asignamos el valor 5 a la variable x
```

Las variales son `tags` o `labels` que apuntan un **objeto** en el namespace del interprete de python. De esta manera un objeto puede estar referenciado por diferentes variables, pero si cambia el objeto, este cambio se refleja en *todas* las variables que lo referenciaban.

```python
a = [1, 2, 3]       # creamos una lista
b = a
c = b
b[1] = 5
print(a, b, c)      # imprime tres veces [1, 5, 3]
```

En los valores constantes o inmutables el comportamiento varía, ya que la variable al reasignarla no puede modificar el objeto, se reasigna a un nuevo objeto.

Las variables pueden apuntar a cualquier tipo de objeto.

```python
x="un string"
print(x)
x = 5
print(x)
del x       # borramos la varible
```

Las variables son `case-sensitive` y pueden contener cualquier caracter alfanumerico y guiones bajos.

## Expresiones
Python soporta expresiones aritméticas.
```python
x, y = 3, 4         # Otra forma de asignar valores a variables.
z = (x + y) / 2
z = (x + y) // 2    # retorna el decimal truncado
```

## Strings
Indica los string mediante el uso de comillas simples o dobles, indistintamente.

Para representar caracteres espciales usamos backslash para escaparlos y lograr su representación: \n (salto de linea), \t (tabulador, \" (comillas dobles), etc.

Las triples comillas simples o dobles, nos brindan la ventaja de no tener que escapar los caracteres
x = """ Este es un texto
que puede representar 'caracteres' especiales
sin necesidad de escparlos"""

## Numeros
Python maneja 4 tipos de números:
  - `Enteros`: su tamaño está dado por los recursos de la computadora.
  - `Flotantes`: Pueden ser escrito como decimal o notación científica. Tamaño máximo de 64-bit.
  - `Complejos`
  - `Booleanos`: True (1) o False (0).

```python
>>> 9 / 2
4.5
>>> 9 // 2      # Trunca la división mostrando la parte entera
4
>>> int(2.3e2)  # int() Transforma el float devuelto por la notación científica a entero
230
float(9 / 3)    # transformamos el número entero en flotante
3.0
```

### Funcions númericas de python (build-in)
abs , divmod, float, hex, int, max, min, oct, pow, round

### Funciones numéricas avanzadas
Podemos usar el `módulo math` para ralizar operaciones más complejas

```python
from math import *      # Importamos las funciones del módulo
```

**Funciones**: acos, asin, atan, cos, ceil, exp, e, hypot, log, log10,...

En la documentación están todas las funciones con la que cuenta.

### Numeric computation
[NumPy](www.scipy.org) es una extensión que permite implementar operaciones avanzadas de computación, como Transdormadas Rápida de Fourier, matrices y más.

## El valor "None"
Es un `objeto especial simple` que nos permite presentar un **valor vacio**.
Al ejecutarse una función que no retorna un valor, por defecto esta devuelve un valor `None`.

Este es un valor que podemos usar como "placeholder" en una estructura de datos.

`None` tiene una sola instancia en todo el sistema Python, de tal manera que cualquier referencia al mismo apuntan al mismo objeto.

## Obteniendo entradas (inputs) del usuario
```python
""" Este es un programa para sacar el factorial de un número dado"""
# El input devulve un valor **string** por defecto. En este caso lo convertimos a int
n = int(input("Ingrese el número a factorizar"))
r = 1
while n > 0:
  r *= n
  n -= 1
print (r)
```

##[Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
En link nos lleva a una guí de las convenciones que deberíamos usar para realizar un código en python.
- Por ejemplo: `my_func`, `my_var`, `my_module`, `MyClass`, `CONST_NAMES`
