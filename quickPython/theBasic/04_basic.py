# Factorial code
## el input es un string por defecto. Lo pasamos a int o float si es necesario
n = int(input("factorizar un numero "))
r = 1
while n > 0:
  r *= n
  n -= 1
print (r)

# Las variables funcionan como tag a un valor.
a = [1, 2, 3]
b = a
c = b
b[1] = 5
print(a, b, c)

d = """ asi podemode escribir saltos de pagina sin tener que aplicar 
el signo de escape."""

del c     # borra la variable c

print (d)

## Estilo de codeo para Python (PEP-Python Enhancement Proposal)
## my_func, my_var, my_module, MyClass, CONST_NAMES