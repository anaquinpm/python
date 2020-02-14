## Usando join y split trabajamos el texto "estamos en el lab" para remplazar los espacios por "-"
texto = "Estamos en el lab"
format_text = texto.split()
"-".join(format_text)

## retor solo "Pablo, Febero" del siguiente string
x = "(Pablo, Febrero),\n"
x.strip("(\n),")      ## consideramos que no toma el orden de los caracteres a eliminar

## Formas de buscar la palabra "rechasado" en un string
x = "Revisar este texto para ver si termina con la palabra roma"
x.find("roma")
x.rfind("roma")
x.endswith("roma")
x.count("roma", -4)

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
x.replace("\"","")

# Format
"{1:{0}}".format(3, 4)
"{0:$>5}".format(3)
"{a:{b}}".format(a=1, b=5)
"{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
