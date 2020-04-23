def say_hello(name):
  return f"Hello {name}"

def be_awesome(name):
  return f"yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
  return greeter_func("bob")

greet_bob(say_hello)
greet_bob(be_awesome)

""" Inner Functions """
def parent():
  print("Escribiendo desde la fc. padre")

  def first_child():
    print ("Escribiendo desde la fc. first_child()")

  def second_child():
    print ("Escribiendo desde la fc. first_child()")

  second_child()
  second_child()

parent()

""""Simple decorator"""
def my_decorator(func):
  def wrapper():
    print("Something is happening before the function is called.")
    func()
    print("Something is happening after the function is called.")
  return wrapper

def say_whee():
  print("Whee!")

say_whee = my_decorator(say_whee)

# Otro ejemplo de un decorator
from datetime import datetime

def not_during_the_night(func):
  def wrapper():
    if 7 <= datetime.now().hour < 22:
      func()
    else:
      pass  # Hush, the neighbors are asleep
  return wrapper

def say_whee():
  print("Whee!")

say_whee = not_during_the_night(say_whee)
say_whee()