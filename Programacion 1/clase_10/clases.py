# cadena_a = "Juan" 
# cadena_b = "Ana"
# mi_lista = [1,2,3]

# print(type(cadena_a))
# print(type(cadena_b))

# cadena_a.upper() # Existe
# cadena_b.upper() # Existe
# mi_lista.upper() # -> No existe


class Animal: # Clase Padre
    def __init__(self, tipo, cant_patas):
        self.tipo = tipo
        self.cant_patas = cant_patas

class Gato(Animal): # Clase Hija
    def __init__(self, tipo, cant_patas, name, race, colour): # Funcion constructora ->>> _ _ init _ _
        super().__init__(tipo, cant_patas)
        self.nombre = name # Atributos
        self.raza = race
        self.color = colour
    
    def maullar(self):
        return "Miau"

class Perro(Animal): # Clase Hija
    def __init__(self, tipo, cant_patas, name, race, colour): # Funcion constructora ->>> _ _ init _ _
        super().__init__(tipo, cant_patas)
        self.nombre = name # Atributos
        self.raza = race
        self.color = colour

    def ladrar(self):
        return "Woof"
    
    def retornar_descripcion(self):
        return f"Mi nombre es {self.nombre}, soy de la raza {self.raza} y mi color es {self.color}, tengo {4} patas y soy del tipo {self.tipo}"

mi_perrito = Perro("Carnivoro", 4, "Bobby", "Caniche", "Negro") # Creacion de una instancia
mi_gatito = Gato("Carnivoro", 4, "Pepe", "Siames", "Blanco") 

print(mi_perrito.ladrar())
print(mi_gatito.maullar())



# print(mi_perrito.nombre)

# # print(mi_perrito) 
# # print(mi_segundo_perrito.nombre)
# # print(type(mi_perrito))
print(mi_perrito.retornar_descripcion())

# class Perro: 
#     def __init__(self, name, race, colour):
#         self.__nombre = name
#         self.raza = race
#         self.color = colour

#     def get_nombre(self):
#         return self.__nombre
    
#     def set_nombre(self, nombre):
#         self.__nombre = nombre
    
# mi_perrito = Perro("Bobby", "Caniche", "Negro") 

# print(mi_perrito.get_nombre())
# mi_perrito.set_nombre("Pepe")
# print(mi_perrito.get_nombre())