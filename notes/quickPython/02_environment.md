# Environment

Podemos instalar **diferentes** versiones de python en un mismo sistema.

Por lo general en Linux contamos con una instalación de python por defecto.

```bash
python3 -V                    # Ver versión de Python instalada en el sistema
python2 -V
sudo apt install python3 python3-pip python3-venv     # En sistemas tipo debian/ubuntu y el manejador de paquetes "pip"
sudo apt install idle3        # Instalar consola interactiva
```

**`INFO`**: www.python.org tiene más opciones para instalar en diferentes OS.

- Vamos a utlizar como interprete
  - Linea de comandos: ingresamos colocando `python3` en el prompt
  - IDLE (Integrated development environmet): tiene pequeñas ayudas para interactuar e ingresamos colocando `idle3` en al terminal

**`OPCION`**: podemos utlizar directamente nuestro editor de código de preferencia si es que lo deseamos.

## Hello World

```python
print("Hello, world")       # En python3, print es una función por lo que debemos usarla de esta manera
x=2
help(x)                     # Fc. que permite tener ayuda de keyword, modulos o topics
```

`help()` es parte de la librería `pydoc` la cual nos da acceso a documentación propia de las librerías de Python.

```python
dir()       # Fc que permite ver los objetos en un namespace determinado. Sin parametros muestra los **objetos Globales**
globals()
locals()    # Las ultimas dos Fc muestran los objetos relacionados a sus valores.
```

Con estas funciones podemos encontrar rapidamente métodos y definiciones de datos en los diferentes _namespaces_.

## Crear un entorno

```bash
sudo apt install python[version] python[version]-venv   # instalar la versión de python deseada y su modulo de "venv"
  sudo apt install python3.11{,-venv}

# Crear entorno local para instalar dependencias para un proyecto
python3.9 -m venv <envs/myEnv>  # este siempre ejecuta la versión de python actualmente instalada
  python3.9 -m venv --system-site-packages <envs/myEnv>   # 
## --- recordar incluir en el archivo .gitignore la carpeta de entorno creada en cada proyecto <envs/MyEnv>

source /envs/myEnv/bin/activate # Activar entorno
deactivate                      # Desactivar entorno
```
