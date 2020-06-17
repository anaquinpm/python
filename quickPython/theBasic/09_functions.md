# Funciones
## Definición básica de función
```Python
def name (parametro1, parametro2, ...):
  """ Descripción de la función"""      # Opcional: documentation string or docstring
  body
```
```Python
def factorial(n):
  """ Retorna el Factorial de un número dado """
  r = 1
  while n > 0:
    r *= n
    n -= 1
  return r          # Valor retornado por la función

print(factorial(int(input("Ingrese un número"))))
```

El `docstring` tiene la función de describir que realiza la función y que parametros toma.

En **Python** al ejecutarse **return arg** el valor `arg` es devuelto saliendo de la función. Aunque la función *no* retorne un **valor explicitamente**, automaticamente esta retorna el valor especial `None`.

## Opciones de parametros en funciones
### Parametros posicionales
Al definir la función le damos los nombres de variable para cada parametro que recibirá. La función al ser llamada asigna según la `posición` el valor a cada variable de los parametros de la función.
```Python
""" Potencia de un número, según su base y potencia """
def potencias(x, y):
  r = 1
  while y > 0:
    r *= x
    y -=1
  return r

print(potencias(3, 3))
```
[code](09_functions.py)

Es necesario en estos métodos que la cantidad de parametros al llamarlos coincida con los definidos en la función.

- **Default Values**: podemos definir valores por defecto en los parametros en que definimos la función, los cuales se asignaran si al llamar a la misma no le otorgamos un valor para esa posición. Los valores predifinidos tienen que ser los ultimos declarados en la función.
```Python
def func(arg1, arg2, arg3=dafault3, arg4=default4.......):
```
```Python
""" Potencia de un número, según su base y potencia. Si no se pasa el segundo parametro se toma potencia 2 """
def potencias(x, y=2):
  r = 1
  while y > 0:
    r *= x
    y -=1
  return r

print(potencias(3,4))
```
[code](09_functions.py)

### Pasando argumentos por nombre de parámetro ("Key-word passing")
Al llamar una función se puede definir que valor recibirá cada parámetro. En este caso no se tiene en cuenta el orden de los parámetros.
```Python
potencias(y=3, x=2)
```

`Key-word passing` y `Default value` combinadas son una herramienta poderosa para procesar información usando una función con muchos argumentos y que tienen deafult values.
```Python
def fileinfo(size=False, create_date=false, mod_date=false, ...)
  Body
  return fileinfostructure

fileinfo = list_file_info(size=True, mod_date=True)
```

### Número de argumentos variables.
#### Indefinido números de argumentos posicionales
Los parámetros recibidos por la función se **asignan** a una `tupla`,la cual luego se puede recorrer para procesar.

```Python
""" Determinar el número máximo de una lista de números"""
def maximo(*numeros):
  if len(numeros)==0:
    return None
  else:
    maxnum = numeros[0]
    for n in numeros[1:]:
      if n > maxnum:
        maxnum = n
    return maxnum

print(maximo(6, 2, 3, -9, 24))
```
[code](09_functions.py)

#### Indefinido números de argumentos pasados por "Keyword"
Al pasar varios argumentos con sus respectivos `keywords`, si estos no están definidos en la función se asignan a un diccionario al cual podemos recorrer cada valor usando su keyword.
```Python
def funcion(x, y , **otros):
  print(f"x: {x}, y: {y}, keys en 'otros': {list(otros.keys())}")

funcion(3, y=2, foo=3, bar=4)
```
[code](09_functions.py)

### Mezclar técnicas para pasar argumentos
Es posible mezclar las técnicas de paso de argumentos, pero estas tienen que relizarse siguiendo un orden espcifico para no tener problemas.
- Orden:
  - `posicional arguments`
  - `named arguments`
  - Indefinite positional argument with a single `*`
  - Indefinite keyword argument with `**`

