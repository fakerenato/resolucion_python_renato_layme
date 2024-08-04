class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = None

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas is not None:
            print(f"Notas: {self.notas}")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

alumno1 = Alumno("Juan", 12345)
alumno1.setAge(20)
alumno1.setNota([85, 90, 78])
alumno1.display()

