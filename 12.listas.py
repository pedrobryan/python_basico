# Listas

# """
# Las listas son secuencias ordenadas en python, que puede contener todo tipo de valores al igual que una tupla, con la diferencia que son mutables, es decir pueden reasignarseles valor a sus elementos.

# Se crean mediante corchetes y los elementos estan separados por comas
# """

print("----- Listas -----")

lista_uno = [1, True, (10,), "texto"] # lista_uno = [1, True, (10,), "texto",]

print(lista_uno)

lista_dos = [10] # lista_dos = [10,]

print(lista_dos)

print(type(lista_dos))

# accediendo al valor de un elemento

print(lista_uno[1])

elem1 = lista_uno[1] # asignación por valor, elem1 = True

print(elem1) # True

# Modificando el valor de un elemento

lista_uno[1] = False # ahora lista_uno es [1, False, (10,), "texto"]

print(elem1) # True

el1 = lista_uno[1]

print(el1) # False

print(lista_uno[1]) # False

# Agregar más elementos a la lista

# lista_uno[len(lista_uno)] = "Elemento agregado" # da error, ya que se está desbordando la lista, no hay ese índice, está fuera de rango.

# una tupla puede contener otras listas

lista_tres = [15, False, (2, 10), "cadena", [True, 25],]

print(lista_tres)

print(lista_tres[-1])

print(lista_tres[-1][-2]) # True

# Extrayendo elementos en una nueva lista

tres_primeros = lista_tres[:3] # [15, False, (2, 10)]

print(tres_primeros)

dos_primeros = lista_tres[0:2]

print(dos_primeros)

# concatenando listas

lista1 = ["Fresa", 20, 25, True]
lista2 = ["Mandarina", 17, 35, False]

lista3 = lista1 + lista2 + ["Manzana",14, 20, True,]

print(lista3) # ['Fresa', 20, 25, True, 'Mandarina', 17, 35, False, 'Manzana', 14, 20, True]

# Algunos métodos de una lista

# Usando el metodo extend(), concatena otra lista, pero la lista es actualizada o modificada.

lista1.extend([100, 250]) # modifica y regresa None

print(lista1) # ['Fresa', 20, 25, True, 100, 250]

# usando el método append, agrega un elemento a la lista, solo un elemento que puede un tipo simple o tupla, lista, etc.

lista1.append("texto nuevo") # modifica la lista

print(lista1)

lista1.append([False, "otro texto"])

print(lista1)

lista1.append((10, 20))

print(lista1) # ['Fresa', 20, 25, True, 100, 250, 'texto nuevo', [False, 'otro texto']]

# Modificando un elemento

# lista1[1] = 20.5

# print(lista1) # es mutable

# Borrando un elemento

del(lista1[2])

print(lista1)

# convertir un string a lista con el método split()

texto = "soy un texto"

lista_texto = texto.split() # por defecto ese texto es separado por los espacios en blanco - lista_texto = texto.split(sep=' ')

print(lista_texto)

print(texto)

cadena1 = "a,b,c,d,e,f"

print(cadena1.split(sep=","))
# print(cadena1.split(","))
print(cadena1)
# print("x.y.z.w".split(sep="."))
# # print("m,n,p,q,r".split(sep=","))

countries = ["Perú", "Argentina", "Colombia"]

# Alias

countries2 = countries # countries2 apunta al espacio de memoria de la variable countries

print(countries2[2])

countries[2] = "Uruguay"

print(countries)

print(countries2)

# Clonar

listaA = [1,  True, "Cusco"]

listaB = listaA[:] # listaB solo contendra el valor, listaB = [1,  True, "Cusco"]

print(listaB)

listaA[2] = "Arequipa"

print(listaA)

print(listaB)

# clear, deja a la lista vacía

listaA.clear()

print(listaA)

# count, cuenta el número de veces que aparece un valor dentro de la lista

vocales = ["a", "e", "i", "o", "u", "a", "a", "e", "a"]

numA = vocales.count("a")

print(numA)

# index(), Devuelve el índice en el que aparece un ítem (error si no aparece)

print(vocales.index("o")) # 3

# print(vocales.index("L")) # error

# insert(índice, valor) # -  Agrega un ítem a la lista en un índice específico:

vocales.insert(1, "i") # en la posicion 1 pone a el valor i y desplza a la e

print(vocales) # ['a', 'i', 'e', 'i', 'o', 'u', 'a', 'a', 'e', 'a']

vocales.insert(-1, "u")

print(vocales) # ['a', 'i', 'e', 'i', 'o', 'u', 'a', 'a', 'e', 'u', 'a']

# un indice fuera de rango incluye al final

vocales.insert(len(vocales), "vocal")

print(vocales)

# vocales.insert(99999, "otra vocal")

# print(vocales)

# pop() - Extrae un ítem de la lista y lo borra. Devuelve el elemento.

numeros = [1, 5, 62, 20.0]

print(numeros.pop())

print(numeros)

numeros.pop()

print(numeros)

elemento_pop = numeros.pop()

print(elemento_pop)

print(numeros)

# remove() - Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos

l = [20,30,30,30,40]

l.remove(30)

print(l) # [20,30,30,40]

# reverse() - invierte el orden de los elementos de la lista actual

l.reverse()

print(l) # [40,30,30,20]

# sort() - Ordena automáticamente los ítems de una lista por su valor de menor a mayor

l.sort()

print(l)



# help([1, 3])


# # link para leer

# # https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-las-listas/