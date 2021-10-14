# Funciones en Python

"""

Las funciones permiten encapsular código repetitivo con la finalidad de poder reutilizarlo.

Dividir código para hacer todo más sencillo.

def nombre_Función(parámetro1, parámetro2, ..., parámetroN):
    instrucciones

Pueden retornar un valor usando "return" seguido del valor a retornar

Pueden o no recibir parámetros

para ejecutar sería:

nombre_Función(argumento1, argumento2, ..., argumentoN)

"""

# Sin parámetro

def saludo():
    return "Hola"


print(saludo())

# help de la función

help(saludo)

# Con parámetros 

def saludar(nombre):
    return f"Hola {nombre}"
    

mi_saludo = saludar("Max")

print(mi_saludo)


def multiplicar(a, b):
    return a * b
    print("Este mensaje no se imprime")

multiplicar(4, 7)
m = multiplicar(4, 7)
print(m)

# Argumentos pasados por posición

def restar(a, b):
    return a - b


print(restar(5, 3))

# Argumentos pasados por nombre

print(restar(b=3, a=1))

# retorna nada(None) y no ponemos que retorna.

def f1():
    print("Hello")


def f2():
    print("Hello")
    return None

f1()
f2()

print("-------------")

x1 = f1()
x2 = f2()

print(x1)
print(x2)

# ejemplo de función

def mayorEdad(edad):
    isMayor = False
    if(edad >= 18):
        isMayor = True
    return isMayor


edad = 20

print(mayorEdad(20))
# print(mayorEdad(17))

# Algunas funciones predefinidas de python

# len, nos da la longitud de un texto, tupla, lista, etc
# print
# sum, suma los elementos de una lista o de una tupla.

lista = [1, 20, 15]
tupla = (1, 50, 14)

print(sum(lista)) # 36
print(sum(tupla)) # 65

# usando for dentro de una función

def listarElementos(una_lista):
    for x in una_lista:
        print(x)


listarElementos([1, True, 21.35, "Felino"])

# Parámetros con valores asignados por defecto.

def gretting(nombre="usuario invitado"):
    print(f"Bienvenido {nombre}")


gretting()
gretting("Max")


def saludando(nombre, mensaje="Hola"):
    print(f"{mensaje} {nombre}")


saludando("Buda", "Buenos días")
saludando("Anika")

# Variables globales, son las variables que van a poder ser accedidas desde fuera o dentro de las funciones, debe usarse la palabra clave "global"

# # global var_global

var_externa = "Externa"

def imprimir(variable):
    var_interna = "variable interna"
    print(f"soy una variable {variable}")
    print(var_interna)


imprimir(var_externa)

# imprimir(var_interna) # Error, variable no definida, ya que no se puede ver desde afuera es una variable local, que pertenece a la función.

def imprimir2(variable):
    global var_interna_global
    var_interna_global = "variable interna global"
    print(f"soy una variable {variable}")


imprimir2(var_externa) # Al ejecutar creamos la variable global var_interna_global
imprimir2(var_interna_global)


# Scope o ámbito de una variable

print("--------  SCOPE --------")

my_var = 20

def my_function():
    if my_var == 20:
        print("El valor es igual a 20")
    else:
        print("El valor no es 20")


my_function()


var2 = 25

def funcion2():
    var2 = 12 # variable local
    if var2 == 12:
        print("Es correcto")
    else:
        print("No es correcto")


funcion2()

def funcion3():
    var3 = 33
    if var3 == 33:
        print("Es 33")
    else:
        print("No es 33")

funcion3()

print(my_var)
print(var2)
# print(var3) # error, ya que no es accesible


# Número de Argumentos sin conocer

"""
Cuando el número de argumentos a pasarle a una función no se sabe a priori se procederá:

- a empaquetarlos en una tupla usando * antes de un nombre que querramos darle a esa tupla.
- a empaquetarlos en un diccionario usando ** antes de un nombre que querramos darle a ese diccionario.
"""

def mostrarArgumentos(*args):## args es un nombre convencional, pero puede ser cualquier otro que Ud. desee.
    print(f"EL número de argumentos pasadas a la función es: {len(args)}")
    print(type(args)) #
    for a in args:
        print(a)

mostrarArgumentos(20, True, [20, 10])


def mostrar_diccionario(**kwargs): # por convención se pone kwargs
    print(type(kwargs))
    print(kwargs)
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

mostrar_diccionario(nombre="Max", raza="Rottweiller", edad=2) # {"nombre": "Max", "raza": "Rottweiller", "edad": 2}


# Anotaciones en funciones, nos sirve de manera informátiva.

def duplicar(num: int) -> int:
    return 2 * num


print(duplicar(20))
print(duplicar("texto"))

# # https://ellibrodepython.com/funciones-en-python
