## Módulo search path
import sys
sys.path

## Reglas de scoping y namaspaces
x = 2
import math
from cmath import cos
globals()
locals()

del x, math, cos    ## podemos borrar los bindings
globals()
locals()

""" Probando los scopes desde la consola en el directorio de trabajo"""
import scopetest
z=2
scopetest.f(z)    # Vamos a notar que z no esta en la lista de locals()

