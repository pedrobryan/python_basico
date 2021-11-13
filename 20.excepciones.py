# Manejo de excepciones
# Bloque try catch
"""
"""
# print(25/0)

a = 1

# b = int(input("Ingrese un número: "))
# a = a / b
# print("Resultado: ", a)

# try:
#     b = int(input("Ingrese un número: "))
#     a = a / b
#     print("Resultado: ", a)
# except:
#     print("Hubo un error")


# Capturando un error específico
# https://aprendeconalf.es/docencia/python/manual/excepciones/

# c = 1

# try:
#     d = int(input("Ingrese un número "))
#     c /= d # c = c / d
#     print("EL resultado es: ", c)

# except ZeroDivisionError:
#     print("El número que ingresaste es el cero y no está permitido la división entre cero")

# except ValueError:
#     print("Debes ingresar un valor numérico")

# # except (ZeroDivisionError, ValueError):
# #     print("HUbo un error en el dato o cero")

# except:    
#     print("Ocurrió un error")


# try except else

# else se ejecuta cuando no ocurre ninguna excepcion

# m = 1

# try:
#     n = int(input("Please enter a number to divide a"))
#     m = m/n
#     # print("algo")
# except ZeroDivisionError:
#     print("The number you provided cant divide 1 because it is 0")
# except ValueError:
#     print("You did not provide a number")
# except:
#     print("Something went wrong")
# else:
#     print("success m=",m)

# try except else finally

# finally se ejecuta siempre, haya error o no

# p = 1

# try:
#     q = int(input("Please enter a number to divide a"))
#     p = p/q
# except ZeroDivisionError:
#     print("The number you provided cant divide 1 because it is 0")
# except ValueError:
#     print("You did not provide a number")
# except:
#     print("Something went wrong")
# else:
#     print("success p=",p)
# finally:
#     print("Processing Complete")

correct = True
w = 1

while (correct):
    try:
        z = int(input("Ingrese un número "))
        w = w / z
        print(w)
        correct = False
    except:
        print("Hubo un Error")