# Calcular el área de un triángulo
import math

def area_triangulo(base, altura):
    return base * altura / 2

def area_circulo(radio):
    return math.pi * radio ** 2

#Pruebas:
print("El area del triángulo es: " + str(area_triangulo(3, 4)))
print("El area del circulo es: " + str(round(area_circulo(2),2)))