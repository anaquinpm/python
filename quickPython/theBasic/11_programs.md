# Python Programs
## Haciendo scripts ejecutables directamente en Unix

```bash
$ chmod +x scriptname.py     # Damos permiso de ejecución al script
$ which python3              # Averiguamos el path donde está nuestro python
```

Conociendo el path de python, agregamos como *primera linea* del script la referencia al ejecutable de python que averiguamos.

```python
#! /usr/bin/env python3
```
```bash
$ ./scriptname args   # Ejecutamos de esta manera en nuestro shell
```

## Un programa básico
Creamos un archivo script1.py
```Python
import sys
def main():
  print("Este nuestro primer archivo de script")
  print(sys.argv)   # Leemos los argumentos que nos pasaron
main()
```
[Code](ch11/script1.py)

En la linea de comando lo ejecutamos con el siguiente comando:
> $ ./script1.py arg1 ag2

`sys.argv` Devuelve un **lista** con los argumento arg1 y arg2, que incluimos al ejecutar le programa.

### Redirigir el input/output de un script
```Python
import sys
def main():
  contents = sys.stdin.read()   # Leemos el standard input
  sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))  # escribimos en el standard output
main()
```

[Code](ch11/replace.py)

El script va leer el `stdin` para luego cambiar las ocurrencia de arg1 por el arg2 y escribirlo por el `stdout`. Con el comando siguiente podemos ejecutarlo:

> $ ./replace.py a A < infile > outfile

Podemos tambien utilizar el pipe ( | ) para redireccionar salidas desde la consola. por lo que podemos hacer dos ejecuciones (remplazos) usando el siguiente comando:

> $ ./replace.py a A < infile | ./replace.py b B > outfile

### Módulo argparse
Soporta el uso de diferentes tipos de argumentos y puede generar mensajes.

```python
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()                                             # Crea una instancia del objeto
    parser.add_argument("indent", type=int, help="indent for report")     # Positional arg (no tienen declarado al inicio "-opt")
    parser.add_argument("input_file", help="read data from this file")    # Positional arg
    parser.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE") # optional arg
    parser.add_argument("-x", "--xray", help="specify xray strength factor")                          # optional arg
    parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=TRUE, help="don't print status messages to std out")
    args = parser.parse_args()
    print("arguments: " args)

main()
```
[Code](ch11/opts.py)

Ingresamos todo los argumentos en el shell para ver como funciona el programa
```bash
$ ./opts.py -x100 -q -f outfile 2 arg2
$ ./opts.py -x100 -q -f outfile 2     ## causamos un error al no ingresar el arg2
```

### Módulo Fileinput
Permite procesar lineas de uno o varios archivos, colocando los argumentos en una lista de archivos.
```python
"""name: script5.py """
import fileinput
def main():
  for line in fileinput.input():           # input(): sin argumentos este toma los argumentos del sys.argv
    if fileinput.isfirstline():            # isfirstline(): Verifica si estamos por imprimir la primer linea del archivo
      print("<Start of file {0}>".format(fileinput.filename()))   # filename(): muestra el nombre de archivo
    if not line.startswith('##'):          # Imprime las lineas que no están comentadas
      print (line, end="")
  print(fileinput.filelineno())            # Números de lineas leidas
main()
```
> $ ./script5.py sole1.tst sole2.tst

`fileinput.input([args])`: puede tener como argumento **un nombre** de archivo o una **lista** de nombres de archivos y no utilizará el sys.argv como entrada de datos.

El método `fileinput` tiene otras funciones que se pueden ver en su documentación en más detalle.

- Módulos útiles para administración en OS Unix
  - gpr
  - pwd
  - resource
  - syslog
  - stat

## Programas y módulos
[Ejemplo: pasar n° a letras](ch11/num2words.py)

Para poder utilizar nuestro código en otros scripts o módulos tenemos que colocar nuestra función de control dentro de un condicional:

```python
if __name__== '__main__':
  main()
else:
  # module-specific initialization code if any
```
Al llamarlo al código como un script, este se ejecuta con el nombre `__main__`  y con el controlador `main()`.
Si el script fue importado a una sesión interactiva o a otro módulo, su nombre será el `nombre del archivo` que tenga.
Al crear un script y setearlo como módulo, nos dá la ventaja de poder importarlo e debugearlo a medida que voy creando mi función.

[Ejemplo](ch11/n2w.py)
```Bash
$ ./n2w.py 199
$ ./n2w.py --test < n2w.tst > n2w.txt     # Modo testeo
```

```python
" En el modo interactivo podemos importarlo como módulo "
import n2w
n2w.num2words("1,234")    " El parametro que espera la fc es un string, por eso las comillas.
```

## Distribuir aplicaciones python
Wheels es la manera más deseable de distribuir aplicaciones y módulos python. Este ayuda a que la instalación sea más intuitiva y soluciona el tema de dependencias.
- [ ] [Leer como hacer un Packages con Wheels](https://packaging.python.org)

### Zipapp and pex
- Zipapp
  - Si contiene un archivo `__main__.py` se puede usar como entry point y si a este lo agregamos al `sys.path` del sistema este puede ser importado y ejecutado.
  - Si agregamos la linea **shebang** y le damos lo permisos de ejecución al archivo, podemos hacerlo un ejecutable por si solo.
  - Podemos usar el módulo zipapp incluido en la librería standard para crear un zipapp por línea de comando.

- Pex
  - Este es un módulo que se puede instalar vía **pip**
  - Tiene muchas más opciones que zipapp

### Ejecutables
**py2exe** y **Freeze**: Crea ejecutables auto-contenidos, para windows. No es necesario tener instalado python para correr nuestra app.
