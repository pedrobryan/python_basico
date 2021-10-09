# IF

"""

if(condición):
    --código a ejecutar si se cumple al condición
else:
    --código a ejecutarse si no se cumple la condición

"""

"""
La condición es un valor booleano, que puede ser directamente un valor o resultado de una operación que de por resutado un booleano
Recordemos que un booleano puede ser resultado de realizar operaciones de comparación o de operaciones lógicas
"""

# if ---- sin else

condicion = True

isActive = True

if(condicion == True):
    print("Se cumplió la condición")


if(isActive):
    print("Se cumplió la condición de isActive")

print("----------------------------")

# if-else

age = 17

if(age >= 18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("----------------------------")


# if anidado, usando "elif"

numero = 11

if(numero < 0):
    print("El número %d es menor que cero" % numero )
elif(numero <= 10):
    print(f"El número {numero} no es negativo y es menor de 10")
else:
    print("El número {} es mayor o igual a 10".format(numero))

print("----------------------------")

# # if anidado, usando más if dentro del if

entero = -1

if(entero >= 0):
    if(entero < 10):
        print(f"El número {entero} es no negativo y menor que diez")
    else:
        print(f"El número {entero} es mayor o igual a diez")
else:
    print(f"El número {entero} es negativo")

print("----------------------------")

# If con condiciones de operaciones lógicas, usar or, and, not

year = 2005


# if((year >= 2000) and (year <=2010)):
if(year >= 2000 and year <=2010):
    print("La canción fue escrita entre el año 2000 y el año 2010")    
else:
    print("La canción fue escrita antes del 2000 o después del 2010")

print("codigo fuera del if y del else")