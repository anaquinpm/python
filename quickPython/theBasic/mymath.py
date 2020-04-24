""" mymath - ejemplo de modulo"""
pi = 3.14159
def area(r):
  """ retorna el area de un circulo con radio r."""
  global pi
  return (pi * r **2)
