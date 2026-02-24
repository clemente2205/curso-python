"""Sistema de Inventario.

Este módulo implementa un sistema básico de gestión de inventario con:

- Clase Producto: representa un producto con nombre, precio y cantidad.
- Clase Inventario: gestiona una colección de productos.
- Función menu_principal: interfaz interactiva por consola.
"""


class Producto:
    """Representa un producto dentro del inventario."""

    def __init__(self, nombre: str, precio: float, cantidad: int):
        """Inicializa un producto con nombre, precio y cantidad.

        Parámetros
        ----------
        nombre : str
            Nombre del producto. No puede estar vacío.
        precio : float
            Precio del producto. Debe ser mayor o igual a cero.
        cantidad : int
            Cantidad disponible. Debe ser mayor o igual a cero.

        Excepciones
        -----------
        ValueError
            Si el nombre está vacío o si precio/cantidad son negativos.
        TypeError
            Si los tipos de datos no son los esperados.
        """
        nombre_limpio = nombre.strip() if isinstance(nombre, str) else ""

        if not nombre_limpio:
            raise ValueError("El nombre no puede estar vacío.")

        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser numérico.")

        precio_float = float(precio)
        if precio_float < 0:
            raise ValueError("El precio no puede ser negativo.")

        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un entero.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre_limpio
        self.precio = precio_float
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto.

        Parámetros
        ----------
        nuevo_precio : float
            Nuevo precio. Debe ser mayor o igual a cero.

        Excepciones
        -----------
        ValueError
            Si el precio es negativo.
        TypeError
            Si el valor no es numérico.
        """
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser numérico.")

        nuevo_precio_float = float(nuevo_precio)
        if nuevo_precio_float < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.precio = nuevo_precio_float

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto.

        Parámetros
        ----------
        nueva_cantidad : int
            Nueva cantidad. Debe ser mayor o igual a cero.

        Excepciones
        -----------
        ValueError
            Si la cantidad es negativa.
        TypeError
            Si el valor no es entero.
        """
        if not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un entero.")

        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        """Calcula el valor total del producto.

        Retorna
        -------
        float
            Resultado de multiplicar precio por cantidad.
        """
        return self.precio * self.cantidad

    def __str__(self):
        """Devuelve una representación legible del producto."""
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad}"


class Inventario:
    """Gestiona una colección de productos."""

    def __init__(self):
        """Inicializa un inventario vacío."""
        self.productos = []

    def agregar_producto(self, producto: Producto):
        """Agrega un producto al inventario.

        Parámetros
        ----------
        producto : Producto
            Objeto de tipo Producto a agregar.

        Excepciones
        -----------
        TypeError
            Si el objeto no es de tipo Producto.
        ValueError
            Si ya existe un producto con el mismo nombre.
        """
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")

        if any(p.nombre.lower() == producto.nombre.lower() for p in self.productos):
            raise ValueError("Ya existe un producto con ese nombre.")

        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        """Busca un producto por nombre.

        Parámetros
        ----------
        nombre : str
            Nombre del producto a buscar (insensible a mayúsculas).

        Retorna
        -------
        Producto | None
            El producto encontrado o None si no existe.

        Excepciones
        -----------
        ValueError
            Si el nombre está vacío.
        """
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise ValueError("El nombre a buscar no puede estar vacío.")

        for producto in self.productos:
            if producto.nombre.lower() == nombre_limpio.lower():
                return producto

        return None

    def calcular_valor_inventario(self):
        """Calcula el valor total del inventario.

        Retorna
        -------
        float
            Suma del valor total de todos los productos.
        """
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        """Muestra todos los productos registrados en el inventario."""
        if not self.productos:
            print("No hay productos en el inventario.\n")
            return

        print("\n--- Productos en el inventario ---")
        for i, producto in enumerate(self.productos, start=1):
            print(f"{i}. {producto}")
        print("")


def menu_principal(inventario: Inventario):
    """Muestra el menú principal y gestiona la interacción con el usuario.

    Parámetros
    ----------
    inventario : Inventario
        Instancia del inventario sobre la cual se realizarán las operaciones.
    """
    while True:
        print(
            "Sistema de Inventario\n"
            "1. Agregar producto\n"
            "2. Buscar producto\n"
            "3. Listar productos\n"
            "4. Calcular valor total del inventario\n"
            "5. Salir"
        )

        opc = input("Seleccione una opción (1-5): ").strip()

        if opc not in ["1", "2", "3", "4", "5"]:
            print("Error: Opción inválida. Debe ingresar un número del 1 al 5.\n")
            continue

        if opc == "1":
            try:
                nombre = input("Ingrese el nombre del producto: ").strip()
                precio = float(input("Ingrese el precio del producto: ").strip())
                cantidad = int(input("Ingrese la cantidad del producto: ").strip())

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)

                print(f"Producto '{producto.nombre}' agregado al inventario.\n")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}\n")

        elif opc == "2":
            try:
                nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
                producto = inventario.buscar_producto(nombre_buscar)

                if producto is None:
                    print("Producto no encontrado.\n")
                else:
                    print(f"Encontrado: {producto}\n")
            except ValueError as e:
                print(f"Error: {e}\n")

        elif opc == "3":
            inventario.listar_productos()

        elif opc == "4":
            total = inventario.calcular_valor_inventario()
            print(f"Valor total del inventario: ${total:.2f}\n")

        elif opc == "5":
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    """Punto de entrada del programa."""
    inventario = Inventario()
    menu_principal(inventario)
