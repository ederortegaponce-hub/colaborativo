#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s

import tkinter as tk
from tkinter import messagebox

# -----------------------------
# CLASES DE ANIMALES
# -----------------------------

class Gato:
    def __init__(self, nombre, color, edad, raza, peso, domestico=True):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.domestico = domestico

    def descripcion(self):
        return (f"Gato\nNombre: {self.nombre}\nColor: {self.color}\nEdad: {self.edad} años\n"
                f"Raza: {self.raza}\nPeso: {self.peso} kg\n¿Doméstico?: {'Sí' if self.domestico else 'No'}")

class Perro:
    def __init__(self, nombre, raza, edad, color, tamaño, sexo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.tamaño = tamaño
        self.sexo = sexo

    def descripcion(self):
        return (f"Perro\nNombre: {self.nombre}\nRaza: {self.raza}\nEdad: {self.edad} años\n"
                f"Color: {self.color}\nTamaño: {self.tamaño}\nSexo: {self.sexo}")

class Aguila:
    def __init__(self):
        self.nombre = "Águila"
        self.tipo = "Ave rapaz"
        self.envergadura = "Hasta 2.5 metros"
        self.color = "Marrón oscuro con cabeza blanca"
        self.habitat = "Montañas, bosques, praderas y zonas abiertas"
        self.alimentacion = "Carnívora: caza peces, mamíferos y aves"

    def descripcion(self):
        return (f"{self.nombre}\nTipo: {self.tipo}\nEnvergadura: {self.envergadura}\nColor: {self.color}\n"
                f"Hábitat: {self.habitat}\nAlimentación: {self.alimentacion}")

class Conejo:
    def __init__(self):
        self.nombre = "Conejo"
        self.tipo = "Mamífero"
        self.tamano = "Entre 20 y 50 cm"
        self.color = "Blanco, marrón, gris o negro"
        self.habitat = "Bosques, praderas y áreas rurales"
        self.alimentacion = "Herbívoro: pasto, hierbas y vegetales"

    def descripcion(self):
        return (f"{self.nombre}\nTipo: {self.tipo}\nTamaño: {self.tamano}\nColor: {self.color}\n"
                f"Hábitat: {self.habitat}\nAlimentación: {self.alimentacion}")

class Caballo:
    def __init__(self, raza, color, peso, estatura, edad):
        self.raza = raza
        self.color = color
        self.peso = peso
        self.estatura = estatura
        self.edad = edad

    def descripcion(self):
        return (f"Caballo\nRaza: {self.raza}\nColor: {self.color}\nPeso: {self.peso} kg\n"
                f"Estatura: {self.estatura} m\nEdad: {self.edad} años")

class Tiburon:
    def __init__(self, edad, tamaño, peso, raza, comportamiento):
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.raza = raza
        self.comportamiento = comportamiento

    def descripcion(self):
        return (f"Tiburón\nEdad: {self.edad} años\nTamaño: {self.tamaño}\nPeso: {self.peso} toneladas\n"
                f"Raza: {self.raza}\nComportamiento: {self.comportamiento}")

class Serpiente:
    def __init__(self, nombre, especie, edad, color, tamaño, venenosa):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
        self.tamaño = tamaño
        self.venenosa = venenosa

    def descripcion(self):
        return (f"Serpiente\nNombre: {self.nombre}\nEspecie: {self.especie}\nEdad: {self.edad} años\n"
                f"Color: {self.color}\nTamaño: {self.tamaño}\nVenenosa: {'Sí' if self.venenosa else 'No'}")

# -----------------------------
# VENTANA CON TKINTER
# -----------------------------

def mostrar_info(animal):
    messagebox.showinfo("Información del animal", animal.descripcion())

# Crear ventana
ventana = tk.Tk()
ventana.title("Animales")
ventana.geometry("300x400")

# Crear objetos
mi_gato = Gato("Luna", "Gris", 3, "Persa", 4.2)
mi_perro = Perro("Dayra", "Chihuahua", 2, "Marrón y blanco", "Pequeña", "Hembra")
mi_aguila = Aguila()
mi_conejo = Conejo()
mi_caballo = Caballo("Árabe", "Marrón", 500, 1.6, 7)
mi_tiburon = Tiburon(5, "10 mts", 1.5, "Blanco", "Tranquilo")
mi_serpiente = Serpiente("Kaa", "Boa Constrictor", 4, "Verde y marrón", "Grande", False)

# Botones
tk.Button(ventana, text="Ver Gato", command=lambda: mostrar_info(mi_gato)).pack(pady=5)
tk.Button(ventana, text="Ver Perro", command=lambda: mostrar_info(mi_perro)).pack(pady=5)
tk.Button(ventana, text="Ver Águila", command=lambda: mostrar_info(mi_aguila)).pack(pady=5)
tk.Button(ventana, text="Ver Conejo", command=lambda: mostrar_info(mi_conejo)).pack(pady=5)
tk.Button(ventana, text="Ver Caballo", command=lambda: mostrar_info(mi_caballo)).pack(pady=5)
tk.Button(ventana, text="Ver Tiburón", command=lambda: mostrar_info(mi_tiburon)).pack(pady=5)
tk.Button(ventana, text="Ver Serpiente", command=lambda: mostrar_info(mi_serpiente)).pack(pady=5)

# Iniciar ventana
ventana.mainloop()
