# Tuplas

"""
Una tupla es una secuencia ordenada(conjundo ordenado) e inmutable de elementos, que pueden contener todo tipo de valores separados por comas, dentro de paréntesis.
"""

notas = (18, 17, 15, 11, 14, 20)

print(notas)

notas1 = (18, 17, 15, 11, 14, 20,)

print(notas1)

mi_tupla = (True, 20, "Max", 50.35) # mi_tupla = (True, 20, "Max", 50.35,)

tupla = 1, 2, 4 # tupla = 1, 2, 4,

print(tupla)

# tupla_vacia = ()

tupla_un_elemento = (5,) # tupla_un_elemento = 5,

print(tupla_un_elemento)

print(type(tupla_un_elemento))

un_elemento = (5) # es un int y no es una tupla

print(un_elemento)

print(type(un_elemento))

# no_es_tupla = (5) # no es una tupla, es un int

# Las tuplas son un tipo de variable

# print(type(tupla)) # <class 'tuple'>

# print(type(mi_tupla)) # <class 'tuple'>

# Accediendo a los elementos de una tupla

print(mi_tupla[0]) # True

print(mi_tupla[3]) # 50.35

print(type(mi_tupla[3])) # <class 'float'>

print(mi_tupla[-1]) # 50.35

# Combinando tuplas

tupla1 = ("fresa", 10.00, True, 25)

tupla2 = ("kilos", 14)

tupla3 = tupla1 + tupla2

print(tupla3)

tupla4 = tupla3 + (False, 5, "otros")

print(tupla4) # ('fresa', 10.0, True, 25, 'kilos', 14, False, 5, 'otros')

# Extrayendo elementos

print(tupla4[0:3]) # devuelve a la tupla ('fresa', 10.0, True)

# print(tupla4[:3]) # ('fresa', 10.0, True)

print(tupla4[5:9]) # (14, False, 5, 'otros')

# Tamaño de una tupla - len

longitud = len(tupla4)

print(longitud)

print(len(tupla4)) # 9

# inmutabilidad

paises = ("Perú", "Colombia", "Argentina")

tupla_paises = paises # ambos apuntan a la misma referencia en memoria

# paises[1] = "Uruguay" # error

print(tupla_paises)

# sorted

notas_ordenados = sorted(notas)

print(notas_ordenados)

print(notas)

print(sorted(notas, reverse=True))

# Una tupla puede contener otras tuplas

tupla_nesting = (10, (True, "Saludar", 20.0), False, 50)

print(tupla_nesting[1]) # (True, 'Saludar', 20.0)

print(tupla_nesting[1][2]) # 20.0

print(tupla_nesting[1][1][-1]) # r
 
print(tupla_nesting[1][1][len(tupla_nesting[1][1]) - 1]) # r

# Las tuplas tienen algunos métodos como index, count, etc. que por ahora no lo veremos.

help(tupla_nesting)