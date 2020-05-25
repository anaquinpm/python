# Environment
Podemos instalar **diferentes** versiones de python en un mismo sistema.

Por lo general en Linux contamos con una instalación de python por defecto.

```bash
$ python3 -V		# Vemos que versiónde python se encuentra en nuestro OS.
$ python2 -V
$ sudo apt install python3		# En sistemas tipo debian/ubuntu
$ sudo apt install idle			# Instalamos la consolo interactiva
```

**`INFO`**: www.python.org tiene más opciones para isntalar en diferentes OS.

- Vamos a utlizar como interprete
  - Linea de comandos: ingresamos colocando `python3` en el prompt
  - IDLE (Integrated development environmet): tiene pequeñas ayudas para interactuar e ingresamor colocando `idle` en el prompt

**`OPCION`**: podemos utlizar directamente nuestro editor de código de preferencia si es que lo deseamos.

## Hello World
```python
print("Hello, world")		# En python3, print es una función por lo que debemos usarla de esta manera
x=2
help(x)						# Fc. que permite tener ayuda de keyword, modulos o topics
```

`help()` es parte de la librería `pydoc` la cual nos da acceso a documentación propia de las librerías de Python.

```python
dir()		# Fc que permite ver los objetos en un namespace determinado. Sin parametros muestra los **objetos Globales**
globals()
locals()	# Las ultimas dos Fc muestran los objetos relacionados a sus valores.
```
Con estas funciones podemos encontrar rapidamente metodos y definiciones de datos en los diferentes namespaces.
