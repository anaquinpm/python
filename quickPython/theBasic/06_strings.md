# Strings
[Code](06_strings.py)

## Strings como secuencia de caracteres
Es posible extraer caracteres o substrings de un string usando "index" o la notación "slice".

```python
x = "Hola\n"
x[0]          # "H"
x[:-1]        # "Hola" -> Util cuando leemos lineas de un archivo y tienen "\n"
x[1:-1]       # "ola"
len(x)        # "5"
```
Python tiene métodos más especificos para trabajar con strings, pero es una forma de ilustrar la posibilidad de ser tratados como una secuencia de datos cualquiera.

La única diferencia entre una lista y un string, es que los strings no pueden ser modificados.

```python
x = "Hola\n"
x = x[:-1]        # Como NO se pueden modificar los strings, tenemos que crear uno nuevo.
```

## Operaciones básicas con strings
```python
# Concatenar
x = "Hola" + "mundo"    # "Hola mundo"
4 * "x"                 # "xxxx" -> Multiplicamos el string "x"
```

## Caracteres especiales y secuencias de escape.
Podemos representar `caracteres especiales` mediante `secuencias de escapes`, las cuales empiezan con un "backlash (\)", tales como el salto de página que ya vimos en ejemplos anteriores (\n).

### Secuencias de escape básicas
Con los **strings** se puede utilizar secuencias de escapes formadas por `dos caracteres`.
| Secuencia | Representación                 |
| --------- | ------------------------------ |
| \'        | Comilla simple                 |
| \"        | Comillas dobles                |
| \a        | Bell character (causa un beep) |
| \b        | Backspace                      |
| \\        | Backslash                      |
| \n        | Salto de linea                 |
| \t        | Tab                            |
| \v        | Tab vertical                   |

### Secuencias de escapes numéricas y Unicode
Podemos representar cualquier caracter ASCII en base `octal` o `hexadecimal`
```python
x = "k"
print("\153")   # representación octal
print("\x6B")   # representación Hexadecimal
```

En Python3 todas los string son `Unicode`, de tal manera que podemos escapar sus caracteres mediante su número o nombre Unicode.

```python
x = '\N{LATIN SMALL LETTER A}'    # "a"
print('\u00E1')                   # "á"
```

* Buscar caracteres ASCII y UNICODE

### Diferencia entre "print" o "evaluar una expresión"
Esto lo podemos ver cuando estamos en una seción interactiva de Python y colocamos el nombre de una variable, en este caso, un string con una secuencia de escape

```python
x = " Hola mundo\n"
x                     # "Hola mundo\n" -> devuelve el string completo sin realizar ninguna conversión sobre los caracteres especiales
print(x)              # "Holas Mundo" -> Devuelve el string pero realizando la conversión del caracter de salto de línea
```

## String Methods
La clase string en Python tiene varios métodos especificos para este tipo de dato, los cuales la eredan al momento de ser creados.

Para utilizar los metodos les anteponemos el objeto string sobre los que vamos a trabajar, lo cuales no se veran modificados.

### Split and Join
Estos métodos son el inverso uno del otro.
  - `Split`: retorna una lista de substrings respecto de un string. Se puede indicar el separador, sino especifica se toma los espacios como tal.
  - `Join`: toma una lista como parametro y la une en un solo string.

Antes utilizamos para concatenar strings el simbolo `"+"`, este es útil en ciertos casos, pero no performa bien debido a que cada vez que se procesa el simbolo se crea un nuevo objeto string.

```python
"-".join(["join","coloca","el","separador","indicado","entre","palabras"])
palabras.split("-")           # Indicamos el separador para procesar el objeto string.
palabras.split(None,2)        # Se puede indicar los "n+1" grupos que queremos crear.
                              # "None" indica que usa los espaciós y nos deja usar el 2° argumento.
```
#### Ejemplo

```python
""" Cambia espacios por guiones """
x = "Cambiamos los espacios de este texto por guines"

"-".join(x.split())     # split() devuelve una lista de las palabras en "x" y 
                        # join() la toma como argumento para colocar su separador
```

### Strings a Números
Podemos convertir strings a números mediante `int` y `float`. Int() puede usar un segundo parametro el cual indica la base numérica de string.
```python
float('123.456')
int('123')
int('1000', 8)      # "1000" en base octal
int('1000', 2)      # "1000" en base binaria
int('ff', 16)       # "1000" en base hexadecimal
```

### Espacios en blanco
Según el OS en que corramos pueden variar los caracteres de espacios en blanco.

```python
import string
string.whitespace		# ' \t\n\r\x0b\x0c' -> Espacios en blanco considerados por el OS.
```

Podemos eliminar los espacios en blanco que se encuentran delante o detras de una cadena de caracteres con los siguiente métodos:
 - `strip`: Devuelve la cadena oreiginal sin los espacios al inicio y filnal de la misma
 - `lstrip`: Cadena sin espacios adelante.
 - `rstrip`: Cadena sin espacios al final.

