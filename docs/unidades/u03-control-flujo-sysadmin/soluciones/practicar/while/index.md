# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En estos ejercicios la clave está en la condición de parada y en la variable que cambia dentro del bucle.

### Ejercicio 1 - while

Idea clave: while contador <= num multiplica; contador += 1 incrementa cada vuelta.

??? example "Ver solución"
    ```python
    # Calcular el factorial
    resultado = 1
    contador = 2
    
    num = int(input("Dime un número: "))
    
    while contador <= num:
        resultado *= contador
        contador += 1
    
    print(f"El resultado es {resultado}")
    ```

### Ejercicio 2 - while

Idea clave: while num != 0 continúa; lee número antes y dentro del bucle.

??? example "Ver solución"
    ```python
    # Pedir números hasta que se introduzca un 0 y sumarlos y hacer media
    suma = 0
    cont = 0
    
    num = int(input("Número (0 para salir): "))
    
    while num != 0:
        suma += num  
        cont += 1 
        num = int(input("Número (0 para salir): "))
    
    if cont > 0:
        media = suma / cont
    else:
        media = 0
    
    # Mostrar resultados
    print(f"Suma: {suma}")
    print(f"Media: {media}")
    ```

### Ejercicio 2 - while true

Idea clave: while True con if num == 0 break; entrada única dentro.

??? example "Ver solución"
    ```python
    # Pedir números hasta que se introduzca un 0 y sumarlos y hacer media
    suma = 0
    cont = 0
    
    while True:
        num = int(input("Número (0 para salir): "))
        if num == 0:
            break
        suma += num
        cont += 1
    
    if cont != 0:
        media = suma / cont
    else:
        media = 0
    
    print(f"Suma: {suma}")
    print(f"Media: {media}")
    ```

### Ejercicio 3 - while

Idea clave: Contador i incremental; while i < cantidad estructura clara.

??? example "Ver solución"
    ```python
    # Pedir un número determinado de números y calcular cuantos son positivos y ceros
    cont_negativos = 0
    cont_positivos = 0
    cont_ceros = 0
    
    i = 0
    
    cantidad_num = int(input("¿Cuántos números vas a introducir?: "))
    
    while i < cantidad_num:
        num = int(input(f"Número {i}: "))
        if num > 0:
            cont_positivos += 1
        elif num < 0:
            cont_negativos += 1
        else:
            cont_ceros += 1
        i+=1
    
    print(f"Números positivos: {cont_positivos}")
    print(f"Números negativos: {cont_negativos}")
    print(f"Números igual a 0: {cont_ceros}")
    ```

### Ejercicio 4 - while

Idea clave: Doble while: primero valida carácter, segundo procesa entrada.

??? example "Ver solución"
    ```python
    
    # Pedir caracteres y decir si es vocal o no (terminar con espacio)
    car = ""
    
    while len(car) != 1: # Asegurarse de que el carácter es solo uno
        car = input("Introduce un carácter: ")
    
    while car != " ":
        if car.lower() in 'aeiou':
            print("VOCAL")
        else:
            print("NO VOCAL")
        
        car = ""
        while len(car) != 1:
            car = input("Introduce un carácter: ")
    ```

### Ejercicio 4 - while true

Idea clave: while True con continue rechaza; len() != 1 realimenta.

??? example "Ver solución"
    ```python
    # Pedir caracteres y decir si es vocal o no (terminar con espacio)
    
    while True:
        car = input("Introduce un carácter: ")
        
        # Asegurarse de que el carácter es solo uno
        if len(car) != 1:
            print("Por favor, introduce solo un carácter.")
            continue
        
        if car == " ":
            break
        
        if car.lower() in 'aeiou':
            print("VOCAL")
        else:
            print("NO VOCAL")
    ```

### Ejercicio 5 - while

Idea clave: Números pares: verifica paridad inicio, num1 += 2 incrementa.

