#Es el 11 convertido a funciones

def mostrar_menu():
    print("\nMenú de la lista de la compra")
    print("1. Crear nueva lista de la compra")
    print("2. Añadir un producto")
    print("3. Eliminar un producto")
    print("4. Contar productos en la lista")
    print("5. Añadir varios productos")
    print("6. Borrar toda la lista")
    print("7. Ordenar la lista de la compra")
    print("8. Calcular el importe total")
    print("9. Mostrar la lista de la compra")
    print("0. Salir")

# Listas para almacenar los datos
productos = []
precios = []
cantidades = []

def crear_lista():
    global productos, precios, cantidades
    productos = []
    precios = []
    cantidades = []
    print("Lista de la compra creada.")

def agregar_producto():
    producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad a comprar: "))
    
    productos.append(producto)
    precios.append(precio)
    cantidades.append(cantidad)
    print(f"{producto} añadido correctamente.")

def eliminar_producto():
    producto = input("Nombre del producto a eliminar: ")
    if producto in productos:
        indice = productos.index(producto)
        productos.pop(indice)
        precios.pop(indice)
        cantidades.pop(indice)
        print(f"{producto} eliminado correctamente.")
    else:
        print("El producto no está en la lista.")

def contar_productos():
    print(f"Total de productos en la lista: {len(productos)}")

def agregar_varios_productos():
    n = int(input("¿Cuántos productos quieres añadir? "))
    for _ in range(n):
        agregar_producto()

def borrar_lista():
    global productos, precios, cantidades
    productos.clear()
    precios.clear()
    cantidades.clear()
    print("Lista de la compra vaciada.")

def ordenar_lista():
    criterio = input("Ordenar por precio (p) o por cantidad (c): ").lower()
    if criterio == "p":
        datos = sorted(zip(precios, productos, cantidades))
    elif criterio == "c":
        datos = sorted(zip(cantidades, productos, precios))
    else:
        print("Opción no válida.")
        return
    
    precios[:], productos[:], cantidades[:] = zip(*datos)
    print("Lista ordenada correctamente.")

def calcular_importe_total():
    total = sum(precio * cantidad for precio, cantidad in zip(precios, cantidades))
    print(f"Importe total de la compra: {total:.2f} €")

def mostrar_lista():
    if not productos:
        print("La lista de la compra está vacía.")
        return

    print("\nLista de la compra:")
    for i in range(len(productos)):
        print(f"{productos[i]} - {cantidades[i]} unidades - {precios[i]:.2f} € c/u")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        crear_lista()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        contar_productos()
    elif opcion == "5":
        agregar_varios_productos()
    elif opcion == "6":
        borrar_lista()
    elif opcion == "7":
        ordenar_lista()
    elif opcion == "8":
        calcular_importe_total()
    elif opcion == "9":
        mostrar_lista()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
