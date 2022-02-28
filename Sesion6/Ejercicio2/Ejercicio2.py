# Crear clase alumno con dos atributos y metodos getter de nombre, nota y si esta aprobado

class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def getNombre(self):
        print(f'El nombre del alumno es {self.nombre}')

    def getNota(self):
        print(f'La nota es {self.nota}')

    def getAprobado(self):
        if self.nota >= 14:
            print(f'El alumno {self.nombre} tiene como nota {self.nota}, por lo tanto está aprobado')
        else:
            print(f'El alumno {self.nombre} tiene como nota {self.nota}, por lo tanto está desaprobado')


# Prueba:

alumno = Alumno("Luis", 13)
alumno.getNombre()
alumno.getNota()
alumno.getAprobado()