## Objetos mutables como argumentos
Los arguemtos en una función son pasados por referencia a un objeto. En `objetos inmutables` (string, numeros, tuplas) esto no es un problema ya que no tienen efectos fuera de la función. Pero si son `objetos mutables` (listas, diccionarios, instancias de clases) cualquier modificación en el objeto se ve reflajada fuera de la función.

## Variables locales, no locales y globales
- **Variable local**: las variables declaradas dentro de una función solo pueden ser alcanzadas hasta que termine la ejecución de dicha función.
- **Variable no local**: esta referencia a una variable que fue declarada en el bloque superior del cual estamos realizando un proceso y podemos acceder a ella mediante la sentencia `nonlocal`.
- **Variable global**: esta puede ser alcanzada desde cualquier punto del programa. Se puede transformar una variable local a una global declarándola nuevamente con la sentencia `global`.

[Ejemplo de los diferentes alcances de las variables](09_nonlocal.py)

## Asignar funciones a variables
Se puede asignar una función a una variable, como cualquier otro objeto de Python.
```Python
""" Convertidor de temperatura a grados Kelvin """
def f_to_kelvin(degrees_f):
  return 273.15 + (degrees_f - 32) * 5 / 9

def c_to_kelvin(degrees_c):
  return 273.15 + degrees_c

abs_temp = t_to_kelvin                            # Asignamos a una variable la función t_to_kelvin
print(abs_temp(32))
abs_temp = c_to_kelvin
print(abs_temp(0))

t = {'FtoK': f_to_kelvin, 'CtoK': c_to_kelvin}    # Asignamos a un diccionario las funciones
print(t['FtoK'](32))
```
[code](09_functions.py)

## Lambda expressions
Son pequeñas funciones que se pueden definir en una linea.
```Python
lambda parameter1, parameter2, .......: expresion
```

Podemos definir el conversor de temperaturas anterior de la siguiente manera:

```Python
temp = {'FtoK': lambda deg_f: 273.15 + (deg_f - 32) * 5 / 9, 'CtoF': lambda deg_c: 273.15 + deg_c}
print(temp['FtoK'](32))
```
[code](09_functions.py)

## Generador de funciones
Es un tipo de _función especial_ que se utiliza para definir tus propios iteradores. _Retorna_ en cada iteracción el valor de la variable especificada por la sentencia `yield`. Los valores de las **variables locales** son accesibles en la siguiente llamada.

El generador se detiene si no tiene más iteraciones, no tiene valor a retornar o cuando termina la función.

```Python
def cuatro():
  x = 0
  while x < 4:    ## Limita las veces que se ejecuta el generador
    print("en el generador, x= ", x)
    yield x
    x +=1

for i in cuatro():
  print(i)
```
[code](09_functions.py)

- En **Python 3.3** `yield from` delega el mecanismo generador a otro subgenerador.
```Python
def subgen(x):
  for i in range(x):
    yield i

def gen(y):
  yield from subgen(y)

for q in gen(6):
  print (q)
```
[code](09_functions.py)

Podemos usar `in` para ver dentro del generador la serie que produce
```Python
5 in cuatro()
```

## Decorators
La función "decorator" toma como parametro otra función y modifica su comportamiento.
- Usar "decorators" implica dos partes:
  - definir la función que va a encapsular (or decorating) otras funciones
  - usar "@" justo antes de declarar la función a encapsular.

```Python
## Decorators
def decorate(func):
  print(" in the function decorate, decorating", func.__name__) # Imprime el nombre de la fc que está encapsulando
  def wrapper_func(*args):                       # Usualmente se usa el prefijo wrapper_ para la inner fc.
    print("Executing", func.__name__)
    return func(*args)
  return wrapper_func                            # Retorna la función encapsulada

@decorate                                        # Definimos que la siguiente función que va a ser encapsulada por "decorate()"
def myfunction(parameter):
  print(parameter)

myfunction("hello")
```
[Ejemplo de función decorate](09_decorator.py)
