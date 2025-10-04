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
