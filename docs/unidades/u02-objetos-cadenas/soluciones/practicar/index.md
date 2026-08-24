# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En esta unidad conviene fijarse en operaciones con cadenas, métodos, slicing y construcción de mensajes a partir de piezas más pequeñas.

### Ejercicio 1

Idea clave: Las cadenas multilínea con triples comillas permiten saltos de línea sin secuencias de escape.

??? example "Ver solución"
    ```python
    # Crear cadenas con diferentes comillas
    cadena1 = 'Esta es una cadena con comillas simples.'
    cadena2 = "Esta es una cadena con comillas dobles."
    cadena3 = """Esta es una cadena
    multilínea con comillas triples."""
    # Imprimir las cadenas
    print(cadena1)
    print(cadena2)
    print(cadena3)
    ```

### Ejercicio 2

Idea clave: Los f-strings integran variables directamente en la cadena con sintaxis {variable}.

??? example "Ver solución"
    ```python
    # Solicitar datos al usuario
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    ciudad = input("Escribe tu ciudad de nacimiento: ")
    # Concatenar cadenas
    resultado = f"Hola, mi nombre es {nombre} {apellido} y nací en {ciudad}."
    # Imprimir el resultado
    print(resultado)
    ```

### Ejercicio 3

Idea clave: El operador * sobre cadenas repite la cadena, diferente que en números.

??? example "Ver solución"
    ```python
    # Solicitar datos al usuario
    palabra = input("Escribe una palabra: ")
    numero = int(input("Escribe un número: "))
    # Repetir la palabra
    resultado = palabra * numero
    # Imprimir el resultado
    print(resultado)
    ```

### Ejercicio 4

Idea clave: Los índices negativos acceden desde el final; los slices [:] extraen subcadenas.

??? example "Ver solución"
    ```python
    # Dada la frase
    frase = "Python es genial"
    # Imprimir caracteres según los índices
    print("Primer carácter:", frase[0])
    print("Último carácter:", frase[-1])
    print("Caracteres del índice 7 al 9:", frase[7:10])
    ```

### Ejercicio 5

Idea clave: Convierte la cadena a número antes de operarla; la multiplicación es diferente luego.

??? example "Ver solución"
    ```python
    # Solicitar número como cadena
    numero_str = input("Escribe un número: ")
    # Convertir a entero y multiplicar por 10
    numero = int(numero_str)
    resultado = numero * 10
    # Imprimir el resultado
    print("El número multiplicado por 10 es:", resultado)
    ```

### Ejercicio 6

Idea clave: Las secuencias \n y \t formatean texto; \ permite comillas dentro de cadenas.

??? example "Ver solución"
    ```python
    # Crear una cadena con secuencias de escape
    cadena = "Esta es una 'cadena' con comillas dobles,\nun salto de línea y \tuna tabulación."
    # Imprimir la cadena
    print(cadena)
    ```

### Ejercicio 7

Idea clave: El tercer parámetro del slice (paso) selecciona cada N-ésimo carácter: [::2] salta uno.

??? example "Ver solución"
    ```python
    # Solicitar una frase al usuario
    frase = input("Escribe una frase: ")
    # Obtener subcadenas
    print("Primeros 5 caracteres:", frase[:5])
    print("Últimos 5 caracteres:", frase[-5:])
    print("Caracteres en posiciones pares:", frase[::2])
    ```

### Ejercicio 8

Idea clave: len() cuenta caracteres en la cadena, incluyendo espacios y caracteres especiales.

??? example "Ver solución"
    ```python
    # Solicitar una frase al usuario
    frase = input("Escribe una frase: ")
    # Calcular la longitud
    longitud = len(frase)
    # Imprimir el resultado
    print("La longitud de la frase es:", longitud)
    ```

### Ejercicio 9

Idea clave: El operador in comprueba si una subcadena existe sin necesidad de bucles.

??? example "Ver solución"
    ```python
    # Solicitar una palabra al usuario
    palabra = input("Escribe una palabra: ")
    # Comprobar si 'a' está en la palabra
    resultado = 'a' in palabra
    # Imprimir el resultado
    print("¿La letra 'a' está en la palabra?:", resultado)
    ```

### Ejercicio 10

Idea clave: upper() y lower() cambian caso; title() capitaliza cada palabra por su utilidad.

??? example "Ver solución"
    ```python
    # Solicitar una frase al usuario
    frase = input("Escribe una frase: ")
    # Modificar y mostrar la frase en diferentes formatos
    print("Frase en mayúsculas:", frase.upper())
    print("Frase en minúsculas:", frase.lower())
    print("Frase en formato título:", frase.title())
    ```

### Ejercicio 11

Idea clave: Observa cómo se encadenan métodos; replace() antes de len() filtra caracteres contados.

