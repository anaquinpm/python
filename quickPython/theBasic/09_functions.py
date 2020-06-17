def factorial(n):
  """ Retorna el Factorial de un número dado """
  r = 1
  while n > 0:
    r *= n
    n -= 1
  return r    # Valor que retorna la función

print(factorial(int(input("Ingrese un número"))))

### Parametros posicionales
""" Potencia de un numero, según su base y potencia """
def potencias(x, y):
  r = 1
  while y > 0:
    r *= x
    y -=1
  return r

print(potencias(3, 3))

#### Default values
""" Potencia de un numero, según su base y potencia. Si no se pasa el segundo parametro se toma potencia 2 """
def potencias(x, y=2):
  r = 1
  while y > 0:
    r *= x
    y -=1
  return r

print(potencias(3,4))

#### Indefinido números de argumentos posicionales
""" Determinar el número máximo de una lista de numeros"""
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

#### Indefinido números de argumentos pasados por "Keyword"
def funcion(x, y , **otros):
  print("x: {0}, y: {1}, keys en 'otros': {2}".format(x, y, list(otros.keys())) )

funcion(3, y =2, foo=3, bar=4)

## Asignar funciones a variables
""" Convertidor de temperatura a grados Kelvin """
def f_to_kelvin(degrees_f):
  return 273.15 + (degrees_f - 32) * 5 / 9

def c_to_kelvin(degrees_c):
  return 273.15 + degrees_c

abs_temp = f_to_kelvin
print(abs_temp(32))
abs_temp = c_to_kelvin
print(abs_temp(0))

t = {'FtoK': f_to_kelvin, 'CtoK': c_to_kelvin}
print(t['FtoK'](32))

## Lambda expressions
temp = {'FtoK': lambda deg_f: 273.15 + (deg_f - 32) * 5 / 9, 'CtoF': lambda deg_c: 273.15 + deg_c}
print(temp['FtoK'](32))

## Generador de funciones
def cuatro():
  x = 0
  while x < 4:
    print("en el generador, x = ", x)
    yield x
    x +=1

for i in cuatro():
  print(i)

### Yield from
def subgen(x):
  for i in range(x):
    yield i

def gen(y):
  yield from subgen(y)

for q in gen(6):
  print (q)

## Decorators
def decorate(func):
  print(" in the function decorate, decorating", func.__name__) # Imprime el nombre de la fc que está encapsulando
  def wrapper_func(*args):    # usualmente se usa el prefijo wrapper_ para la inner fc.
    print("Executing", func.__name__)
    return func(*args)
  return wrapper_func         # retorna la fc encapsulada

@decorate                     # definimos que la siguiente función es la que va se encapsulada por "decorate()"
def myfunction(parameter):
  print(parameter)

myfunction("hello")