# Descargando un archivo externo

# import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
# filename = 'Example.txt'
# urllib.request.urlretrieve(url, filename)

# Leyendo archivo de texto

# file = open("Example.txt")
# print(file.name)

example = "Example.txt"
file1 = open(example, "r") # r significa modo lectura y está por defecto, si ponemos w es para escritura
print(file1.name)

print(file1.mode) # ver el modo

fileContent = file1.read() # Leer el archivo.
print(fileContent)

print(type(fileContent)) # es de tipo str

file1.close() # cerramos el archivo

# Abrir el archivo usando "with"

with open("Example.txt", "r") as file2:# uso de alias
    f = file2.read()
    print(f)
# el archivo file2 fue cerrado

# Verificando si un archivo está cerrado
print(file1.closed)
print(file2.closed)
# aunque file2 está cerrado f guardo la lectura de file2
print(f)
print("****************")
print(fileContent)

# Leyendo solo unos caracteres

print("--------------")

with open(example) as f:
    print(f.read(4))# lee los primeros 4 caracteres y queda en la posición 4
    print(f.read(4))
    print(f.read(7))
    print(f.read(15))

print("**************")

with open(example, "r") as f:
    print(f.read(9))
    print(f.read(5))
    print(f.read(15))

# Leyendo líneas usando "readline()"

print("**********************")

with open(example) as f:
    print(f.readline())
    print(f.readline())


print("----------------")

with open(example) as f:
    print(f.readline(2)) # lee 2 caracteres
    print(f.read(5)) # lee los 5 caracteres que continuan

print("----------------")

# Iterando las líneas de un archivo

with open(example) as f:
    i = 0
    for line in f:
        print(str(i) + ": " + line) # print(f"{i}: {line}")
        i = i + 1 # i += 1


# Uso de readlines()

print("*****************")

with open(example) as f:
    print(f.readlines())


print("----------------")

with open(example) as f:
    fL = f.readlines() # guarda como una lista

print(type(fL))

print(fL[0]) # primera línea

print(fL[-1]) # Última línea