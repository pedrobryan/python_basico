# Los diccionarios

"""
Los diccionarios son colecciones de datos, donde cada elemento esta asociado a una clave, es decir los elementos del diccionario son de la forma clave: valor(key: value)
Los keys o claves deben ser inmutables y únicos.
"""

mi_diccionario = {"clave1": 20, "clave2": "Texto", "Clave3": (1, True), "clave 4": [1, 51], (1, 20): 25.0}

print(mi_diccionario)

print(mi_diccionario["clave 4"])

print(mi_diccionario[(1, 20)])

# Agregando un nuevo elemento

mi_diccionario["clave5"] = 41.56

print(mi_diccionario)

# elimando un elemento con "del"

del(mi_diccionario["clave1"])

print(mi_diccionario) # {"clave2": "Texto", "Clave3": (1, True), "clave 4": [1, 51], (1, 20): 25.0}

# Usando in paar ver si existe esa clave en un diccionario

print("clave 4" in mi_diccionario)

print("clave 5" in mi_diccionario)

# Obtener las claves de un diccionario

print(mi_diccionario.keys())

print(type(mi_diccionario.keys()))

# Obtener los valores de un diccionario

print(mi_diccionario.values())

print(type(mi_diccionario.values()))
