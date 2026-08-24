#Es el 10 convertido a funciones

lista=[]

def mostrar_menu():
    print("\nGestión de Lista de la Compra")
    print("1. Mostrar la lista")
    print("2. Añadir elementos a la lista")
    print("3. Borrar elementos de la lista")
    print("4. Contar elementos de la lista")
    print("5. Añadir una lista de elementos a la ya existente")
    print("6. Borrar toda la lista")
    print("7. Salir")

def mostrar_lista():
    if lista:
        print("Elementos de la lista:" + ', '.join(lista))
    else:
        print("La lista está vacía")

def agregar_producto():
    elemento = input("Introduce el elemento a añadir: ")
    lista.append(elemento)
    print(f"'{elemento}' ha sido añadido a la lista.")

def eliminar_producto():
    elemento = input("Introduce el elemento a borrar: ")
    if elemento in lista:
        lista.remove(elemento)
        print(f"'{elemento}' ha sido eliminado de la lista.")
    else:
        print(f"'{elemento}' no está en la lista.")

def contar_productos():
    print(f"La lista tiene {len(lista)} elementos.")

def agregar_varios_productos():
    elementos = input("Introduce los elementos separados por comas: ").split(',')
    elementos = [e.strip() for e in elementos]
    lista.extend(elementos)
    print("Los elementos han sido añadidos a la lista.")

def borrar_lista():
    lista.clear()
    print("La lista ha sido vaciada.")

 
while True:
    
    #Mostrar menu
    mostrar_menu()
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_lista()

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
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")