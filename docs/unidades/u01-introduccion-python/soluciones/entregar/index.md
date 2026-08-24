# Soluciones

Estas soluciones están presentadas como contenido web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente `.py` siguen existiendo en el repositorio público, de modo que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer una solución entregable"
	- Comprueba primero si tu programa sigue la misma secuencia de pasos.
	- Fíjate en qué datos se leen por teclado y cuándo se convierten a `int` o `float`.
	- Si tu resultado no coincide, revisa la fórmula antes de reescribir todo el programa.

## Entrada, operaciones y fórmulas básicas

### Ejercicio 1. Saludo al usuario

Idea clave: el caso más simple de `input()` consiste en leer una cadena y reutilizarla directamente en la salida.

??? example "Ver solución"
	```python
	# Programa para saludar al usuario

	# Leer el nombre del usuario
	nombre = input("Dime tu nombre: ")

	# Mostrar el saludo
	print(f"Hola {nombre}")
	```

### Ejercicio 2. Perímetro y área de un rectángulo

Idea clave: una misma entrada puede participar en más de un cálculo, así que conviene guardarla una sola vez y reutilizarla.

??? example "Ver solución"
	```python
	# Calcular el perímetro y área de un rectángulo dada su base y su altura.

	# Solicitar los datos de entrada
	base = float(input("Introduce la base: "))
	altura = float(input("Introduce la altura: "))

	# Calcular el perímetro y el área
	perimetro = 2 * base + 2 * altura
	area = base * altura

	# Mostrar los resultados
	print(f"El perímetro es {perimetro} y el área es {area}")
	```

### Ejercicio 3. Hipotenusa de un triángulo rectángulo

Idea clave: cuando un ejercicio pide una raíz cuadrada, es buena ocasión para introducir `math.sqrt()` y el teorema de Pitágoras.

??? example "Ver solución"
	```python
	# Calcular la hipotenusa dados los catetos de un triángulo rectángulo

	# Importar la función sqrt para calcular la raíz cuadrada
	import math

	# Solicitar los datos de entrada
	cateto1 = float(input("Introduce el cateto 1: "))
	cateto2 = float(input("Introduce el cateto 2: "))

	# Calcular la hipotenusa usando el teorema de Pitágoras
	hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

	# Mostrar el resultado
	print(f"La hipotenusa es {hipotenusa}")
	```

### Ejercicio 4. Operaciones con dos números

Idea clave: una vez tienes dos valores numéricos, puedes mostrar varias operaciones sin necesidad de variables intermedias.

??? example "Ver solución"
	```python
	# Calcular la suma, resta, multiplicación y división de dos números

	# Solicitar los datos de entrada
	num1 = float(input("Introduce el número 1: "))
	num2 = float(input("Introduce el número 2: "))

	# Mostrar los resultados
	print(f"La suma es {num1 + num2}")
	print(f"La resta es {num1 - num2}")
	print(f"La multiplicación es {num1 * num2}")
	print(f"La división es {num1 / num2}")
	```

### Ejercicio 5. Conversión de Fahrenheit a Celsius

Idea clave: aquí lo importante es trasladar una fórmula matemática al código respetando el orden de operaciones.

??? example "Ver solución"
	```python
	# Convertir un valor de grados Fahrenheit a grados Celsius

	# Solicitar la temperatura en grados Fahrenheit
	fahrenheit = float(input("Introduce la temperatura en °F: "))

	# Calcular los grados Celsius
	celsius = (fahrenheit - 32) * 5 / 9

	# Mostrar el resultado en grados Celsius
	print(f"La temperatura es {celsius:.2f} °C.")
	```

### Ejercicio 6. Media de tres números

Idea clave: la media siempre repite el mismo patrón: sumar todos los valores y dividir entre cuántos hay.

??? example "Ver solución"
	```python
	# Calcular la media de tres números pedidos por teclado

	# Solicitar los tres números
	num1 = float(input("Introduce el número 1: "))
	num2 = float(input("Introduce el número 2: "))
	num3 = float(input("Introduce el número 3: "))

	# Calcular la media
	media = (num1 + num2 + num3) / 3

	# Mostrar el resultado
	print(f"La media es {media:.2f}")
	```

