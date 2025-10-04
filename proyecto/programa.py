#Aqui va el codigo de su programa
#En la carpeta clases iran 5 clases con al menos 5 atributos para mostrar en pantallas
#Debera generar su rama por equipo.s

from clases import Avion
from clases import Pastel

import tkinter as tk
from tkinter import ttk

class Avion:
    def __init__(self, cargamento, capacidad, tamaño, modelo, color):
        self.cargamento = cargamento
        self.capacidad = capacidad
        self.tamaño = tamaño
        self.modelo = modelo
        self.color = color
    
    def mostrar_info(self):
        return (
            f"--- Información de avión ---\n"
            f"Cargamento: {self.cargamento}\n"
            f"Capacidad: {self.capacidad}\n"
            f"Tamaño: {self.tamaño}\n"
            f"Modelo: {self.modelo}\n"
            f"Color: {self.color}\n"
        )


class Pastel:
    def __init__(self, tamaño, sabor, decoración, capas, tipo_glaseado, color):
        self.tamaño = tamaño         
        self.sabor = sabor            
        self.decoración = decoración  
        self.capas = capas            
        self.tipo_glaseado = tipo_glaseado 
        self.color = color           
    
    def preparar(self):
        print(f"Preparar el pastel {self.color} de {self.sabor}...")
    
    def decorar(self):
        print(f"Decorar el pastel con {self.decoración} y {self.capas} capas.")
    
    def aplicar_glasé(self):
        print(f"Añadir glaseado de {self.tipo_glaseado} al pastel.")
    
    def servir(self):
        print(f"Un pastel {self.color} de tamaño {self.tamaño}, con {self.capas} capas y glaseado de {self.tipo_glaseado} está por servirse. ;)")

    def mostrar_info(self):
        return f"Pastel {self.color}:\nTamaño: {self.tamaño}\nSabor: {self.sabor}\nDecoración: {self.decoración}\nCapas: {self.capas}\nTipo de glaseado: {self.tipo_glaseado}\nColor: {self.color}"



Avion_American_Airlines = Avion(
    "Personas y maletas",
    "Entre 150 y 180 personas y más de 100 kg de equipaje",
    "Su tamaño ronda los 38m",
    "Airbus A320",
    "En su mayoría blancos con azul"
)

Avion_United_Airlines = Avion(
    "Personas y maletas",
    "Entre 150 y 180 personas y más de 100 kg de equipaje",
    "Longitud aprox. 39.5m, envergadura 35.8m, altura de cola 12.5m",
    "Boeing 737",
    "En su mayoría blancos con azul"
)


def mostrar_avion(avion):
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, avion.mostrar_info())
    text_area.config(state="disabled")


def crear_pastel():
    tamaño = entry_tamaño.get()
    sabor = entry_sabor.get()
    decoración = entry_decoración.get()
    capas = int(entry_capas.get())
    tipo_glaseado = entry_glaseado.get()
    color = entry_color.get()

    pastel = Pastel(tamaño, sabor, decoración, capas, tipo_glaseado, color)

    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, pastel.mostrar_info())
    text_area.config(state="disabled")
    

ventana = tk.Tk()
ventana.title("Información de Aviones y Pasteles")
ventana.geometry("800x600")
ventana.configure(bg="#2c3e50")

frame_aviones = tk.Frame(ventana, bg="#34495e", padx=20, pady=10)
frame_aviones.pack(fill="x", padx=10, pady=10)

title_label_aviones = tk.Label(
    frame_aviones, text="Información de Aviones", font=("Helvetica", 16, "bold"), fg="white", bg="#34495e"
)
title_label_aviones.pack(pady=5)

button_frame_aviones = tk.Frame(frame_aviones, bg="#34495e")
button_frame_aviones.pack(pady=10, fill="x")

btn_american = ttk.Button(button_frame_aviones, text="Avión American Airlines", command=lambda: mostrar_avion(Avion_American_Airlines))
btn_american.pack(side="left", expand=True, padx=10)

