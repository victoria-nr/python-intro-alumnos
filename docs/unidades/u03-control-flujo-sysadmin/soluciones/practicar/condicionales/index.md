# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En este bloque conviene fijarse en cómo se expresan las condiciones y en cómo se separan los distintos casos posibles.

### Ejercicio 1

Idea clave: Comparación simple de dos números; if/else sin complejidad adicional.

??? example "Ver solución"
    ```python
    # Algoritmo para determinar si un número es mayor que otro
    
    
    num1 = int(input("Dime el número 1: "))
    num2 = int(input("Dime el número 2: "))
    
    
    if num1 > num2:
        print("Número 1 es mayor que número 2")
    else:
        print("Número 1 NO es mayor que número 2")
    ```

### Ejercicio 2

Idea clave: Tres casos mutuamente excluyentes; if/elif/else orden importa.

??? example "Ver solución"
    ```python
    # Algoritmo para determinar si un número es positivo, negativo o cero
    
    
    num = int(input("Dime el número: "))
    
    if num == 0:
        print("Es igual a 0")
    elif num > 0:
        print("Es positivo")
    else:
        print("Es negativo")
    ```

### Ejercicio 3

Idea clave: Módulo 2 determina paridad; % == 0 identifica números pares.

??? example "Ver solución"
    ```python
    # Algoritmo para determinar si un número es par o impar
    
    num = int(input("Dime el número: "))
    
    if num % 2 == 0:
        print("Es Par")
    else:
        print("Es Impar")
    ```

### Ejercicio 4

Idea clave: Valida divisor antes de dividir; if divisor == 0 evita excepción.

??? example "Ver solución"
    ```python
    # Algoritmo para realizar una división y manejar el caso de divisor igual a 0
    
    dividendo = int(input("Dime el número 1: "))
    divisor = int(input("Dime el número 2: "))
    
    if divisor == 0:
        print("No puedes dividir por 0")
    else:
        print("La división es", dividendo / divisor)
    ```

### Ejercicio 5

Idea clave: Autenticación con and; ambas condiciones deben cumplirse.

??? example "Ver solución"
    ```python
    # Algoritmo para autenticar a un usuario mediante un nombre y una contraseña
    
    usuario = input("Introduce el usuario: ")
    
    password = input("Introduce el password: ")
    
    if usuario == "pepe" and password == "asdasd":
        print("Has entrado al sistema")
    else:
        print("Usuario/password incorrecto")
    ```

### Ejercicio 6

Idea clave: cadena.upper() compara normalizada; igualdad verifica mayúsculas.

??? example "Ver solución"
    ```python
    # Algoritmo para comprobar si una cadena es completamente en mayúsculas
    
    cadena = input("Introduce una cadena: ")
    
    if cadena == cadena.upper():
        print("La cadena es mayúsculas")
    else:
        print("La cadena no es mayúsculas")
    ```

### Ejercicio 7

Idea clave: Tres casos: positivo, cero, negativo; exponente negativo invierte potencia.

??? example "Ver solución"
    ```python
    # Algoritmo para calcular la potencia de un número considerando casos especiales
    
    base = float(input("Dime la base: "))
    exponente = int(input("Dime el exponente: "))
    
    if exponente > 0:
        print("La potencia es", base ** exponente)
    elif exponente == 0:
        print("La potencia es 1")
    else:
        print("La potencia es", 1 / (base ** abs(exponente)))
    ```

### Ejercicio 8

Idea clave: Condiciones anidadas; nota >= 5 AND edad >= 18 primer nivel.

??? example "Ver solución"
    ```python
    # Algoritmo para determinar la aceptación según nota, edad y sexo
    
    nota = int(input("Introduce la nota: "))
    edad = int(input("Introduce la edad: "))
    sexo = input("Introduce el sexo (F/M): ").upper()
    
    if nota >= 5 and edad >= 18:
        if sexo == "F":
            print("Aceptada")
        elif sexo == "M":
            print("Posible")
        else:
            print("No Aceptada")
    else:
        print("No Aceptada")
    ```

### Ejercicio 9

Idea clave: Ordenar tres números requiere lógica exhaustiva; if/elif/else profundo.

??? example "Ver solución"
    ```python
    # Algoritmo para ordenar tres números de mayor a menor
    
    num1 = int(input("Dime el número 1: "))
    num2 = int(input("Dime el número 2: "))
    num3 = int(input("Dime el número 3: "))
    
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            print(num2, num1, num3)
        else:
            print(num2, num3, num1)
    else:
        if num1 >= num2:
            print(num3, num1, num2)
        else:
            print(num3, num2, num1)
    ```

### Ejercicio 10

Idea clave: math.sqrt calcula distancia entre centros; seis casos de posiciones.