??? example "Ver solución"
    ```python
    # Solicitar el nombre completo
    nombre_completo = input("Escribe tu nombre completo: ")
    
    # Imprimir en mayúsculas, minúsculas y formato título
    print("Nombre en mayúsculas:", nombre_completo.upper())
    print("Nombre en minúsculas:", nombre_completo.lower())
    print("Nombre en formato título:", nombre_completo.title())
    
    # Contar caracteres excluyendo espacios
    caracteres_sin_espacios = len(nombre_completo.replace(" ", ""))
    print("Número de caracteres (sin espacios):", caracteres_sin_espacios)
    ```

### Ejercicio 12

Idea clave: F-strings concatenan múltiples valores; prácticos para mensajes complejos con varios datos.

??? example "Ver solución"
    ```python
    # Solicitar información sobre la asignatura favorita
    asignatura = input("Nombre de tu asignatura favorita: ")
    creditos = input("Número de créditos: ")
    calificacion = input("Calificación obtenida: ")
    
    # Mostrar el mensaje con f-string
    print(f"Mi asignatura favorita es {asignatura}, tiene {creditos} créditos y obtuve una calificación de {calificacion}.")
    ```

### Ejercicio 13

Idea clave: El slice [::-1] invierte cadenas sin bucles; el tercer parámetro negativo es clave.

??? example "Ver solución"
    ```python
    # Solicitar una frase
    frase = input("Escribe una frase: ")
    
    # Trocear la frase
    print("Primeros 10 caracteres:", frase[:10])
    print("Últimos 10 caracteres:", frase[-10:])
    print("Caracteres de la posición 5 a la 15:", frase[5:15])
    print("Frase en orden inverso:", frase[::-1])
    ```

### Ejercicio 14

Idea clave: Las cadenas triple-comillas dentro de f-string preservan formato con saltos incorporados.

??? example "Ver solución"
    ```python
    # Solicitar información del libro
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    año = input("Año de publicación: ")
    genero = input("Género: ")
    
    # Crear la cadena multilínea
    informacion = f"""Título: {titulo}
    Autor: {autor}
    Año: {año}
    Género: {genero}
    """
    
    # Imprimir la información
    print(informacion)
    ```

### Ejercicio 15

Idea clave: Las secuencias \n y \t funcionan en f-strings; cuidado con las comillas anidadas.

??? example "Ver solución"
    ```python
    # Solicitar un mensaje corto
    mensaje = input("Escribe un mensaje corto: ")
    
    # Crear la cadena con caracteres especiales
    mensaje_modificado = f'\n\t"{mensaje}"'
    print("Mensaje con caracteres especiales:", mensaje_modificado)
    ```

### Ejercicio 16

Idea clave: Los replace() encadenados cambian múltiples caracteres secuencialmente sin alterar el original.

??? example "Ver solución"
    ```python
    # Solicitar una frase
    frase = input("Escribe una frase: ")
    
    # Reemplazar vocales con asteriscos
    frase_modificada = frase.replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
    
    # Mostrar resultados
    print("Frase original:", frase)
    print("Frase modificada:", frase_modificada)
    ```

### Ejercicio 17

Idea clave: Las cadenas se comparan alfabéticamente; == y > aplican orden lexicográfico.

??? example "Ver solución"
    ```python
    # Solicitar dos palabras
    palabra1 = input("Escribe la primera palabra: ")
    palabra2 = input("Escribe la segunda palabra: ")
    
    # Comparar palabras
    print("¿Son iguales?", palabra1 == palabra2)
    print(f"¿Es la palabra {palabra1} mayor que la palabra {palabra2}?", palabra1 > palabra2)
    ```

### Ejercicio 18

Idea clave: isnumeric() verifica si todos los caracteres son dígitos; distinto de isdigit().

??? example "Ver solución"
    ```python
    # Solicitar un número como cadena
    numero = input("Escribe un número: ")
    
    # Verificar si todos los caracteres son numéricos
    es_numerico = numero.isnumeric()
    print("¿Todos los caracteres son numéricos?", es_numerico)
    ```

### Ejercicio 19

Idea clave: Verifica subcadenas con in; funciona tanto en cadenas como en listas.

??? example "Ver solución"
    ```python
    # Solicitar una oración y una palabra
    oracion = input("Escribe una oración: ")
    palabra = input("Escribe una palabra: ")
    
    # Comprobar si la palabra está en la oración
    esta_presente = palabra in oracion
    print(f"¿La palabra '{palabra}' está en la oración? {esta_presente}")
    ```

### Ejercicio 20

Idea clave: ord() convierte carácter a código Unicode; chr() invierte el proceso.

??? example "Ver solución"
    ```python
    # Solicitar un carácter
    caracter = input("Escribe un carácter: ")
    
    # Mostrar su valor Unicode
    print("Valor Unicode del carácter: ", ord(caracter))
    
    # Solicitar valor entre 32 y 126
    unicode_valor = int(input("Escribe un valor entre 32 y 126: "))
    
    print("Carácter correspondiente: ", chr(unicode_valor))
    ```
