# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En estos ejercicios conviene mirar el recorrido, el uso de range() y los acumuladores o contadores que se actualizan en cada vuelta.

### Ejercicio 1 - for

Idea clave: range(2, num+1) calcula factorial; *= acumula producto iterativamente.

??? example "Ver solución"
    ```python
    #factorial
    res = 1
    
    num = int(input("Dime un número: "))
    
    for contador in range(2, num + 1):
        res *= contador
    
    print(f"El resultado es {res}")
    ```

### Ejercicio 2 - for

Idea clave: range(1000) con break controla entrada; cnt acumula números válidos.

??? example "Ver solución"
    ```python
    # Pedir números hasta que se introduzca un 0 y sumarlos y hacer media
    suma = 0
    cont = 0
    
    for _ in range(1000):
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

### Ejercicio 3 - for

Idea clave: Tres contadores distintos clasifican números en positivo, negativo, cero.

??? example "Ver solución"
    ```python
    # Pedir un número determinado de números y calcular cuantos son positivos y ceros
    cont_negativos = 0
    cont_positivos = 0
    cont_ceros = 0
    
    cantidad_num = int(input("¿Cuántos números vas a introducir?: "))
    
    for i in range(1, cantidad_num + 1):
        num = int(input(f"Número {i}: "))
        if num > 0:
            cont_positivos += 1
        elif num < 0:
            cont_negativos += 1
        else:
            cont_ceros += 1
    
    print(f"Números positivos: {cont_positivos}")
    print(f"Números negativos: {cont_negativos}")
    print(f"Números igual a 0: {cont_ceros}")
    ```

### Ejercicio 4 - for

Idea clave: Validación con continue; len() != 1 filtra entrada carácter a carácter.

??? example "Ver solución"
    ```python
    # Pedir caracteres y decir si es vocal o no (terminar con espacio)
    
    for _ in range(1000):
        car = input("Introduce un carácter: ")
        
        # Asegurarse de que el carácter es solo uno
        if len(car) != 1:
            print("Por favor, introduce solo un carácter.")
            continue
        # Otra forma de asegurarse que el carácter es solo uno
        # while True:
        #     car = input("Introduce un carácter: ")
        #     if len(car) == 1:
        #         break
        #     print("Por favor, introduce solo un carácter.")
    
        if car == " ":
            break
        
        if car.lower() in 'aeiou':
            print("VOCAL")
        else:
            print("NO VOCAL")
    ```

### Ejercicio 5 - for

Idea clave: range(num1, num2+1, 2) con step; suma 1 si inicio es impar.

??? example "Ver solución"
    ```python
    # Programa que imprime todos los números pares entre dos números dados por el usuario.
    
    # Leer los números
    num1 = int(input("Introduce el número 1: "))
    num2 = int(input("Introduce el número 2: "))
    
    if num1 % 2 == 1:
        num1 += 1
    
    for num in range(num1, num2 + 1, 2):
        print(f"{num}")
    ```

### Ejercicio 6 - for

Idea clave: range(1, 11) tabla simple; formateo f-string con operación inline.

??? example "Ver solución"
    ```python
    # Programa para mostrar la tabla de multiplicar de un número ingresado por el usuario
    
    num_tabla = int(input("¿De qué número quieres mostrar la tabla de multiplicar?: "))
    
    for num in range(1, 11):
        print(f"{num} * {num_tabla} = {num * num_tabla}")
    ```

### Ejercicio 7 - for

Idea clave: range(1000) con validación; exponente >= 0 asegura entrada válida.

??? example "Ver solución"
    ```python
    # Programa para calcular la potencia de un número sin usar el operador de potencia.
    
    base = float(input("Dame la base de la potencia: "))
    
    for _ in range(1000):
        exponente = int(input("Dame el exponente de la potencia: "))
        if exponente >= 0:
            break
        print("ERROR: El exponente debe ser positivo")
    
    potencia = 1.0
    
    for i in range(1, exponente + 1):
        potencia *= base
    
    print("Potencia:", potencia)
    ```

### Ejercicio 8 - for

Idea clave: Dos posiciones convergen; km1 avanza y km2 retrocede hasta encontrarse.

??? example "Ver solución"
    ```python
    # Calcular el km en el que se encuentran 2 coches
    km1 = 70
    km2 = 150
    
    for km in range(1000):
        pos1= km1 + km
        pos2= km2 - km
    
        if pos1 >= pos2:
            print("Se encuentran en el km:", pos1)
            break
    ```

### Ejercicio 9 - for

Idea clave: range(1000) con doble break; suma dentro, cuenta fuera intervalo.

??? example "Ver solución"
    ```python
    # Programa que pide un intervalo y analiza los números introducidos por el usuario.
    
    suma_dentro_intervalo = 0
    cont_fuera_intervalo = 0
    igual_limites = False
    
    for _ in range(1000):
        lim_inf = int(input("Introduce el límite inferior del intervalo: "))
        lim_sup = int(input("Introduce el límite superior del intervalo: "))
        if lim_inf <= lim_sup:
            break
        else:
            print("ERROR: El límite inferior debe ser menor que el superior.")
    
    
    for _ in range(1000):
        num = int(input("Introduce un número (0 para salir): "))
        if num == 0:
            break
        if num == lim_inf or num == lim_sup: # Número igual a alguno de los límites
            igual_limites = True
    
        if lim_inf < num < lim_sup: # Pertenece al intervalo
            suma_dentro_intervalo += num
        else:
            cont_fuera_intervalo += 1 # No pertenece al intervalo
    
    
    print("La suma de los números dentro del intervalo es:", suma_dentro_intervalo)
    print("La cantidad de números fuera del intervalo es:", cont_fuera_intervalo)
    if igual_limites:
        print("Se ha introducido algún número igual a los límites del intervalo.")
    else:
        print("No se ha introducido ningún número igual a los límites del intervalo.")
    ```

### Ejercicio 10 - for

Idea clave: random.randint genera número secreto; for/else ejecuta si no break.

??? example "Ver solución"
    ```python
    import random
    
    # Adivina un número en 10 intentos
    num_secreto = random.randint(1, 100)
    
    print("Adivina el número (de 1 a 100):")
    
    for intento in range(1,11):
        num = int(input("Introduce un número: "))
    
        if num_secreto == num:
            print(f"CORRECTO: era el {num_secreto} y lo has adivinado en {intento} intentos.")
            break
        elif num < num_secreto:
            print("Muy bajo")
        else:
             print("Muy alto")
    
        print(f"Te quedan {10-intento} intentos.")
        
       
    else:
        print(f"¡Has perdido! El número era: {num_secreto}")
    ```

### Ejercicio 11

Idea clave: math.sqrt limita búsqueda divisores; rango hasta raíz cuadrada.

??? example "Ver solución"
    ```python
    import math
    
    es_primo = True
    
    num = int(input("Introduce un número para comprobar si es primo: "))
    
    if num <= 1:
        es_primo = False
    else:
        # Comprobación de divisibilidad desde 2 hasta la raíz cuadrada del número
        for div in range(2, int(math.sqrt(num)) + 1):
            if num % div == 0:
                es_primo = False
                print("No es primo")
                break 
            
        else: #solo se ejecuta si no se ejecuta el break
            print("Es primo")
    ```

### Ejercicio 12

Idea clave: for range(1,13) acumula mes a mes; += suma ahorro anterior.

??? example "Ver solución"
    ```python
    # Calcular ahorro en un año
    ahorro_acum = 0.0
    
    # Bucle para calcular el ahorro de cada mes
    for mes in range(1, 13):
        ahorro_mes = float(input(f"¿Cuánto has ahorrado en el mes {mes}?: "))
        ahorro_acum += ahorro_mes
        print(f"En el mes {mes} llevas ahorrado {ahorro_acum:.2f} euros.")
    ```

### Ejercicio 13

Idea clave: for range(1,7) suma horas diarias; multiplicar por tarifa semanal.

??? example "Ver solución"
    ```python
    # Calcular sueldo semanal preguntando las horas de cada día
    horas_sem = 0
    
    sueldo_hora = float(input("Introduce el sueldo por hora: "))
    
    for dia in range(1, 7):
        horas = int(input(f"¿Cuántas horas has trabajado el día {dia}?: "))
        horas_sem += horas
    
    sueldo_sem = sueldo_hora * horas_sem
    
    print(f"Horas acumuladas en la semana: {horas_sem}")
    print(f"Sueldo semanal: {sueldo_sem:.2f} euros")
    ```

### Ejercicio 14

Idea clave: Valor se duplica; *= 2 cada iteración exponencial.

??? example "Ver solución"
    ```python
    
    #Calcular lo que se ha pagado durante 10 meses, si comienzas de 10€ y si cada mes se dobla la cantidad a pagar
    pago_acum = 0  
    pago = 10      
    
    for mes in range(1, 11):  
        pago_acum += pago    
        print(f'En el mes {mes} pagó {pago} €')
        pago *= 2       
    
    print("Al final de los 20 meses tuvo que pagar:", pago_acum)
    ```

### Ejercicio 15

Idea clave: for anidado: trabajador y horas; suma total de todos.

??? example "Ver solución"
    ```python
    # Calcular sueldo semanal de cada trabajador y el total que paga la empresa
    horas_total = 0  
    num_trab = int(input("¿Cuántos trabajadores tiene la empresa?: "))
    sueldo_hora = float(input("Sueldo por hora: "))
    
    
    for trabajador in range(1, num_trab + 1):
        horas_sem = int(input(f"¿Cuántas horas ha trabajado el trabajador {trabajador}?: "))
        sueldo_semanal = horas_sem * sueldo_hora
        horas_total += horas_sem  
        print(f"El trabajador {trabajador} tiene de sueldo {sueldo_semanal:.2f}")
    
    total_pago = horas_total * sueldo_hora
    print(f"El pago a los {num_trab} trabajadores es: {total_pago:.2f}")
    ```

### Ejercicio 16

Idea clave: for anidado: tabla y número; input() espera entre grupos.

??? example "Ver solución"
    ```python
    # Programa para mostrar las tablas de multiplicar de los números 1, 2, 3, 4 y 5.
    
    for tabla in range(1, 6): 
        print(f"Tabla del {tabla}:")
        
        for num in range(1, 11):
            print(f"{tabla} * {num} = {tabla * num}")
        
        input("Presiona Enter para continuar...\n")
    ```

### Ejercicio 17

Idea clave: Triple for anidado: trabajador, días, horas; acumula total empresa.

??? example "Ver solución"
    ```python
    
    horas_acum = 0  
    
    num_trab = int(input("¿Cuántos trabajadores tiene la empresa?: "))
    sueldo_hora = float(input("Sueldo por hora: "))
    
    # Para cada trabajador
    for trabajador in range(1, num_trab + 1):
        horas_trab = 0  
        dias = int(input(f"¿Cuántos días ha trabajado el trabajador {trabajador}?: "))
    
        # Para cada día
        for dia in range(1, dias + 1):
            horas = int(input(f"¿Cuántas horas ha trabajado el trabajador {trabajador} el día {dia}?: "))
            horas_trab += horas 
       
        sueldo_semanal = horas_trab * sueldo_hora
        print(f"El trabajador {trabajador} tiene de sueldo {sueldo_semanal:.2f}")
    
        horas_acum += horas_trab
    
    total_pago = horas_acum * sueldo_hora
    print(f"El pago a los {num_trab} trabajadores es: {total_pago}")
    ```

### Ejercicio 18

Idea clave: for anidado hora:minuto:segundo con time.sleep(1) simula reloj.

??? example "Ver solución"
    ```python
    import time
    
    for hora in range(24):  
        for minuto in range(60): 
            for segundo in range(60):  
                print(f"{hora:02}:{minuto:02}:{segundo:02}")  # Muestra la hora en formato HH:MM:SS
                time.sleep(1) 
    ```

### Ejercicio 19

Idea clave: continue salta múltiplos de 3; % 3 == 0 identifica.

??? example "Ver solución"
    ```python
    # Programa para mostrar las tablas de multiplicar de los números 1, 2, 3, 4 y 5 sin los múltiplos de 3.
    
    for tabla in range(1, 6): 
        print(f"Tabla del {tabla}:")
        
        for num in range(1, 11):
            res = tabla * num
            if res % 3 == 0:
                continue
            print(f"{tabla} * {num} = {res}")
        
        input("Presiona Enter para continuar...\n")
    ```

### Ejercicio 20

Idea clave: while dentro for: encuentra N primos; rango divisores eficiente.

??? example "Ver solución"
    ```python
    # Mostrar los N primeros primos
    N = int(input("Ingresa la cantidad de números primos que quieres mostrar: "))
    
    contador_primos = 0  
    numero = 2          
    
    while contador_primos < N:
        es_primo = True
    
        for divisor in range(2, int(numero ** 0.5) + 1):
            if numero % divisor == 0:
                es_primo = False
                break
    
        if es_primo:
            print(numero)
            contador_primos += 1
    
        numero += 1
    ```
