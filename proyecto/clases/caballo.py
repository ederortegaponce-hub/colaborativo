class Caballo:
    def __init__(self, raza, color, peso, estatura, edad):
        self.raza = raza
        self.color = color
        self.peso = peso
        self.estatura = estatura
        self.edad = edad

    def relinchar(self):
        print(f"El caballo de raza {self.raza} dice: ¡Hiii!")

    def correr(self, velocidad):
        print(f"El caballo está corriendo a {velocidad} km/h")

    def descripcion(self):
        print(f"Caballo: raza={self.raza}, color={self.color}, peso={self.peso}kg, "
              f"estatura={self.estatura}m, edad={self.edad} años")

    def cumplir_anios(self):
        self.edad += 1
        print(f"El caballo ahora tiene {self.edad} años")

# Ejemplo de uso
mi_caballo = Caballo('Árabe', 'Marrón', 500, 1.6, 7)
mi_caballo.descripcion()
mi_caballo.relinchar()
mi_caballo.correr(40)
mi_caballo.cumplir_anios()

