# Funciones lambda

def sumar(x, y): # forma declarada
    return x + y

suma = lambda a,b : a + b # forma expresada, uso de función anónima o lñambda

print(suma(5,6))

# map

# opera sobre los elementos de una lista

# map(funcion que opera sobre los elementos, lista)

def alCuadrado(el):
    return el**2

print(alCuadrado(2)) # 4

lista = [1,2,3]

print(list(map(alCuadrado, lista))) # alCuadrado es usada como callback

print(list(map(lambda x: x**3, lista))) # función lambda usada como callback, y en su forma anónima(función anónima)

# filter

# filter(func, lista)

menorACinco = lambda x: x < 5

def menorQueCinco(x):
    return x < 5

elementos = [1,2,4,5,14,20]

print(list(filter(menorACinco, elementos)))

print(list(filter(lambda x: x < 6, elementos)))

# reduce

# reduce(func, lista)

# func tiene la forma : usa dos parámetros.
# cuando la funcion recorra la lista va a crear un acumulador que almacena los valores de haber sumado el primer elemento de la lista con el sgte y luego sumar lo acumulado con el tercero y asi al llegar al ultimo

from functools import reduce

# lista: [1,2,3]

print(reduce(suma, lista)) # 6

print(reduce(lambda x,y : x * y, [1,5,10])) # 50

print(reduce(lambda x,y : 2 * x + y, [1,5,3], 2)) # 33

print(reduce(lambda x,y: x + y, [1,5], 20)) # it1: 20 + 1 = 21 -> ac = 21; it2: ac + 5 = 21 + 5 = 26 