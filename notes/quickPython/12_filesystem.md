# Usando el filesystem

## Pathsnames

Un `path` es la ruta de acceso a un directorio o archivo, al cual python puede acceder mediante los módulos *os* u *os.path* y actualmente se está usando más **pathlib**.

Dependiendo del O.S., la convención de como se representan un `path` varía. Python nos abstrae de esta complejidad de representación de tal manera de hacer posible correr nuestro programa sin problemas en diferentes *filesystems*.

- Tipos:
  - Absolutos: este indica el *path completo* de un archivo en el filesystem. EJ: "/home/anaquin/dev/usr.py"
  - Relativos: la posición del archivo se indica en forma relativa, en función del contexto en el que se use. EJ: "dev/usr.py"
    1. Tomando como referencia un path absoluto y concatenarlo a uno relativo.
    2. Tomando como referencia el **directorio de trabajo actual**

```python
import os
os.getcwd()       # "current working direcotory"
```

 directorio   | rep | representación portable
--------------|-----|------------------------
  actual      | .   | os.curdir
  padre       | ..  | os.pardir

```python
os.chdir("folder_name")     # Cambiar el directorio actual
os.listdir(os.curdir)       # Devuelve una "lista" con los archivos y directorios en el directorio actual
print(os.path.split(os.path.join('algun','directorio','archivo')))   # "('algun\\directorio', 'archivo') -> siempre devuelve una tupla
print(os.path.basename(os.path.join('algun','directorio','arch.txt')))   # "('arch.txt')
print(os.path.dirname(os.path.join('algun','directorio','arch.txt')))    # "('algun\\directorio')
print(os.path.splitext(os.path.join('algun','directorio','arch.txt')))   # "('algun/directorio/arch', '.txt')
os.path.expadvars('$USER')                                               # "anaquinpm" -> Muestra variables del sistema.
```
Con la constante os.name podemos saber en que O.S. se está ejecutando el código, de tal manera que podriamos usar este dato para utilizar operaciones especiales para cada caso.

```python
import os
if os.name == 'posix' :         # OS linux
  root_dir = "/"
elif osname == 'nt' :           # Cualquier versión de windows
  root_dir == "C:\\"
else:
  print("No se que OS tiene este sistema")
```

### Pathlib
```python
import pathlib
cur_path = pathlib.Path()
cur_path.cwd()              # "PosixPath('/home/anaquin/dev')
```

```python
form pathlib import Path
cur_path = Path()
print(cur_path.joinpath('bin', 'utils', 'disktools')    # "bin\utils\disktools"
a_path = Path('algun', 'directorio', ' arch.tx')
a_path.name                                             # "arch.txt"
print(a_path.parent)                                    # "algun\directorio"
a_path.suffix                                           " ".txt"
```


