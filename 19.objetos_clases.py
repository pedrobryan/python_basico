"""
Las clases son como un molde de objetos existentes(ejm clase perro), esos moldes cuando son creados son llamados objetos(instanciación de una clase, ejemplo Bobby)

los objetos poseen propiedades o caracteristicas(ejemplo: color, raza, edad, etc.)
Los objetos poseen comportamientos o métodos(comer, ladrar, saltar, etc.)

La programación orientada a objetos está basada en 6 principios o pilares básicos:

Herencia
Cohesión
Abstracción
Polimorfismo
Acoplamiento
Encapsulamiento
"""

# Definiendo una clase

class Auto(): # Clase vacía y sin parámetros
    pass

# Instanciando la clase o creando un objeto

mi_auto = Auto()

# Definiendo atributos


# atributos de instancia

class Perro:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):# método mágico __init__ sirve de constructor, es decir que se ejecutará al instanciar a la clase. el self hace referencia al objeto en sí.
        print(f"El perro se llama {nombre} y es de raza: {raza}")

        #atributos de instancia

        self.nombre = nombre # self.nombre es un atributo de instancia, aunque aquí causa confusión ya que tieen el mismo nombre del parámetro, en realidad podriamos poner cualquer otro nombre.
        self.raza = raza

        print(self.nombre)


mi_perro = Perro("Scooby", "Gran Danés")

print(mi_perro.raza) # viendo el valor del atributo raza del objeto mi_perro
print(type(mi_perro))

# atributos de clase

class Perro2:
    # Atributo de clase, no es necesario crear un objeto(instanciar la clase para poder acceder a él)
    especie = "Mamífero"

    def __init__(self, nombre, raza):
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza


print(Perro2.especie)

mi_perro2 = Perro2("Max", "LabraRott")

print(mi_perro2.especie) # también se puede acceder a un atributo de clase a través de una instancia

mi_perro.nombre = "Scooby Doo"
print(mi_perro.nombre)

mi_perro2.especie = "Ave"
print(mi_perro2.especie)

print(Perro2.especie)
Perro2.especie = "Reptil"
print(Perro2.especie)

# definiendo otros métodos

class Perro3:
    especie = "Mamífero"

    def __init__(self, nombre, raza):
        self.name = nombre
        self.breed = raza

    def ladrar(self):# el uso de self es obligatorio
        print("Guau")

    def caminar(self, pasos):
        print(f"{self.name} camina {pasos} pasos")


mi_perro3 = Perro3("Buda", "Collie cruzado")
mi_perro3.ladrar()
mi_perro3.caminar(3)


# https://ellibrodepython.com/cohesion-en-programacion