??? example "Ver solución"
    ```python
    # Programa que imprime todos los números pares entre dos números dados por el usuario.
    
    # Leer los números
    num1 = int(input("Introduce el número 1: "))
    num2 = int(input("Introduce el número 2: "))
    
    if num1 % 2 == 1:
        num1 += 1
    
    while num1 <= num2:
        print(f"{num1}")
        num1+=2
    ```

### Ejercicio 6 - while

Idea clave: num <= 10 con num += 1; while reemplaza for rango.

??? example "Ver solución"
    ```python
    # Programa para mostrar la tabla de multiplicar de un número ingresado por el usuario
    
    num_tabla = int(input("¿De qué número quieres mostrar la tabla de multiplicar?: "))
    
    num=1
    while num<=10:
        print(f" {num_tabla} * {num} = {num * num_tabla}")
        num+=1
    ```

### Ejercicio 7 - while true while

Idea clave: Anidación: while True valida, inner while repite bucle.

??? example "Ver solución"
    ```python
    # Programa para calcular la potencia de un número sin usar el operador de potencia.
    
    base = float(input("Dame la base de la potencia: "))
    
    while True:
        exponente = int(input("Dame el exponente de la potencia: "))
        if exponente >= 0:
            break
        
        print("ERROR: El exponente debe ser positivo")
    
    potencia = 1.0
    
    i = 1
    while i <= exponente:
        potencia *= base
        i+=1
    
    print("Potencia:", potencia)
    ```

### Ejercicio 8 - while

Idea clave: Dos posiciones avanzan hacia centro; mientras km1 != km2.

??? example "Ver solución"
    ```python
    # Calcular el km en el que se encuentran 2 coches
    km1 = 70
    km2 = 150
    
    while km1 != km2:
        km1 += 1  
        km2 -= 1  
    
    print("Se encuentran en el km:", km1)
    ```

### Ejercicio 9 - while

Idea clave: Intervalo validado; lee número antes y dentro bucle.

??? example "Ver solución"
    ```python
    # Programa que pide un intervalo y analiza los números introducidos por el usuario.
    
    suma_dentro_intervalo = 0
    cont_fuera_intervalo = 0
    igual_limites = False
    
    while True:
        lim_inf = int(input("Introduce el límite inferior del intervalo: "))
        lim_sup = int(input("Introduce el límite superior del intervalo: "))
        if lim_inf <= lim_sup:
            break
        else:
            print("ERROR: El límite inferior debe ser menor que el superior.")
    
    
    num = int(input("Introduce un número (0 para salir): "))
    while num != 0:
        if lim_inf < num < lim_sup: # Pertenece al intervalo
            suma_dentro_intervalo += num
        else:
            cont_fuera_intervalo += 1 # No pertenece al intervalo
    
        if num == lim_inf or num == lim_sup: # Número igual a alguno de los límites
            igual_limites = True
    
    
        num = int(input("Introduce un número (0 para salir): "))
    
    
    print("La suma de los números dentro del intervalo es:", suma_dentro_intervalo)
    print("La cantidad de números fuera del intervalo es:", cont_fuera_intervalo)
    if igual_limites:
        print("Se ha introducido algún número igual a los límites del intervalo.")
    else:
        print("No se ha introducido ningún número igual a los límites del intervalo.")
    ```

### Ejercicio 10 - while

Idea clave: Intentos limitados con contador; while num != num_secreto.

??? example "Ver solución"
    ```python
    import random
    
    # Adivina un número en 10 intentos
    intentos = 10
    num_secreto = random.randint(1, 100)
    
    print("Adivina el número (de 1 a 100):")
    
    num = int(input("Introduce un número: "))
    
    while num_secreto != num and intentos > 1:
        if num_secreto > num:
            print("Muy bajo")
        else:
            print("Muy alto")
        
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
        
        num = int(input("Introduce otro número: "))
    
    if num_secreto == num:
        print(f"CORRECTO: era el {num_secreto} y lo has adivinado en {11 - intentos} intentos.")
    else:
        print(f"¡Has perdido! El número era: {num_secreto}")
    ```

### Extra

Idea clave: Menú while; isdigit() valida opción, opcion != 5 continúa.

??? example "Ver solución"
    ```python
    
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
    ```
