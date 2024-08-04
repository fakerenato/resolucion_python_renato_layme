import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

circulo1 = CIRCULO(5)
circulo2 = CIRCULO(10)

area1 = circulo1.calcular_area()
area2 = circulo2.calcular_area()

print(area1)
print(area2)
