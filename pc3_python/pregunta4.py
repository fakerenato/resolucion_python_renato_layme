class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

rectangulo = RECTANGULO(4, 6)
cuadrado = CUADRADO(4)

area_rectangulo = rectangulo.calcular_area()
area_cuadrado = cuadrado.calcular_area()

print(area_rectangulo)
print(area_cuadrado)
