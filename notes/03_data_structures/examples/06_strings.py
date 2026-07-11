## Podemos usarla como secuencias de caracteres
# Operaciones básicas
x = "Hola\n"    # podemos utilizar secuencias de escape -> hexadecimal|ASCII "\" , octal "\x"
x[0]
x[:-1]    ## leemos la secuencia salteando el "\n"
len(x)    ## podemos determinar la cantidad de caracteres
# x.append("c") | x[0]="c" ## Los strings NO pueden Modificarse, son INMUTABLES
x = "Hola " + "Mundo"
8 * "x"   ## podemos multiplicar el string

#String methods
# Al usar "+" para concatenar strings perdemos performance porque creamos 2 objetos.
palabras = "-".join(["Hola", "todo", "el", "Mundo"]) # usamos mejor el metodo join que es más eficiente
palabras.split("-")    # por defecto elimina los espacios pero podemos pasarle la secuencia de caracteres a eliminar
y = 'a b c d'
y.split(' ', 2)   # podemos indicar los n+1 grupos que forma al realizar el split

# String to numbers
float('123.456')
int('123')
int('1000', 8)      ## "1000" en base octal
int('1000', 2)      ## "1000" en base binaria
int('ff', 16)       ## "1000" en base hexadecimal

# Eliminando espacios al inicio o final de un string
import string           # segun el OS se tomán como espacio en blanco diferentes caracteres, 
string.whitespace       # de esta manera podemos determinar cuales son los mismos
" \t\n\r\v\f"

x = "   Hola todo el mundo \t\n"
x.strip()   # elimina espacios a la izquierda y derecha del string
x.lstrip()
x.rstrip()
y = "www.pepe.com"
y.strip("moc")      ## elimina en cualquier orden los caracteres

# String searching
# El modulo "re" tiene diferentes formas de tratar de string que retomaremos más adelante
## Simple string searching "find, rfind, index, rindex".
# Relacionado a estos tb tenemos "count" que cuenta las ocurrencias
x = "Mississippi"
# string.find("text", start, end)
x.find("ss",2)    ## devuelve la posición de la primera ocurrencia, sino devuelve "-1"
x.count("ss")     ## cuenta la ocurrencia del texto en el string
## Los siguientes tambien lo podemos usar con una tupla como parametro y buscar varias palabras.
x.startswith("Miss")  ## indica si hay coincidencia en el inicio del string
x.endswith("pi")
x.endswith(("i","u"))

# Modificando strings
## No podemos realmente modificarlas directamente, pero podemos aplicales métodos para que retornen 
## nuevas cadenas resultantes de la original 

x = "Mississipi"
x.replace("ss", "+++")
## Realizar remplazo de caracteres por otro con los siguientes dos métodos
x = "~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]")   
x.translate(table)

x = "probando que \t podemos hacer con algunos metodos"
x.lower()
x.upper()
x.capitalize()    ## pone en mayuscula el primer caracter del string
x.title()         ## pone en mayusculas el primer caracter de todas las palabras en el string
x.expandtabs(tabsize=4)   ## cambiamos el \t por una cantidad de espacios determinada
x.zfill(60)   ## completa con ceros a la izquierda para llegar a una cantidad de caracteres dada por el parametro del metodo
x.rjust(60)   ## justifica el string a la derecha y agrega espacios para llegar al ancho dada por el parametro del metodo
x.ljust(60)

# Modificando string con manipulación de listas
text = "Hello, World"
wordList = list(text)
wordList[6:] = []   ## elimino elementos de la lista
wordList.reverse()
text = "".join(wordList)    ## este metodo es costoso en terminos de procesamiento ya que crea y destruyes objetos

# Objects to strings
x =[1]
x.append(2)
x.append([3, 4])
'The list x is ' + repr(x)      ## repr(), el objeto x lo representa como un string

# Format Method
"{{Ambrosia}} es la {0} de los {1}".format("comida", "Dioses")
"{comida} es la comida de los {user[0]}".format(comida="Ambrosia", user=["hombre", "Dioses", "otros"])
"{0:10} es la comida de los Dioses".format("Ambrosia")
"{food:{width}} es la comida de los Dioses".format(food="Ambrosia", width=10)
"{0:&>10} es la comida de los Dioses".format("Ambrosia")

# String interpolation (f-strings) -> PEP-498
pi = 3.1415
print(f"pi es {pi:{10}.{3}}")

# Bytes object -> secuencia de Enteros con valores entre 0 y 256. Util cuando se esta trabajando con datos en binarios
unicode_a_with_acute = "\N{LATIN SMALL LETTER A WITH ACUTE}"    ## caracter unicode
unicode_a_with_acute
xb = unicode_a_with_acute.encode()    ## el caracter unicode lo transformo en un objeto de 2 bytes
xb.decode()   ## decodifico el objeto de bytes al string original
