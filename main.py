# LABORATORIO 7 - Proyecto integrador
# Sistema básico de inventario de productos

productos = []


def cargar_productos():
    try:
        archivo = open("inventario.txt", "r", encoding="utf-8")

        for linea in archivo:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                producto = {
                    "nombre": datos[0],
                    "precio": float(datos[1]),
                    "stock": int(datos[2])
                }
                productos.append(producto)

        archivo.close()

    except FileNotFoundError:
        print("No existe un archivo anterior. Se iniciará un inventario nuevo.")


def guardar_productos():
    archivo = open("inventario.txt", "w", encoding="utf-8")

    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['stock']}\n"
        archivo.write(linea)

    archivo.close()


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)
    guardar_productos()

    print("Producto registrado correctamente.")


def listar_productos():
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        print("LISTA DE PRODUCTOS")
        for producto in productos:
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Stock:", producto["stock"])
            print("----------------------")


def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("Producto encontrado:")
            print("Nombre:", producto["nombre"])
            print("Precio:", producto["precio"])
            print("Stock:", producto["stock"])
            encontrado = True

    if not encontrado:
        print("Producto no encontrado.")


def menu():
    opcion = 0

    while opcion != 4:
        print("\nSISTEMA DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            listar_productos()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            print("Programa finalizado.")
        else:
            print("Opción no válida.")


cargar_productos()
menu()