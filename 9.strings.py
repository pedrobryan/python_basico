# Es una secuencia de caracteres

saludo = "Buenos días"

gretting = 'Hello, how are you?'

# print(type(gretting))

texto = "1 2 3 4 5"

texto2 = "@$#&/*%"

print(texto2)

name = "Robert Downey Jr."

print(name[0]) # R

print(name[16]) # .

print(name[-1]) # .

print(name[-5])

# Extrayendo fragmento del texto

print(name[:6]) # Robert

print(name[0:6]) # Robert

print(name[7:13]) # Downey

print(name[0::2]) # Rbr onyJ.

print(name[::2]) # Rbr onyJ.

print(name[7::2]) # Dwe r

print(name[0:5:2]) # Rbr

print(name[0:]) # Robert Downey Jr.

print(name)

print(name[5:]) # t Downey Jr.

print(name[0:-1]) # Robert Downey Jr   -- no considera al último

x = 7

print(name[0:x]) # Robert

# Longitud de la cadena de texto - uso de len

print(len(name)) # 17

print(name[16]) # .

print(name[len(name) - 1]) # .

# Concatenar cadenas

print("Hola" + " mundo") # Hola mundo

saludo = "Hola"
nombre = "Max"

print(saludo + nombre)

print(saludo + " " + nombre)

# Replicar valores con "*"

print(3 * "Max ")

# Los strings son inmutables, se refiere a que los caracteres de las cadenas no pueden modificarse como un array

# nombre[0] ="m" # da error

nombre = "Hola " + nombre

print(nombre)

print(nombre + ", el pequeño.")

# Secuencia de escape - uso de "\" - ALT + 92

# print("Hola "Max"")

print("Hola \"Max\"")

print("Hola, bienvenido.\nEsta es una nueva línea") # salto de línea

print("Hello \t desde Python") # tabulación

print("Hello \ desde Python")

print(r"Hello \ desde Python")

print("Hello \\ desde Python") # es útil cuando queremos escapar un caracter como tal que dificulta nuestro código

# print("\") # da error

# # https://stackoverflow.com/questions/33729045/what-does-an-r-represent-before-a-string-in-python

print("\"") # "

print(r"\"") # \"

# print("\"")

# print(r"\") # da error

print("\\") # \

# Métodos para cadenas

print("Métodos para cadenas")

# upper()

a = "soy una cadena de texto"
print(a.upper())
print(a)

b = a.upper()
print(b)
print(a)

# lower()

print(b.lower())

# replace()

print(b.replace("UNA CADENA DE", "UN")) # SOY UN TEXTO

print(b) # 

# find, encuentra la primera coindiencia y devuelve el indice, si no encuentra coincidencia devuelve -1

print(a.find("a")) # 6
print(a.find("A")) # -1, ya que "A" no existe en la cadena, hay "a" que es diferente de "A"
print(a)

# Tenemos más métodos para cadenas en python como rfind(), join(), split(), lstrip(), rstrip() y strip().