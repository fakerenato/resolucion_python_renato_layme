from biblioteca.libro import Libro
from biblioteca.gestion import GestionBiblioteca

def menu():
    gestion = GestionBiblioteca()

    while True:
        print("\nMenú Biblioteca:")
        print("1. Agregar un libro")
        print("2. Listar los libros")
        print("3. Buscar un libro por título")
        print("4. Buscar un libro por autor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == "2":
            libros = gestion.listar_libros()
            if libros:
                print("Lista de libros en la biblioteca:")
                for libro in libros:
                    print(libro)
            else:
                print("No hay libros en la biblioteca.")

        elif opcion == "3":
            titulo = input("Ingrese el título del libro a buscar: ")
            libros = gestion.buscar_por_titulo(titulo)
            if libros:
                print("Libros encontrados:")
                for libro in libros:
                    print(libro)
            else:
                print("No se encontraron libros con ese título.")

        elif opcion == "4":
            autor = input("Ingrese el autor del libro a buscar: ")
            libros = gestion.buscar_por_autor(autor)
            if libros:
                print("Libros encontrados:")
                for libro in libros:
                    print(libro)
            else:
                print("No se encontraron libros de ese autor.")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")

if __name__ == "__main__":
    menu()