### Ejercicio 7. Minutos convertidos en horas y minutos

Idea clave: la división entera `//` y el resto `%` suelen aparecer juntos cuando descompones una cantidad en partes.

??? example "Ver solución"
	```python
	# Convertir una cantidad de minutos en horas y minutos

	# Solicitar la cantidad de minutos
	minutos = int(input("Dime la cantidad de minutos: "))

	# Calcular las horas y los minutos restantes
	res_horas = minutos // 60  # División entera para obtener las horas
	res_min = minutos % 60     # Resto para obtener los minutos sobrantes

	# Mostrar el resultado
	print(f"{res_horas} horas y {res_min} minutos.")
	```

### Ejercicio 8. Sueldo base y comisiones

Idea clave: conviene separar primero el cálculo de la comisión y después el cálculo del sueldo total.

??? example "Ver solución"
	```python
	# Calcular el sueldo total de un vendedor con comisiones por ventas

	# Solicitar el sueldo base
	sueldo_base = float(input("Dime el sueldo base: "))

	# Solicitar los valores de las tres ventas
	venta1 = float(input("Dime el precio de la venta 1: "))
	venta2 = float(input("Dime el precio de la venta 2: "))
	venta3 = float(input("Dime el precio de la venta 3: "))

	# Calcular la comisión (10% de cada venta)
	comision = venta1 * 0.1 + venta2 * 0.1 + venta3 * 0.1

	# Calcular el sueldo total
	sueldo_total = sueldo_base + comision

	# Mostrar los resultados
	print(f"Comisión por ventas: {comision:.2f}")
	print(f"Sueldo total: {sueldo_total:.2f}")
	```

### Ejercicio 9. Descuento del 15%

Idea clave: un descuento puede calcularse restando al precio original el porcentaje correspondiente.

??? example "Ver solución"
	```python
	# Calcular el precio final de una compra con un descuento del 15%

	# Solicitar el precio de la compra
	precio = float(input("Dime el precio: "))

	# Calcular el precio final aplicando el descuento del 15%
	precio_final = precio - precio * 0.15

	# Mostrar el precio final
	print(f"Precio final: {precio_final:.2f}")
	```

### Ejercicio 10. Nota final ponderada

Idea clave: cuando distintos apartados pesan diferente, conviene traducir cada porcentaje a un factor decimal.

??? example "Ver solución"
	```python
	# Calcular la nota final de un alumno en la materia de Algoritmos

	# Solicitar las notas parciales
	parcial1 = float(input("Dime la nota del parcial 1: "))
	parcial2 = float(input("Dime la nota del parcial 2: "))
	parcial3 = float(input("Dime la nota del parcial 3: "))

	# Solicitar las notas del examen final y el trabajo final
	examen = float(input("Dime la nota del examen: "))
	trabajo = float(input("Dime la nota del trabajo: "))

	# Calcular la nota final
	nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + 0.3 * examen + 0.15 * trabajo

	# Mostrar la nota final
	print(f"Nota final: {nota:.2f}")
	```

## Distancias, raíces y descomposición aritmética

### Ejercicio 11. Distancia entre dos números

Idea clave: `abs()` evita tener que decidir manualmente cuál de los dos números es mayor.

??? example "Ver solución"
	```python
	# Calcular la distancia (valor absoluto de la diferencia) entre dos números

	# Solicitar los dos números al usuario
	num1 = int(input("Dime el número 1: "))
	num2 = int(input("Dime el número 2: "))

	# Calcular la distancia (valor absoluto de la diferencia)
	distancia = abs(num1 - num2)

	# Mostrar la distancia
	print(f"Distancia: {distancia}")
	```

### Ejercicio 12. Distancia entre dos puntos

Idea clave: este ejercicio combina lectura de varios datos, potencias y raíz cuadrada en una sola expresión.

