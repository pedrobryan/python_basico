#----------------- Formateo e interpolación ----------------------

nombre = "Max"

edad = 2

print("Hola " + nombre) # Hola Max

# 1era forma usando %, válido para python2 y python3 (formateo antiguo)

print("Hola %s" % nombre) # Hola Max
 
print("%s tiene %d años" % (nombre, edad)) # Max tiene 2 años

# tupla = "Buda", 3

# print("%s" % tupla) # da error

# print("%s" %(tupla,))

"""
%s para textos(str), si pasamos un entero o decimal en vez de texto, python usará str() para convertirlo internamente
%d para enteros(int)
%f para decimales(float)
"""

print("%s tiene %s años" % (nombre, edad)) # print("%s tiene %s años" % (nombre, str(edad)))

"""
- Si usamos %.2f le decimos que solo muestre 2 decimales, asi %.3f para tres deecimales y así ...
- Si deseamos que a un numero positivo sin signo le ponga el signo + usamos %+d, %+f
- Para mostrar un número como hexadecimal usamos %x o %X, si usamos %#x nos da 0x además del hexadecimal y lo propio para %#X agrega 0X 
"""

print("El precio es: %.2f" % 2.5878) # redondea a 2 decimales 2.59
# print("El precio es: %.2f" % (2.5878))
print("El número es: %+d" % 5) #  +5
# print("El número es: %+d" % (5))
print("El decimal es: %+f" % 10)
# print("El decimal es: %+f" % (10))
print("el número decimal es: %+.2f" % (10))
# print("el número decimal es: %+.2f" % 10)
print("%x" % 11) # b
print("%X" % 11) # B
print("%#x" % 11) # 0xb
print("%#X" % 11) # 0XB
print("0x%X" % 11) # 0xB

print("%3d" % 5) #   epacioespacio5

print("%03d" % 9) # 009

# 2da forma, formateo de cadena de nuevo estilo
# funciona en python3 y agregado a python2.7

print("Hola {}".format(nombre)) # Hola Max

print("{} tiene {} años".format(nombre, edad)) # Max tiene 2 años

print("{name} tiene {age} años".format(name=nombre, age=edad)) # Max tiene 2 años

# print("{nombre} tiene {edad} años".format(nombre=nombre, edad=edad))

# usando índice

print("{0} tiene {1} años. {0} ladra muy fuerte".format(nombre, edad)) # Max tiene 2 años. Max ladra muy fuerte

# # # 

print("{tot:.2f}".format(tot=25.36789)) # redondea a 25.37

print("{:x}".format(10)) # a
print("{:X}".format(10)) # A
 
print("{:+}".format(20)) # +20

# print("{0:+}".format(9))

print("{0:5}".format(7)) # espacioespacioespacioespacio7

# print("{:5}".format(7))

print("{:>5}".format(7)) # alineación a la derecha

# print("{0:>5}".format(7))

print("{:<5}".format(7)) # alineacion a la izquierda

print("{0:^5}".format(7)) # alineación al centro # ALT + 94

print("{:05}".format(7)) # 0007


# # 3ra forma, interpolación de cadenas - cadenas f - python 3.6+

# nos permite escribir código python dentro de un string

print(f"Hola {nombre}")

num = 2

a = 5
b= 3

print(f"El total es {round(20.3678, 2)}") # El total es 20.37

print(f"{nombre} tiene {2 * num} amigos, 5 + 3 es {a + b}, 12578 - 3541 es {12578 - 3541}")

print(f"{15:05}") #  00015

print(f"{25:.2f}") # 25.00


# 4ta forma -  Uso de Template del módulo string, su uso se recomienda para temas de seguridad

from string import Template # este módulo está presente en las bibliotecas estándar

t = Template("Hola $nombre!")
T = t.substitute(nombre=nombre)

print(T) #

# # https://recursospython.com/guias-y-manuales/formateo-de-cadenas/

# # https://realpython.com/python-string-formatting/?fbclid=IwAR1_NAHEB2khthrNgMOLjIbFLff90w1df4Yz10N0nuGUXamaYF05z4_53Ys

# # https://pybonacci.org/2020/02/05/formateando-texto-en-python/

# # https://programmerclick.com/article/2030946467/