from geometria import CIRCULO, RECTANGULO, CUADRADO
from utilidades import validar_numero_positivo

def menu():
    while True:
        print("Menú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            radio = validar_numero_positivo(input("Ingrese el radio del círculo: "))
            if radio:
                circulo = CIRCULO(radio)
                print(f"El área del círculo es: {circulo.calcular_area()}")

        elif opcion == "2":
            largo = validar_numero_positivo(input("Ingrese el largo del rectángulo: "))
            ancho = validar_numero_positivo(input("Ingrese el ancho del rectángulo: "))
            if largo and ancho:
                rectangulo = RECTANGULO(largo, ancho)
                print(f"El área del rectángulo es: {rectangulo.calcular_area()}")

        elif opcion == "3":
            lado = validar_numero_positivo(input("Ingrese el lado del cuadrado: "))
            if lado:
                cuadrado = CUADRADO(lado)
                print(f"El área del cuadrado es: {cuadrado.calcular_area()}")

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    menu()