??? example "Ver solución"
	```python
	# Calcular la distancia entre dos puntos en el plano

	# Importar la función sqrt para calcular la raíz cuadrada
	import math

	# Solicitar las coordenadas del primer punto
	x1 = int(input("Dime la coordenada x1 del punto 1: "))
	y1 = int(input("Dime la coordenada y1 del punto 1: "))

	# Solicitar las coordenadas del segundo punto
	x2 = int(input("Dime la coordenada x2 del punto 2: "))
	y2 = int(input("Dime la coordenada y2 del punto 2: "))

	# Calcular la distancia entre los puntos
	distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

	# Mostrar la distancia
	print(f"Distancia: {distancia:.2f}")
	```

### Ejercicio 13. Raíz cuadrada y raíz cúbica

Idea clave: no todas las raíces se resuelven igual; aquí se mezclan `math.sqrt()` y potencias fraccionarias.

??? example "Ver solución"
	```python
	# Calcular la raíz cuadrada y cúbica de un número

	# Importar la función sqrt para calcular la raíz cuadrada
	import math

	# Solicitar el número
	num = float(input("Dime el número: "))

	# Calcular la raíz cuadrada
	raiz_cuadrada = math.sqrt(num)

	# Calcular la raíz cúbica (elevando a la potencia 1/3)
	raiz_cubica = num ** (1/3)

	# Mostrar las raíces
	print(f"Raíz cuadrada: {raiz_cuadrada:.2f}")
	print(f"Raíz cúbica: {raiz_cubica:.2f}")
	```

### Ejercicio 14. Invertir un número de dos cifras

Idea clave: descomponer primero en decenas y unidades simplifica mucho la reconstrucción del número invertido.

??? example "Ver solución"
	```python
	# Invertir un número de dos cifras y descomponerlo en decenas y unidades

	# Solicitar un número de dos cifras
	num = int(input("Dime un número de dos cifras: "))

	# Calcular decenas y unidades
	decenas = num // 10  # División entera para obtener las decenas
	unidades = num % 10  # Resto para obtener las unidades

	# Mostrar las cifras descompuestas
	print(f"Primera cifra (decenas): {decenas}")
	print(f"Segunda cifra (unidades): {unidades}")

	# Construir el número invertido
	num_invertido = unidades * 10 + decenas
	print(f"Número invertido: {num_invertido}")
	```

### Ejercicio 15. Intercambiar dos variables

Idea clave: usar una variable auxiliar permite entender el intercambio paso a paso antes de aprender formas más compactas.

??? example "Ver solución"
	```python
	# Intercambiar los valores de dos variables y mostrarlos

	# Solicitar los valores de las variables A y B
	a = int(input("Introduce el valor de la variable A: "))
	b = int(input("Introduce el valor de la variable B: "))

	# Intercambiar los valores usando una variable auxiliar
	aux = a
	a = b
	b = aux

	# Se podría hacer también usando la siguiente expresión
	# a, b = b, a

	# Mostrar los nuevos valores de las variables
	print(f"Nuevo valor de A: {a}")
	print(f"Nuevo valor de B: {b}")
	```

### Ejercicio 16. Alcance entre dos vehículos

Idea clave: la clave no es la velocidad total, sino la velocidad relativa entre ambos vehículos.

??? example "Ver solución"
	```python
	# Calcular el tiempo en minutos en que un vehículo más rápido alcanzará a otro

	# Solicitar las velocidades de los vehículos y la distancia entre ellos
	velocidad1 = float(input("Dime la velocidad del coche 1 (km/h): "))
	velocidad2 = float(input("Dime la velocidad del coche 2 (más pequeña) (km/h): "))
	distancia = float(input("Dime la distancia entre los coches (km): "))

	# Calcular el tiempo en horas para que el vehículo más rápido alcance al otro
	tiempo_horas = distancia / (velocidad1 - velocidad2)

	# Convertir el tiempo a minutos
	tiempo_minutos = tiempo_horas * 60

	# Mostrar el resultado
	print(f"Lo alcanza en {tiempo_minutos:.2f} minutos.")
	```

