# print(type(5))

# print("Hola" + 5)


# print("Hola" + "5")
print("Hola" + str(5))


# convertir otros tipos a float

# convertir un entero a real - de int a float

print("--------")
entero = 2
print(type(entero))
print(entero)
entero_a_real = float(entero)
print(entero_a_real)
print(type(entero_a_real))

# convertir una cadena a real - de str a float

numero_como_cadena = "5"
print(type(numero_como_cadena))
print(float(numero_como_cadena))

print(type(float(numero_como_cadena)))

# print(float("cadena"))

# convertir booleano a real - de bool a float

booleano = False
print(float(booleano)) # 0.0

print(float(True)) # 1.0

print("-------------")

# Convertir otros tipos a entero

decimal = 10.35
print(int(decimal))

print(int(booleano)) # 0
print(int(False)) # 0
print(int(True)) # 1

print(numero_como_cadena)
print(int(numero_como_cadena))

print(type(numero_como_cadena))
print(type(int(numero_como_cadena)))
# print(int("cadena"))


print("-----------")

# Convertir otros tipos a cadena
print(entero)
print(type(entero))

print(str(entero))
print(type(str(entero)))

print("-------")

print(decimal)
print(type(decimal))

print(type(str(decimal)))

print("-------")

print(booleano)
print(str(booleano))
print(type(str(booleano)))

print("---------")

# Convertir otros tipos a booleano o lógico

print(type(entero))
print(entero)

print(bool(entero)) # True

print(type(bool(entero)))
# print(bool(entero))
print(bool(-2)) # True
print(bool(0)) # False

print("----------")

print(decimal)

print(bool(decimal)) # True
print(bool(-10.35)) # True
print(bool(0.00)) # False

print("---------")

print(bool("Hola")) # True
print(bool("    ")) # True
print(bool("")) # False

# print("----------")