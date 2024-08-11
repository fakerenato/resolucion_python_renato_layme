import random
from pyfiglet import Figlet

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()

    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = figlet.getFonts()

    # Solicitar al usuario el nombre de la fuente a utilizar
    fuente_seleccionada = input("Ingrese el nombre de la fuente a utilizar (o presione Enter para seleccionar una aleatoria): ")

    # Si no se ingresa una fuente, seleccionar una fuente aleatoria
    if not fuente_seleccionada:
        fuente_seleccionada = random.choice(fuentes_disponibles)

    # Verificar si la fuente ingresada es válida
    if fuente_seleccionada not in fuentes_disponibles:
        print(f"Fuente '{fuente_seleccionada}' no válida. Seleccionando una fuente aleatoria.")
        fuente_seleccionada = random.choice(fuentes_disponibles)

    # Establecer la fuente seleccionada
    figlet.setFont(font=fuente_seleccionada)

    # Solicitar al usuario el texto a imprimir
    texto_imprimir = input("Ingrese el texto a imprimir: ")

    # Imprimir el texto utilizando la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()