### Ejercicio 17. Hora de llegada

Idea clave: convertir todo a segundos evita errores cuando el tiempo de viaje hace cambiar minutos, horas o incluso de día.

??? example "Ver solución"
	```python
	# Calcular la hora de llegada a partir de la hora de salida y el tiempo de viaje en segundos

	# Solicitar la hora de salida
	horapartida = int(input("Hora de salida (HH): "))
	minpartida = int(input("Minutos de salida (MM): "))
	segpartida = int(input("Segundos de salida (SS): "))

	# Solicitar el tiempo de viaje en segundos
	segviaje = int(input("Tiempo que has tardado en segundos: "))

	# Convertir la hora de salida a segundos
	seginicial = horapartida * 3600 + minpartida * 60 + segpartida

	# Sumar el tiempo del viaje en segundos
	segfinal = seginicial + segviaje

	# Calcular la hora, minutos y segundos de llegada
	horallegada = (segfinal // 3600) % 24  # Usamos módulo 24 para mantener un formato de 24 horas
	minllegada = (segfinal % 3600) // 60
	segllegada = (segfinal % 3600) % 60

	# Mostrar la hora de llegada
	print(f"Hora de llegada: {horallegada:02}:{minllegada:02}:{segllegada:02}")
	```

## Cadenas, puntuación y monedas

### Ejercicio 18. Iniciales de una persona

Idea clave: las cadenas pueden indexarse para obtener el primer carácter de cada palabra.

??? example "Ver solución"
	```python
	# Obtener las iniciales del nombre y los apellidos de una persona

	# Solicitar el nombre y los apellidos
	nombre = input("Dime tu nombre: ")
	apellido1 = input("Dime tu primer apellido: ")
	apellido2 = input("Dime tu segundo apellido: ")

	# Obtener las iniciales (primer carácter de cada cadena) y convertirlas a mayúsculas
	iniciales = (nombre[0] + apellido1[0] + apellido2[0]).upper()

	# Mostrar las iniciales
	print(f"Las iniciales son: {iniciales}")
	```

### Ejercicio 19. Puntuación de un test

Idea clave: a veces basta con una fórmula simple; aquí las respuestas en blanco no cambian el cálculo y por eso ni siquiera se piden.

??? example "Ver solución"
	```python
	# Calcular la nota final de un estudiante basada en sus respuestas

	# Solicitar la cantidad de respuestas correctas, incorrectas y en blanco
	correctas = int(input("Dime la cantidad de respuestas correctas: "))
	incorrectas = int(input("Dime la cantidad de respuestas incorrectas: "))
	# Las respuestas en blanco no afectan el cálculo, por lo que no las pedimos

	# Calcular los puntos obtenidos
	puntos = correctas * 5 + incorrectas * (-1)

	# Mostrar los puntos finales
	print(f"Puntos: {puntos}")
	```

### Ejercicio 20. Recuento de monedas

Idea clave: puedes sumar euros y céntimos por separado y usar `%` para dejar los céntimos sobrantes por debajo de 100.

??? example "Ver solución"
	```python
	# Calcular el total de dinero en euros y céntimos según las monedas ingresadas

	# Solicitar la cantidad de monedas de cada tipo
	euro2 = int(input("Monedas de 2 euros: "))
	euro1 = int(input("Monedas de 1 euro: "))
	cent50 = int(input("Monedas de 50 céntimos: "))
	cent20 = int(input("Monedas de 20 céntimos: "))
	cent10 = int(input("Monedas de 10 céntimos: "))

	# Calcular el total de euros y céntimos
	total_euros = euro2 * 2 + euro1
	total_centimos = cent50 * 50 + cent20 * 20 + cent10 * 10

	# Convertir céntimos adicionales en euros
	total_euros += total_centimos // 100
	total_centimos = total_centimos % 100

	# Mostrar el total en euros y céntimos
	print(f"{total_euros} euros y {total_centimos} céntimos.")
	```