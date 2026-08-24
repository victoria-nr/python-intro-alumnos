
opcion = 0
while opcion != 5:

    print("\nMenú de recomendaciones")
    print("   1. Literatura")
    print("   2. Cine")
    print("   3. Música")
    print("   4. Videojuegos")
    print("   5. Salir")

    opcion = input("Elija una opción (1-5): ")

    if opcion.isdigit():  
        opcion = int(opcion)
    else:
        print("Opción no válida. Ingrese un número entre 1 y 5.")
        continue

    if opcion == 1:
        print("\nHas escogido literatura")
       
    elif opcion == 2:
        print("\nHas escogido cine:")
        
    elif opcion == 3:
        print("\nHas escogido música")
        
    elif opcion == 4:
        print("\nHas escogido videojuegos")
       
    elif opcion == 5:
        print("Gracias, vuelva pronto.")
    else:
        print("Opción no válida. Ingrese un número entre 1 y 5.")

    if opcion != 5:
        input("\nPresione Enter para continuar...")

