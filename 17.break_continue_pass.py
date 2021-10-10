# Control de bucles, break, continue y pass

# Break, ruptura. Permite salir de un ciclo dependiendo de una condición

print("------- BREAK --------")

for n in range(10):
    if n == 7:
        break

    print("El número es:" + str(n))

print("Fuera de el ciclo for")

# continue, omite parte de un ciclo dependiendo de una condicón, pero sigue con el resto del ciclo

print("------- CONTINUE --------")


for n in range(10):
    if n == 7:
        continue

    print("El número es:" + str(n))

print("Fuera de el ciclo for")

# pass
"""
- Es una operación nula, o sea que no pasa nada cuando se ejecuta.
- Se utiliza cuando se requiere por sintaxis una declaración pero no se quiere ejecutar ningún comando o código.
- También se utiliza en lugares donde donde el código irá finalmente, pero no ha sido escrita todavía (utilizándolo como un relleno temporal, hasta que se escriba el código final).
"""

print("---------- PASS -----------")

paises = ["Perú", "Argentina", "Bolivia", "Colombia"]

for p in paises:
    if(p == "Bolivia"):        
        #aquí irá ....
        pass

    print(p)
