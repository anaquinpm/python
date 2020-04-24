# Modules and Scoping rules
## Que es un Modulo
Es un archivo que contiene código python. En este se definen un **conjunto** de `funciones` u ` objetos` _relacionados_. El nombre del modulo resume el tema de lo que contiene.

Los modulos pueden ser de código Pyton, compilados de C u archivos con objetos de C++.

Estos nos permiten hacer más manejable el código que estamos creando.

```Python
""" mymath - ejemplo de modulo"""
pi = 3.14159
def area(r):
  """ retorna el area de un circulo con radio r."""
  global pi
  return (pi * r **2)
```
[Código del módulo](mymath.py)

Cargamos el módulo en un IDE. 
```Python
import mymath     # Importamos el modulo
maymath.area(3)   # Llama a la función que está en el modulo
```
[Code](10_ModulesAndScopingRules.py)

La forma en que se llama a la función area anteponiendo el nombre del módulo se la refiere como "`qualification`" (clasificación), la cual nos permite diferenciar funciones de diferentes módulos con el mismos nombre. También podemos usar el atributo "pi" del modulo mymath (mymath.pi).

Para no tener que anteponer el nombre del módulo para usar "pi" hacemos
```Python
from mymath import pi
print(pi)
mymath.area (2)   # La fc area aún tiene que antepones el nombre del módulo
```

Hay veces en que estamos modificando un módulo y queremos probarlo, este no recarga las modificaciones al usar la función `reload` del módulo `importlib`
```Python
import mymath, importlib
importlib.reload(mymath)
```

## Import
Está sentencia tiene 3 diferentes formas:
  1. Busca el archivo del modulo para parsearlo y dejarlo disponible para su uso. Si no lo encuentra se genera un error.
  > import modulename"
  2. Exportar explicitamente objetos de un módulo para usarse sin anteponer el nombre.
  > from modulename import name1, name2, name3, ...
  3. Forma general:
  > form modulename import *
  `*` exporta todos los nombres del modulo. Hay que tener cuidado de como usamos esta forma ya que sin darnos cuenta podemos sobrescribir un nombre que se encuentra en más de 2 modulos, quedara accesible el ultimo en importar.

## Módulo Search path
La variable "path" nos indica donde busca los modulos python y en el orden que lo hace.
```Python
import sys    # modulo de llamadas al sistema
sys.path
```
La variable es una **lista** que python recorre para buscar el módulo especificado y al primero que satisfaga la busqueda para.

El primer elemento de `sys.path` es un string vacío. Este expresa que el primer lugar en buscar es el directorio actual.

### Módulos propios
Para asegurarse que los modulos a usar sean accesibles necesitamos:
1. Colocar los módulos donde **normalmente Python los busca**. Esta no es recomendable porque estos directorios están destinados a códigos propios de la instalación actual y pueden ser borrados en cualquier otra instalación.
2. Colocar los módulos usados por el programa en el **mismo directorio del programa**. Buena para módulos desarrollados para dicho programa.
3. Crear **uno o varios directorios** para colocar los módulos y modificar el `sys.path` para que Python lo encuentre. Esta es la _**opción más recomendada**_.

#### Agregar módulos al sys.path
Vamos a crear un archivo con extensión `.pth` el cual vamos a ubicarlo en el directorio "site-packages". El archivo va contener, line a linea, los path completos donde python podrá buscar los módulos que creamos.

## Private names in modules
Se Pueden importar casí todos los "names" del módulo mediante `from module import *`. Los exceptuados son los que empiezan con guión bajo (_), usando esto como una forma de ocultar partes del módulo que no queremos que se vean desde afuera del mismo.

De todas manera podemos acceder a estos con guión bajo importando el módulo normalmente y usando la notación `qualification` para acceder a lo que necesitamos.
```Python
import mymodule
mymodule._b
mymodule._area(3)
```

- Tip: es una convención usar el guión bajo para indicar "private names" en cualquier código de Python, no solo en los módulos.

## Library and third-part modules
La distribución de python esta dividida en módulos, para poder hacerla más manejable. Según la necesidad en nuestros programas podemos importar el módulo, función o clase, antes de utilizarla.
[Ptyhion Library Reference](https://docs.python.org/3.9/library/)

Podemos usar módulos de terceros.
[Python Package Index - pyPI](https://pypi.org/)

## Reglas de scoping y namaspaces
- `Namespaces`: es un mapeo de identificadores a objetos. Esta es la manera en que Python tiene el rastro de que variables e identificadores están activos y a que apuntan.

Cuando un bloque de código se ejecuta tiene tres namespaces y se busca en ellos las referencias a sus elementos en el siguiente orden: `Local`, `global` y `build-in`.

Debemos tener cuidado cuando nombramos elementos, porque se pueden sobreescribir los los del módulo `build-in` (len, min, max, int, float, list, tuple, range...).

`Locals()` and `globals()` son funciones build-in que retornan un diccionario que contienen los bindings de cada espacio.

Con `del` podemos borrar los bindings del namespace.

```Python
x = 2
import math
from cmath import cos
globals()
locals()

del x, math, cos    ## podemos borrar los bindings
globals()
locals() 
```
[Code](10_ModulesAndScopingRules.py)

Veremos ahora un poco del build-in namespaces. 
`dir()`: al darle un modulo como parametro, devuelve una lista de nombres definidas en él.

Aqui vemos los nombres de entradas de Error, Exit y funciones de build-in. Podemos obtener documentación de ellos de la siguiente manera:
```Python
help(max)
print(max.__doc__)
```

Es un error común sobrescribir algún "name build-in" o quizas otro name ya usado en el namespace. En el primer caso podemos recuperar el binding borrando el nombre sobrescrito usando "del"
