# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

La clave aquí es elegir bien cuándo recorrer, buscar, acumular o transformar elementos de una lista.

### Ejercicio 1

Idea clave: Recorre lista sin índices; calcula transformaciones elemento a elemento.

??? example "Ver solución"
    ```python
    import random
    
    lista_numeros = [0]*10
    
    for i in range(10):
        lista_numeros[i]=random.randint(1, 10)
    
    for numero in lista_numeros:
        cuadrado = numero ** 2
        cubo = numero ** 3
        print(f"Número: {numero}, Cuadrado: {cuadrado}, Cubo: {cubo}")
    ```

### Ejercicio 2

Idea clave: El slicing [::-1] invierte lista; recorre resultado sin modificar original.

??? example "Ver solución"
    ```python
    
    lista_original = []
    
    for i in range(5):
        cadena = input(f"Introduce la cadena {i + 1}: ")
        lista_original.append(cadena)
    
    lista_invertida = lista_original[::-1]
    
    print("\nLista invertida:")
    for cadena in lista_invertida:
        print(cadena)
    ```

### Ejercicio 3

Idea clave: sum()/len() media; max()/min() extremos; enumerate() etiqueta posiciones.

??? example "Ver solución"
    ```python
    
    notas = []
    
    for i in range(5):
        nota=-1.0
        while nota < 0 or nota > 10:
            nota = float(input(f"Introduce la nota {i + 1} (entre 0 y 10): "))
          
        notas.append(nota)
    
    
    print("\nLas notas ingresadas son:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
    
    
    nota_media = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    print(f"\nNota media: {nota_media:.2f}")
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")
    ```

### Ejercicio 4

Idea clave: while len(lista) < 10 con break permite salida flexible.

??? example "Ver solución"
    ```python
    
    lista=[]
    
    while len(lista) < 10:
        num = int(input("Introduce un número (negativo para terminar): "))
        if num < 0:
            break
        lista.append(num)
    
    print("Lista final:", lista)
    ```

### Ejercicio 5

Idea clave: .sort() modifica in-place; no reasignes como lista = sorted().

??? example "Ver solución"
    ```python
    import random
    lista=[]
    for _ in range(10):
        numero =random.randint(1, 100)
        lista.append(numero)
    
    print("Lista original:", lista)
    
    lista.sort()
    
    print("Lista ordenada:", lista)
    ```

### Ejercicio 6

Idea clave: Acceso índice num-1; valida entrada antes de usar.

??? example "Ver solución"
    ```python
    
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    
    
    num_mes = int(input("Introduce un número de mes (1-12): "))
    while num_mes < 1 or num_mes > 12:
        print("Número de mes no válido. Debe estar entre 1 y 12.")
        num_mes = int(input("Introduce un número de mes (1-12): "))
    
    
    nombre_mes = meses[num_mes - 1]
    dias = dias_mes[num_mes - 1]
    print(f"El mes {nombre_mes} tiene {dias} días.")
    ```

### Ejercicio 7

Idea clave: lista1 + lista2 crea nueva lista; más legible que .extend().

??? example "Ver solución"
    ```python
    
    lista1 = []
    lista2 = []
       
    print("Elementos para la lista 1")
    for i in range(5):
        num = int(input(f"Número {i + 1}: "))
        lista1.append(num)
    
    print("Elementos para la lista 2")
    for i in range(5):
        num = int(input(f"Número {i + 1}: "))
        lista2.append(num)
    
    # Unir las listas en una sola
    resultado = lista1 + lista2 
    
    print("\nLista resultado:", resultado)
    ```

### Ejercicio 8

Idea clave: Índices vinculan datos de dos listas; range(len()) acceso simultáneo.

??? example "Ver solución"
    ```python
    
    nombres = []
    edades = []
    
    while True:
        nombre = input("Introduce el nombre del alumno (o '*' para terminar): ")
        if nombre == "*":
            break
        edad = int(input("Introduce la edad del alumno: "))
        
        nombres.append(nombre)
        edades.append(edad)
    
    print("\nAlumnos mayores de edad:")
    for i in range(len(edades)):
        if edades[i] >= 18:
            print(f"{nombres[i]} ({edades[i]} años)")
    
    # Encontrar la edad máxima
    edad_maxima = max(edades)
    print("\nAlumnos más mayores:")
    for i in range(len(edades)):
        if edades[i] == edad_maxima:
            print(f"{nombres[i]} ({edades[i]} años)")
    ```

### Ejercicio 9

Idea clave: Tres listas paralelas gestionan datos relacionados con acceso simultáneo.

??? example "Ver solución"
    ```python
    
    temp_min = []
    temp_max = []
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    
    for i in range(7):
        print(f"\nDía {dias[i]}:")
        mint = float(input("Introduce la temperatura mínima: "))
        maxt = float(input("Introduce la temperatura máxima: "))
    
        temp_min.append(mint)
        temp_max.append(maxt)
    
    print("\nTemperatura media de cada día:")
    for i in range(7):
        media = (temp_min[i] + temp_max[i]) / 2
        print(f"Día {dias[i]}: {media:.2f}°C")
    
    
    min_t = min(temp_min)
    print("\nDías con menor temperatura mínima:")
    for i in range(7):
        if temp_min[i] == min_t:
            print(f"Día {dias[i]}: {temp_min[i]}°C")
    
    
    temp = float(input("\nIntroduce una temperatura máxima para buscar: "))
    existe = False
    for i in range(7):
        if temp_max[i] == temp:
            print(dias[i])
            existe=True
    if not existe:
        print("No hay días con esa temperatura máxima.")
    ```

### Ejercicio 10

Idea clave: .append(), .extend(), .remove(), .clear() modifican; .join() serializa.

??? example "Ver solución"
    ```python
    
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
    ```

### Ejercicio 11

Idea clave: zip() vincula; sorted(zip()) ordena; zip(*) desempaqueta resultado.

??? example "Ver solución"
    ```python
    
        
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
    ```

### Ejercicio 12

Idea clave: Refactorizar menú en funciones mejora legibilidad; global accede variables.

??? example "Ver solución"
    ```python
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
    ```

### Ejercicio 13

Idea clave: Dividir lógica en funciones reutilizables simplifica menú con operaciones.

??? example "Ver solución"
    ```python
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
    ```
