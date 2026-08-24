# Soluciones

Estas soluciones se muestran también en formato web para que puedas compararlas desde el navegador sin tener que abrir cada archivo por separado.

Los mismos programas siguen estando en los archivos `.py` del repositorio público, así que si actualizas el repositorio con `git pull` también los tendrás en local para ejecutarlos en VS Code.

!!! note "Cómo aprovechar estas soluciones"
	- Intenta resolver primero el ejercicio por tu cuenta.
	- Antes de abrir el código, piensa qué variables, operaciones o conversiones necesitas.
	- Cuando compares, no mires solo el resultado final: fíjate también en el orden de los pasos y en los nombres de las variables.

## Retos con números

### 1. El súper cálculo

Idea clave: sumar varios valores, guardar el total y reutilizarlo para calcular la media.

??? example "Ver solución"
	```python
	# 1 El súper cálculo
	# Declara tres variables con precios de productos.
	# Calcula el total de la compra y el precio medio.
	# Muestra ambos resultados por pantalla.

	# Precios de ejemplo (puedes cambiarlos)
	precio1 = 12.50
	precio2 = 7.99
	precio3 = 3.25

	total = precio1 + precio2 + precio3
	media = total / 3

	print("Precios:", precio1, precio2, precio3)
	print("Total de la compra:", total)
	print("Precio medio:", media)
	```

### 2. La propina

Idea clave: representar un porcentaje como número decimal y multiplicarlo por el importe original.

??? example "Ver solución"
	```python
	# 2 La propina
	# Guarda el precio de una cena en una variable.
	# Calcula el 10% de propina y muéstralo.

	precio_cena = 28.90
	propina = precio_cena * 0.10

	print("Precio de la cena:", precio_cena)
	print("Propina (10%):", propina)
	```

### 3. Conversión rápida

Idea clave: cambiar de unidad exige una multiplicación clara y una variable nueva para el resultado.

??? example "Ver solución"
	```python
	# 3 Conversión rápida
	# Guarda tu altura en metros. Convierte esa altura a centímetros y muéstrala.

	altura_m = 1.68
	altura_cm = altura_m * 100

	print("Altura en metros:", altura_m)
	print("Altura en centímetros:", altura_cm)
	```

### 4. El futuro

Idea clave: separar el cálculo en pasos intermedios hace más fácil entender de dónde sale el resultado final.

??? example "Ver solución"
	```python
	# 4 El futuro
	# Guarda tu edad actual en una variable.
	# Calcula cuántos años tendrás en 2030 y muéstralo.

	edad_actual = 16
	anio_actual = 2025
	anio_objetivo = 2030

	anios_que_pasan = anio_objetivo - anio_actual
	edad_en_2030 = edad_actual + anios_que_pasan

	print("Edad actual:", edad_actual)
	print("Año actual:", anio_actual)
	print("Año objetivo:", anio_objetivo)
	print("Años que pasan:", anios_que_pasan)
	print("Tendrás en 2030:", edad_en_2030)
	```

## Retos con cadenas

### 1. Presentación personal

Idea clave: cuando mezclas texto y números en una sola frase, debes convertir el número a cadena.

??? example "Ver solución"
	```python
	# 1 Presentación personal
	# Guarda tu nombre y edad en variables.
	# Muestra un mensaje como: "Hola, me llamo Ana y tengo 16 años."

	nombre = "Ana"
	edad = 16

	#mensaje = f"Hola, me llamo {nombre} y tengo {edad} años."
	mensaje = "Hola, me llamo " + nombre + " y tengo " + str(edad) + " años."
	print(mensaje)
	```

### 2. Cuenta letras

Idea clave: `len()` no cuenta palabras, sino caracteres de la cadena completa.

??? example "Ver solución"
	```python
	# 2 Cuenta letras
	# Guarda una frase en una variable.
	# Muestra cuántos caracteres tiene con len().

	frase = "Me gusta aprender Python en ASIX"
	cantidad = len(frase)

	print("Frase: ", frase)
	print("Número de caracteres: ", cantidad)
	```