??? example "Ver solución"
    ```python
    import math
    
    # Algoritmo para clasificar la relación entre dos circunferencias
    
    x1 = float(input("Dime coordenada x de la primera circunferencia: "))
    y1 = float(input("Dime coordenada y de la primera circunferencia: "))
    r1 = float(input("Dime el radio de la primera circunferencia: "))
    
    x2 = float(input("Dime coordenada x de la segunda circunferencia: "))
    y2 = float(input("Dime coordenada y de la segunda circunferencia: "))
    r2 = float(input("Dime el radio de la segunda circunferencia: "))
    
    # Calcular la distancia entre los centros
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distancia > (r1 + r2):
        print("Circunferencias exteriores")
    elif distancia == (r1 + r2):
        print("Circunferencias tangentes exteriores")
    elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
        print("Circunferencias secantes")
    elif distancia == abs(r1 - r2):
        print("Circunferencias tangentes interiores")
    elif distancia > 0 and distancia < abs(r1 - r2):
        print("Circunferencias interiores")
    elif distancia == 0:
        print("Circunferencias concéntricas")
    ```

### Ejercicio 11

Idea clave: Teorema Pitágoras en condición; comprueba si sum potencias igual.

??? example "Ver solución"
    ```python
    # Programa para determinar el tipo de triángulo según sus lados
    
    ladoA = float(input("Introduce la longitud del lado A: "))
    ladoB = float(input("Introduce la longitud del lado B: "))
    ladoC = float(input("Introduce la longitud del lado C: "))
    
    #triángulo rectángulo (Pitágoras)
    if (ladoA**2 + ladoB**2 == ladoC**2) or (ladoB**2 + ladoC**2 == ladoA**2) or (ladoC**2 + ladoA**2 == ladoB**2):
        print("Triángulo Rectángulo")
    
    
    if ladoA == ladoB == ladoC:
        print("Triángulo Equilátero")
    
    elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoC == ladoA):
        print("Triángulo Isósceles")
    
    else:
        print("Triángulo Escaleno")
    ```

### Ejercicio 12

Idea clave: Año bisiesto: divisible por 4 Y NO por 100 O por 400.

??? example "Ver solución"
    ```python
    # Programa para determinar si un año es bisiesto
    
    year = int(input("Introduce el año: "))
    
    if (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0):
        print("Año bisiesto.")
    else:
        print("Año no bisiesto.")
    ```

### Ejercicio 13

Idea clave: Días del mes varían; febrero es caso especial con bisiesto.

??? example "Ver solución"
    ```python
    # Programa para verificar si una fecha es correcta
    
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    year = int(input("Introduce el año: "))
    
    #if mes in [1, 3, 5, 7, 8, 10, 12]:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_del_mes = 31
    #elif mes in [4, 6, 9, 11]:
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_del_mes = 30
    elif mes == 2:
        #  bisiesto
        if (year % 4 == 0 and not (year % 100 == 0)) or (year % 400 == 0):
            dias_del_mes = 29
        else:
            dias_del_mes = 28
    else:
        print("Fecha incorrecta")
        exit()
    
    if dia < 1 or dia > dias_del_mes:
        print("Fecha incorrecta")
    else:
        print("Fecha correcta")
    ```

### Ejercicio 14

Idea clave: Cálculo escalonado; tipo y tamaño ajustan precio base.

??? example "Ver solución"
    ```python
    # Programa para calcular el precio final de venta de la uva
    
    precio_inicial = float(input("Introduce el precio inicial por kilo de la UVA (en céntimos): "))
    kilos = int(input("Introduce cuántos kilos has vendido: "))
    tipo = input("Introduce el tipo de la UVA (A/B): ").upper()
    
    #if tipo not in ["A", "B"]:
    if tipo != "A" and tipo != "B":
        print("Tipo incorrecto")
    else:
        tamano = input("Introduce el tamaño de la UVA (1/2): ")
    
        #if tamano not in ["1", "2"]:
        if tamano != "1" and tamano != "2":
            print("Tamaño incorrecto")
        else:
            if tipo == "A":
                if tamano == "1":
                    precio_inicial += 20
                else:  # Tamaño "2"
                    precio_inicial += 30
            elif tipo == "B":
                if tamano == "1":
                    precio_inicial -= 30
                else:  # Tamaño "2"
                    precio_inicial -= 50
    
            precio_final = precio_inicial * kilos
    
            print(f"La ganancia es {precio_final / 100:.2f} euros.")
    ```

### Ejercicio 15

Idea clave: Rangos de cantidad (100, 50, 30) tienen precios diferentes.

