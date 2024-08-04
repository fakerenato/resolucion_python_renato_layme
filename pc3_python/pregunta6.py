class Producto:
    def __init__(self, nombre, precio, año, categoria):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.categoria = categoria

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}, Categoría: {producto.categoria}")

    def filtrar_por_año(self, año):
        return [producto for producto in self.productos if producto.año == año]

    def filtrar_por_categoria(self, categoria):
        return [producto for producto in self.productos if producto.categoria == categoria]


producto1 = Producto("Filtro de aire", 20.0, 2022, "Filtros")
producto2 = Producto("Bujía", 15.0, 2023, "Encendido")
producto3 = Producto("Aceite de motor", 35.0, 2022, "Lubricantes")


catalogo = Catalogo()
catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)


catalogo.mostrar_productos()

productos_2022 = catalogo.filtrar_por_año(2022)
print("Productos del año 2022:")
for producto in productos_2022:
    print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}, Categoría: {producto.categoria}")


productos_filtros = catalogo.filtrar_por_categoria(
