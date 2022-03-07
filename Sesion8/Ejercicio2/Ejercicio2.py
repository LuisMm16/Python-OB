import pickle

class Vehiculo:
    marca = ''
    color = ''
    motor = 0

    def __init__(self, marca, color, motor):
        self.marca = marca
        self.color = color
        self.motor = motor

    def getMarca(self):
        return self.marca

    def getColor(self):
        return self.color

    def getMotor(self):
        return self.motor


# Serializando
coche = Vehiculo('Ford', 'rojo', '2200')
f = open('coche.bin', 'wb')
pickle.dump(coche, f)
f.close()

# Recuperando objeto

f = open('coche.bin', 'rb')
coche_loaded = pickle.load(f)
f.close()
print('Despues de recuperar el archivo:')
print(f'El color del coche es {coche_loaded.getColor()}')