### 3. El DJ

Idea clave: una cadena más larga puede construirse a partir de piezas pequeñas guardadas en variables intermedias.

??? example "Ver solución"
	```python
	# 3 El DJ
	# Crea variables con palabras como "boom", "clap".
	# Construye una "canción" repitiendo y uniendo esas palabras.

	palabra1 = "boom"
	palabra2 = "clap"

	parte1 = palabra1 + " " + palabra2
	parte2 = palabra1 + " " + palabra1
	parte3 = palabra2 + " " + palabra2

	cancion = parte1 + " | " + parte2 + " | " + parte3
	print("Canción:", cancion)
	```

### 4. Ficha de alumno

Idea clave: varias salidas simples seguidas suelen ser más legibles que una sola línea demasiado larga.

??? example "Ver solución"
	```python
	# 4 Ficha de alumno
	# Crea variables para nombre, edad, curso y nota media.
	# Muestra una ficha con esa información.

	nombre = "Carlos"
	edad = 17
	curso = "2º ASIX"
	nota_media = 7.8

	print("--- FICHA DE ALUMNO ---")
	print("Nombre:", nombre)
	print("Edad:", edad)
	print("Curso:", curso)
	print("Nota media:", nota_media)
	```

## Retos interactivos

En esta parte conviene recordar una regla clave de Python: `input()` siempre devuelve texto. Si después quieres operar con números, primero tienes que convertir ese texto con `int()` o `float()`.

### 1. Saludo personalizado

Idea clave: si solo vas a componer un saludo, no hace falta convertir nada; basta con reutilizar el texto recibido.

??? example "Ver solución"
	```python
	# 1 Saludo personalizado
	# Pide el nombre al usuario.
	# Muestra: "Hola, [nombre], ¡bienvenido a Python!"

	nombre = input("¿Cómo te llamas? ")
	#mensaje = f"Hola, {nombre}, ¡bienvenido a Python!"
	mensaje = "Hola, " + nombre + " ¡bienvenido a Python!"
	print(mensaje)
	```

### 2. Tu edad en 2030

Idea clave: en cuanto un dato de entrada vaya a participar en una suma, conviene transformarlo a entero cuanto antes.

??? example "Ver solución"
	```python
	# 2 Tu edad en 2030
	# Pide la edad actual al usuario.
	# Calcula cuántos años tendrá en 2030 y muéstralo.

	edad_texto = input("Introduce tu edad actual: ")
	edad = int(edad_texto)

	anio_actual = 2025
	anio_objetivo = 2030

	anios_que_pasan = anio_objetivo - anio_actual
	edad_en_2030 = edad + anios_que_pasan

	print("Tu edad en 2030 será:", edad_en_2030)
	```

### 3. La calculadora sencilla

Idea clave: leer primero, convertir después y calcular al final ayuda a separar claramente las fases del programa.

??? example "Ver solución"
	```python
	# 3 La calculadora sencilla
	# Pide al usuario dos números.
	# Muestra la suma, la resta, la multiplicación y la división.

	a_texto = input("Primer número: ")
	b_texto = input("Segundo número: ")

	a = float(a_texto)
	b = float(b_texto)

	suma = a + b
	resta = a - b
	multiplicacion = a * b
	division = a / b

	print("Suma:", suma)
	print("Resta:", resta)
	print("Multiplicación:", multiplicacion)
	print("División:", division)
	```

### 4. El doble y el triple

Idea clave: una vez convertido el dato de entrada, puedes reutilizar la misma variable para varios cálculos relacionados.

??? example "Ver solución"
	```python
	# 4 El doble y el triple
	# Pide un número.
	# Muestra su doble y su triple en frases diferentes.

	n_texto = input("Introduce un número: ")
	n = float(n_texto)

	doble = n * 2
	triple = n * 3

	print("El doble es:", doble)
	print("El triple es:", triple)
	```
