# Loops (ciclos o bucles)

# Explicando el tipo range

"""

range es un objeto con números en sucesión aritmética

range(inicio, fin, paso)

range(fin)

el paso por defecto es 1

"""

print("---------- rango -------------")

rango = range(4) # va del 0 al 3 # range(0, 4)

print(type(rango))

print(rango) # range(0, 4)

# para verlo podemos pasarlo a una lista, convertir el rango a una lista con la función list

lista = list(rango)

print(lista)

rango2 = range(1, 5)
print(list(rango2))

rango3 = range(5, 25, 2)
print(rango3)
print(list(rango3))


# Podemos recorrer el rango sin convertirlo lista, tal como veremos con los ciclos while y for

# Ciclo while

print("---------- while -------------")

i = 0

while(i < len(rango)): # rango tiene los valores de 0, 1, 2, 3
    print(rango[i])
    i += 1 # i = i + 1

print("---------------------------")

tupla = (5, "Hola", False)

j = 0

while (j < len(tupla)):
    print(tupla[j])
    j += 1

# Ciclo for

print("---------- for -------------")

for x in rango:
    print(x)

print("---------------------------")

lista = [1, True, 25.0, "Max"]

for el in lista:
    print(el)

print("---------------------------")

for m in range(len(lista)): # range(4) # range(0:4) # 0, 1, 2, 3
    print(lista[m]) # print(lista[0]), print(lista[1]), print(lista[2]), print(lista[3])

print("---------------------------")

mi_set = {1, "texto"}

for y in mi_set:
    print(y)
    # print("Hola")

print("---------------------------")

mi_diccionario = {"nombre": "Max", "raza": "Rott Weiller", "edad": 2}

# con for podemos recorrer las claves de un diccionario

for clave in mi_diccionario:
    print(f"{clave}: {mi_diccionario[clave]}")

# Hay métodos especiales que nos permiten acceder a los valores o las claves de un diccionario, esos son keys() y values()

print("---------------------------")

for k in mi_diccionario.keys():
    print(k)

print("---------------------------")

for v in mi_diccionario.values():
    print(v)

# Algo adicional

# enumerate

# """
# Uso de función enumerate

# Transforma a un objeto iterable(que se pueden recorrer con for) de python en un objeto de pares ordenados (indice, valor) que en realidad son tuplas, para verlo debemos transformarlo en una lista con el método list
# """
print("---------------------------")

enum = enumerate(lista) 
print(enum)
print(type(enum))

lista_enum = list(enum)

print(lista_enum) # [(0, 1), (1, True), (2, 25.0), (3, 'Max')]

for (indice, valor) in enumerate(lista):
    print(f"{indice}: {valor}")

print("---------------------------")

for indice, valor in enumerate(lista):
    print(f"{indice}: {valor}")