??? example "Ver solución"
    ```python
    # Programa para calcular el coste del autobús y el coste por alumno
    
    num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?: "))
    
    
    coste_por_alumno = 0.0
    coste_autobus = 0.0
    
    if num_alumnos >= 100:
        coste_por_alumno = 65
    elif num_alumnos >= 50:
        coste_por_alumno = 70
    elif num_alumnos >= 30:
        coste_por_alumno = 95
    elif num_alumnos > 0:  # Menos de 30 alumnos
        coste_por_alumno = 2850 / num_alumnos
    else:
        print("El número de alumnos debe ser un valor positivo.")
        exit()
    
    coste_autobus = num_alumnos * coste_por_alumno
    
    print(f"El coste por alumno es {coste_por_alumno:.2f} euros.")
    print(f"El coste del autobús es {coste_autobus:.2f} euros.")
    ```

### Ejercicio 16

Idea clave: Minutos por tramos con precios decrecientes; porcentaje extra según día.

??? example "Ver solución"
    ```python
    # Programa para calcular el coste de una llamada telefónica
    
    tiempo = int(input("¿Cuánto tiempo es la llamada (en minutos)?: "))
    es_domingo = input("¿Es Domingo? (S/N): ").strip().upper()
    
    coste = 0.0 #tipo float
    
    if es_domingo == "N":
        turno = input("¿Qué turno: Mañana o Tarde? (M/T): ").strip().upper()
    
    if tiempo <= 5:
        coste = tiempo * 100
    elif tiempo <= 8: #minuto 6, 7 y 8 a 80 céntimos
        coste = (tiempo - 5) * 80 + 500
    elif tiempo <= 10: #minuto 9 y 10 a 70 céntimos
        coste = (tiempo - 8) * 70 + 240 + 500
    else: #minutos 11 y sucesivos a 50 
        coste = (tiempo - 10) * 50 + 140 + 240 + 500
    
    if es_domingo == "S":
        coste += coste * 0.03  # 3% adicional
    else:
        if turno == "M":
            coste += coste * 0.15  # 15% adicional
        elif turno == "T":
            coste += coste * 0.10  # 10% adicional
    
    print(f"El coste de la llamada es: {coste / 100:.2f} euros.")
    ```

### Ejercicio 17

Idea clave: Cara opuesta dado: suma a 7; múltiples elif uno por valor.

??? example "Ver solución"
    ```python
    # Programa para determinar la cara opuesta de un dado de seis caras
    
    cara = int(input("Introduce el número de la cara: "))
    
    if cara == 1:
        print("SEIS")
    elif cara == 2:
        print("CINCO")
    elif cara == 3:
        print("CUATRO")
    elif cara == 4:
        print("TRES")
    elif cara == 5:
        print("DOS")
    elif cara == 6:
        print("UNO")
    else:
        print("ERROR: número incorrecto.")
    ```

### Ejercicio 18

Idea clave: Mapeo número a día; elif encadenados para cada opción.

??? example "Ver solución"
    ```python
    # Programa para mostrar el día de la semana correspondiente a un número
    
    dia = int(input("Dime un día de la semana (1-7): "))
    
    if dia == 1:
        print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miércoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:
        print("Sábado")
    elif dia == 7:
        print("Domingo")
    else:
        print("Día incorrecto")
    ```

### Ejercicio 19

Idea clave: Meses por grupos: 31, 30, 28/29 días; febrero especial.

??? example "Ver solución"
    ```python
    # Programa para determinar el número de días de un mes
    
    mes = int(input("Introduce el número de mes (1-12): "))
    
    #if mes in [1, 3, 5, 7, 8, 10, 12]:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("31 días")
    elif mes == 2:
        print("28 o 29 días")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    #elif mes in [4, 6, 9, 11]:
        print("30 días")
    else:
        print("Mes incorrecto")
    ```

### Ejercicio 20

Idea clave: Peso y zona determinan tarifa; if valida peso antes de calcular.

??? example "Ver solución"
    ```python
    # Programa para calcular el coste de transporte según el peso y la zona
    
    peso = int(input("¿Qué peso tiene el paquete (en gramos)?: "))
    
    if peso > 0 and peso <= 5000:
        print("1.- América del Norte")
        print("2.- América Central")
        print("3.- América del Sur")
        print("4.- Europa")
        print("5.- Asia")
        
        zona = int(input("¿A qué zona se reparte (1-5)?: "))
        
        if zona == 1:
            print(f"Coste: {peso * 24 / 100:.2f} euros.")
        elif zona == 2:
            print(f"Coste: {peso * 20 / 100:.2f} euros.")
        elif zona == 3:
            print(f"Coste: {peso * 21 / 100:.2f} euros.")
        elif zona == 4:
            print(f"Coste: {peso * 10 / 100:.2f} euros.")
        elif zona == 5:
            print(f"Coste: {peso * 18 / 100:.2f} euros.")
        else:
            print("Zona incorrecta.")
    else:
        print("Peso incorrecto (no podemos transportar paquetes de más de 5Kg).")
    ```
