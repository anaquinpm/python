# ingresar 3 nombres y edades para los mismo. Consultar un nombre y que arrije su edad
edades = {}
while len(edades) < 3:
  nombre = input("Ingrese un nombre\n")
  edades[nombre]= int(input ("Ingrese la edad para esa persona\n"))
print(edades.keys())
print(edades[input("De quien quiere saber la Edad")])