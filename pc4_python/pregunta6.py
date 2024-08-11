def contar_lineas_codigo(ruta_archivo):
    try:
        # Verificar que el archivo tiene la extensión .py
        if not ruta_archivo.endswith(".py"):
            print("El archivo no es un archivo .py válido.")
            return
        
        with open(ruta_archivo, 'r') as file:
            lineas = file.readlines()
        
        lineas_codigo = 0
        
        for linea in lineas:
            linea = linea.strip()
            # Ignorar líneas en blanco o líneas que son solo comentarios
            if linea and not linea.startswith("#"):
                lineas_codigo += 1
        
        print(f"El archivo '{ruta_archivo}' tiene {lineas_codigo} líneas de código.")
    
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no existe.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Contar líneas de código en un archivo .py")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ruta_archivo = input("Ingrese la ruta y nombre del archivo .py: ")
            contar_lineas_codigo(ruta_archivo)
        
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
