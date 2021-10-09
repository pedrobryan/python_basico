# Los sets o conjuntos

"""
Los sets, es un conjunto de elementos.
Son desordenados.
El set es mutable.
Sus elementos no se repiten.
Puede contener elementos de tipo texto(str), entero(int), decinal(float), lógico(bool), tupla(tuple).
No puede contener a otro set, lista(list), diccionario(dict), ya que solo debe contener elementos inmutables como la tupla
"""

set1 = {"uno", "dos", 20, 15, False, True, 15, "dos", "tres", (1,)}

print(set1)

set2 = set() # Conjunto vacío

print(type(set1))

# Crear un set a partir de una lista

set3 = set([1, 20, True, 50, 20]) # crea {1, 50, 20} , al True lo ve como el número 1

print(set3)

print(set([1, 20, True, (111,)]))

# print(set([1, 20, True, (111,), ["texto", 24]])) # error

# print(type(set1))

# set a partir de una tupla

print(set((1,20)))

tupla = (1, False)

print(set(tupla))

# Usando método add, agrega un elemento al set

set3.add("texto")

print(set3)

set3.add((20, 5, True))

print(set3) # {1, (20, 5, True), 'texto', 50, 20}

# Usando remove

set3.remove(50)

print(set3)

# set3.remove((20, 5, True))

s = (20, 5, True)

set3.remove(s)

print(set3) # {1, 'texto', 20}

# Buscando un elemento dentro del set con "in"

print("texto" in set3) # True

print(1 in set3)

print(50 in set3)

# Intersección de sets

set_1 = {5, 25, 75, 105}

set_2 = {15, 45, 75, 105}

print(set_1 & set_2) # retorna el set {105, 75}

(set_1.intersection(set_2))

print((set_1.intersection(set_2)))

# Unión de sets

print(set_1.union(set_2))

# Uso de issubset, pregunta si los elementos de un set estan todos dentro de otro set, es como preguntar si es un subconjunto.

set_3 = {15, 75}

print(set_3.issubset(set_2)) # True

# # https://hetpro-store.com/TUTORIALES/set-en-python-7-colecciones/
# # https://www.delftstack.com/es/tutorial/python-3-basic-tutorial/data-type-sets/

# # https://j2logo.com/python/tutorial/tipo-set-python/

