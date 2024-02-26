# Leer y escribir archivos

```python
with open('archivo.txt','r') as file_object:
   line = file_object.readline()
```

Con la función `open` retorna un **file object** el cual apunta al archivo, de tal manera que las I/O las realizamos usando este objeto.

En el ejemplo anterior el **context manager** y el `with` cierra automáticamente el archivo una vez que lo utilizan completamente.

El según el argumento de `open` nos indica el **modo** en que vamos a abrir el archivo.

Modo    | descripción
--------|----------------------------
'r'     | Abre el archivo para lectura
'w'     | Abre el archivo el escritura, borrando su contenido si existe.
'a'     | Abre el archivo agregar contenido al final del mismo.
'rb'    | Abre el archivo para lectura pero en modo binario (secuencia de bytes)
'wb'    | Abre el archivo para escritura pero en modo binario (secuencia de bytes)

En caso de que abramos un archivo utilizando simplemente la función `open`, no debemos olvidarnos de cerrar el archivo para liberar recursos del sistema, esto se realiza mediante la función `close` ("file_object.close()").

`readline` Lee linea a linea el archivo apuntado hasta que retorna un **empty string**.

`readlines` nos permite leer todo un archivo linea a linea, retornando una "lista" cuyos elementos son cada línea del archivo. Volcando de esta manera todo el archivo a memoria.
También podemos utilizar otra forma simple de leer un archivo y contar sus lineas.

```python
file_obj = open("arch.txt". 'r')
count = 0
for linea in file_obj:
  count += 1
print (count)
file_obj.close
```

**!** La ventaja de usar el código anterior para leer por líneas un archivo es que utiliza memoria a medida que va  leyendo, por lo que es una ventaja con archivos de gran tamaño para no quedarnos sin memoria y además es simple de leer.

- `writeline` y `writelines` son simetricas a los métodos anteriormente vistos.

[ejemplo de lectura y escritura](lines.py)

```python
input_file = open("binaryfile",'rb')
header = input_file.read(4)           # El argumento en "read(arg)" indica el tamaño fijo de bytes a leer, o menos si no tiene suficiente indormación.
data = input_file.read()              # read() sin argumentos lee todo los bytes
input_file.close()                    # Cerramos el obajeto.
```

## Pathlib: leer y escribir

```python
from pathlib import Path
p_text = Path('texto.txt')
p_text.write_text('Contenido que queremos en nuestro archivo')
p_text.read_text()
p_binary = Path('archivobinario')
p_binary.write_bytes(b'Escribimos en binario para este archivo')
p_binary.read_bytes()
```
