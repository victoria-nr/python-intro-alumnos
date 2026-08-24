
    
# Listas para almacenar los datos
productos = []
precios = []
cantidades = []



# Bucle principal del programa
while True:
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

    opcion = input("Elige una opción: ")

    if opcion == "1":
        
        productos = []
        precios = []
        cantidades = []
        print("Lista de la compra creada.")

    elif opcion == "2":
        producto = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad a comprar: "))
    
        productos.append(producto)
        precios.append(precio)
        cantidades.append(cantidad)
        print(f"{producto} añadido correctamente.")

    elif opcion == "3":
        producto = input("Nombre del producto a eliminar: ")
        if producto in productos:
            indice = productos.index(producto)
            productos.pop(indice)
            precios.pop(indice)
            cantidades.pop(indice)
            print(f"{producto} eliminado correctamente.")
        else:
            print("El producto no está en la lista.")

    elif opcion == "4":
        print(f"Total de productos en la lista: {len(productos)}")

    elif opcion == "5":
        n = int(input("¿Cuántos productos quieres añadir? "))
        for _ in range(n):
            producto = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad a comprar: "))
    
            productos.append(producto)
            precios.append(precio)
            cantidades.append(cantidad)
            print(f"{producto} añadido correctamente.")

    elif opcion == "6":
            
        productos.clear()
        precios.clear()
        cantidades.clear()
        print("Lista de la compra vaciada.")

    elif opcion == "7":
        criterio = input("Ordenar por precio (p) o por cantidad (c): ").lower()
        if criterio == "p":
            datos = sorted(zip(precios, productos, cantidades))
            precios[:], productos[:], cantidades[:] = zip(*datos)
            print("Lista ordenada correctamente.")
        elif criterio == "c":
            datos = sorted(zip(cantidades, productos, precios))
            cantidades[:],  productos[:], precios[:] = zip(*datos)
            print("Lista ordenada correctamente.")
        else:
            print("Opción no válida.")
    
       

    elif opcion == 10: #alternativa ordenar
        
        criterio = input("Ordenar por precio (p) o por cantidad (c): ").lower()

        # Ordenamos las listas manteniendo la relación entre ellas
        if criterio == "p":
            indices_ordenados = sorted(range(len(precios)), key=lambda i: precios[i])
        elif criterio == "c":
            indices_ordenados = sorted(range(len(cantidades)), key=lambda i: cantidades[i])
        else:
            print("Opción no válida.")
            exit()

        # Reordenamos las listas según los índices ordenados
        precios = [precios[i] for i in indices_ordenados]
        productos = [productos[i] for i in indices_ordenados]
        cantidades = [cantidades[i] for i in indices_ordenados]

        # Mostramos el resultado
        print("Lista ordenada correctamente.")
        print("Productos:", productos)
        print("Precios:", precios)
        print("Cantidades:", cantidades)

    elif opcion == "8":
        
        total=0
        for precio, cantidad in zip(precios, cantidades):
            total+=precio*cantidad

        print(f"Importe total de la compra: {total:.2f} €")

    elif opcion == "9":
        if not productos:
            print("La lista de la compra está vacía.")
        else:

            print("\nLista de la compra:")
            for i in range(len(productos)):
                print(f"{productos[i]} - {cantidades[i]} ud - {precios[i]:.2f} €")

    elif opcion == "0":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida, intenta de nuevo.")
