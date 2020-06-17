v=6
def f(x):
   """f: test de alcence de la función"""
   print("global: ", list(globals().keys()))
   print("entry local: ", locals())
   y = x
   w = v
   print("exit local: ", list(locals().keys()))