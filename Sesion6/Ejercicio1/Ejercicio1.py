# Crear una clase generica vehiculo con sus atributos y una clase coche que hereda de vehiculo

class Vehiculo:
    color = "Verde"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 6

miCoche = Coche()
print(miCoche)