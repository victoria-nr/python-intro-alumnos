
lista=[]

while True:
    
    #Mostrar menu
    print("\nGestión de Lista de la Compra")
    print("1. Mostrar la lista")
    print("2. Añadir elementos a la lista")
    print("3. Borrar elementos de la lista")
    print("4. Contar elementos de la lista")
    print("5. Añadir una lista de elementos a la ya existente")
    print("6. Borrar toda la lista")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        if lista:
            print("Elementos de la lista:" + ', '.join(lista))
        else:
            print("La lista está vacía")
    elif opcion == "2":
        elemento = input("Introduce el elemento a añadir: ")
        if elemento not in lista:
            lista.append(elemento)
        print(f"'{elemento}' ha sido añadido a la lista.")
    elif opcion == "3":
        elemento = input("Introduce el elemento a borrar: ")
        if elemento in lista:
            lista.remove(elemento)
            print(f"'{elemento}' ha sido eliminado de la lista.")
        else:
            print(f"'{elemento}' no está en la lista.")
    elif opcion == "4":
        print(f"La lista tiene {len(lista)} elementos.")
    elif opcion == "5":
        elementos = input("Introduce los elementos separados por comas: ").split(',')
        elementos = [e.strip() for e in elementos]
        lista.extend(elementos)
        print("Los elementos han sido añadidos a la lista.")
    elif opcion == "6":
        lista.clear()
        print("La lista ha sido vaciada.")
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")