```python
x = "\t     Hola, Mundo \n\r"
x.strip()               # "Hola, Mundo"
y ="www.mundo.com"
y.strip("w.")           # "mundo.com" -> Como argumento de la función podemos indicar los caracteres a remover.
```

## Busqueda de Strings

`find` busca un **substring** dentro de un *string* y devuelve el **indice** de su primer ocurrencia o **-1** cuando no la encuentra.
```python
""" string.find(substring[, start][, end] """
x = "Pollo"
x.find("ll")      # "2"
x.count("ll")     # "1" -> cantidad de ocurrencias del substring
x.find("o",2)     # "4" -> busca desde el indice 2 y encuentra la primer ocurrencia de "o" en el indice "4"
```

A estas `funciones básicas de busqueda` se le suman: **rfind, index y rindex**

La diferencia entre las funciones `find` e `index` es que index al no encontrar el substring en su busqueda devuelve una *excepción* "ValueError"

Los métodos `stratswith` y `endswith` buscan un substring al *incio* o *final* de un string. Devuelven como resultado **True** o **False**.
```python
x = "pollo"
x.startswith("po")      # "True"
x.endswith("le")        # "False"
x.endswith(("lo","l"))  # "true" -> Usa como parametro un tupla. Si algún elemento de la tupla ocurre, devuelve True
```

### Modificando Strings
Los strings no son modificables, pero podemos obtener cadenas a partir de ellos mediante métodos.

```python
x = "pollo"
x.replace("ll","y")     # "poyo" -> replace() retorna otro string remplazando un substring por otro que indiquemos

""" Podemos realizar remplazo de caracteres usando una tabla creada por nosotros y aplicandola a nuestro string ""
x = "( -A ![number])"               # string de un lenguaje imaginario
tabla = x.maketrans("-!","*^")      # Creamos la tabla para cambiar cada caracter. Las posiciones en cada parametro se corresponden en el orden
x.translate(tabla)                  # Trasladamos el texto según la tabla creada.
```

Otros métodos :
  - lower()
  - upper()
  - capitalize()
  - title()
  - expandtabs(tabsize=4)
  - zfill()
  - rjust()
  - ljust()

### Modificando strings con manipulación de listas
Otra posibilidad de trabajar con los strings es haciendo "listas" a partir de ellos y utilizando los métodos para tal.
```python
x = "Cambiando tipo de dato"
nuevaLista = list(x)
parrafo = "".join(nuevaListai[8:0])   # Unimos los elementos de la lista sin agregar separadores.
```
Esta forma de modificar no es optima para trabajar grandes cadenas de strings, por lo que estamos creando nuevos objetos para poder modificarlos.

### Objetos a strings
repr() nos permite mostrar objetos como una representación de string.

```python
x = ['hola',' Mundo']
'objeto ' + repr(x)           # "objeto ['hola',' Mundo']" -> Como es un string podemos concatenarlo
```

## Format method
Podemos dar formato mediante el método `format`.
```python
""" Dos formas de ingresar parametro son por posición y nombre """
"El Asado es la {0} de los {1}".format("comida","Dioses")     # El n° en las llaves simples indican la posición del parametro por el que se va remplazar
"El {comida} es la comida de los {user[0]}".format(comida="asado",user=["Dioses","hombre","otros"])   # podemos usar nombres en los parametros
""" Format specifiers """
"El {0:10} es la comida de los Dioses".format("Asado")        # En las llaves también podemos especificar la posición del dato y el tamaño del campo
"El {comida:{width}} es la comida de los Dioses".format(comida="Asado", width=10)   # Lo mismo a lo anterior pero con nombre de parametros
"{0:&>10} es la comida de los Dioses".format("Asado")         #"&" es el caracterer con lo que vamos a "justificar"(<>) los espacios en blanco del campo a remplazar
```

## Interpolación de strings (f-strings) -> [Documentación python PEP-498](https://www.python.org/dev/peps/pep-0498/)
Es una forma de incluir valores de expresiones python dentro de un "string literal"

Los `f-strings` tienen menos **overhead** que los string producidos con el método "format".
```python
pi = 3.1415
mensaje = f"pi es {pi:{10}.{3}}"
print(mensaje)
```

## Bytes object
Secuencia de enteros con valores de 0 a 256. Utiles al manipular información en formato binario.
```python
unicode_a_with_acute = "\N{LATIN SMALL LETTER A WITH ACUTE}"    # Caracter unicode
unicode_a_with_acute
xb = unicode_a_with_acute.encode()      # El caracter unicode lo transformo en un objeto de 2 bytes
xb.decode()                             # Decodifico el objeto de bytes al string original
```
