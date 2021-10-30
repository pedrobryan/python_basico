# Escribir una línea

example = "Example2.txt"

with open(example, "w") as w:
    w.write("this is line A") # va a sobreescribirlo si existe ese archivo, con w si no hay archivo lo crea.

with open(example) as r:
    f = r.read()

print(f)

print("*********************")

with open("Example3.txt", "w") as w:
    w.write("This is line A\n")
    w.write("This is line B\n")

with open("Example3.txt") as r:
    print(r.read())

# Escribiendo los elementos(strings) de una Lista

Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open("Example4.txt", "w") as w:
    for line in Lines:
        w.write(line)

print("*************************")

f4 = open("Example4.txt").read()
print(f4)

# Agregando texto sin reemplazar lo anterior, usando el modo "a"

with open("Example3.txt", "a") as f:
    f.write("this is line C\n")
    f.write("this is line D\n")
    f.write("this is line E\n")


print("***********************")
print(open("Example3.txt").read())

# *************************************
# Modos adicionales

# r+  ---> Leyendo y escribiendo sin truncar el archivo
# w+  ---> Escribiendo y leyendo truncando el archivo
# a+  ---> Agregando y leyendo si no hay un archivo lo crea.

print("************-----***************")

with open("Example4.txt", "a+") as twf:
    twf.write("this is line D\n")
    print(twf.read())

# Veremos que no se logra ver la lectura del archivo, eso pasa porque el cursor de escritura dejó el cursor al final.

print("------------*********************-----------")

print(open("Example4.txt").read()) # aquí si funciona pero si deseamos que funcione con a+ se tiene métodos que nos ayudarán con ello.

# tell()   ---> Regresa la posición actual en bytes
# seek(offset, from)  ---> cambia la posición en bytes en "offset" ponemos cuanto a referencia de lo puesto en "from"

with open("Example4.txt", "a+") as twf:

    print("posición actual: {}".format(twf.tell()))  # el cursor está al final

    data = twf.read()

    if(not data):
        print("No se muestra nada")
    else:
        print(data)

    twf.seek(0, 0)
    print("Nueva posición actual: {}".format(twf.tell())) 

    data = twf.read()

    if(not data):
        print("No se muestra nada")
    else:
        print(data)

    print("Nueva posición actual después de read: {}".format(twf.tell())) 

# Finalmente, una nota sobre la diferencia entre w+ y r+. Ambos modos permiten el acceso a métodos de lectura y escritura, sin embargo, abrir un archivo en w+ lo sobrescribe y borra todos los datos preexistentes.
# Para trabajar con un archivo con datos existentes, use r+ y a+. Mientras usa r+, puede ser útil agregar un método .truncate () al final de sus datos. Esto reducirá el archivo a sus datos y eliminará todo lo que sigue.
# En el siguiente bloque de código, primero ejecute el código como está y luego ejecútelo con .truncate ().

print("************* r+ *******************")

with open("Example4.txt", "r+") as twf:
    data = twf.readlines()
    print(data)
    twf.seek(0, 0) # probar comentado
    print(twf.tell())

    twf.write("Line 1" + "\n")
    twf.write("Line 2" + "\n")
    twf.write("Line 3" + "\n")
    twf.write("finished\n")

    print(twf.tell())
    twf.truncate() # probar comentado, borra el texto que sigue a la posición actual del cursor.
    twf.seek(0, 0) # probar comentado
    print(twf.read())


# Copiando un archivo en uno nuevo.

with open("Example4.txt") as rf:
    with open("Example5.txt", "w") as wf:
        for line in rf:
            wf.write(line)

    
print(open("Example5.txt").read())