btn_united = ttk.Button(button_frame_aviones, text="Avión United Airlines", command=lambda: mostrar_avion(Avion_United_Airlines))
btn_united.pack(side="left", expand=True, padx=10)

frame_pasteles = tk.Frame(ventana, bg="#34495e", padx=20, pady=10)
frame_pasteles.pack(fill="x", padx=10, pady=10)

title_label_pasteles = tk.Label(
    frame_pasteles, text="Crear tu Pastel", font=("Helvetica", 16, "bold"), fg="white", bg="#34495e"
)
title_label_pasteles.pack(pady=5)

tk.Label(frame_pasteles, text="Tamaño:", bg="#34495e", fg="white").pack()
entry_tamaño = tk.Entry(frame_pasteles)
entry_tamaño.pack()

tk.Label(frame_pasteles, text="Sabor:", bg="#34495e", fg="white").pack()
entry_sabor = tk.Entry(frame_pasteles)
entry_sabor.pack()

tk.Label(frame_pasteles, text="Decoración:", bg="#34495e", fg="white").pack()
entry_decoración = tk.Entry(frame_pasteles)
entry_decoración.pack()

tk.Label(frame_pasteles, text="Capas:", bg="#34495e", fg="white").pack()
entry_capas = tk.Entry(frame_pasteles)
entry_capas.pack()

tk.Label(frame_pasteles, text="Tipo de glaseado:", bg="#34495e", fg="white").pack()
entry_glaseado = tk.Entry(frame_pasteles)
entry_glaseado.pack()

tk.Label(frame_pasteles, text="Color:", bg="#34495e", fg="white").pack()
entry_color = tk.Entry(frame_pasteles)
entry_color.pack()

tk.Button(frame_pasteles, text="Crear Pastel", command=crear_pastel).pack(pady=10)

text_frame = tk.Frame(ventana)
text_frame.pack(pady=20, padx=20, fill="both", expand=True)

text_area = tk.Text(
    text_frame, wrap="word", font=("Consolas", 12), bg="#ecf0f1", fg="#2c3e50", relief="flat", bd=2
)
text_area.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(text_frame, command=text_area.yview)
scrollbar.pack(side="right", fill="y")

text_area.config(yscrollcommand=scrollbar.set)
text_area.insert("1.0", "Selecciona un avión o crea un pastel para mostrar su información.")
text_area.config(state="disabled")

ventana.mainloop()

import tkinter as tk

class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} | Color: {self.color} | Velocidad: {self.velocidad} km/h"


def mostrar_info_coche(coche, etiqueta):
    etiqueta.config(text=coche.mostrar_info())

def acelerar_coche(coche, etiqueta):
    coche.acelerar(10)
    mostrar_info_coche(coche, etiqueta)

def frenar_coche(coche, etiqueta):
    coche.frenar(10)
    mostrar_info_coche(coche, etiqueta)


ventana = tk.Tk()
ventana.title("Coches con Tkinter")

mi_coche_rojo = Coche("Lamborghini", "Huracán", "Rojo")
coche_amigo = Coche("Honda", "Civic", "Azul")

etiqueta1 = tk.Label(ventana, text=mi_coche_rojo.mostrar_info(), font=("Arial", 10))
etiqueta1.pack(pady=5)

tk.Button(ventana, text="Acelerar coche rojo", command=lambda: acelerar_coche(mi_coche_rojo, etiqueta1)).pack()
tk.Button(ventana, text="Frenar coche rojo", command=lambda: frenar_coche(mi_coche_rojo, etiqueta1)).pack()

etiqueta2 = tk.Label(ventana, text=coche_amigo.mostrar_info(), font=("Arial", 10))
etiqueta2.pack(pady=5)

tk.Button(ventana, text="Acelerar coche azul", command=lambda: acelerar_coche(coche_amigo, etiqueta2)).pack()
tk.Button(ventana, text="Frenar coche azul", command=lambda: frenar_coche(coche_amigo, etiqueta2)).pack()

ventana.mainloop()
