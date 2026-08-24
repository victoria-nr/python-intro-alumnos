# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En estos ejercicios conviene fijarse en las rutas, el modo de apertura y la separación entre lectura, procesamiento y escritura.

### Ejercicio 1

Idea clave: Modo 'w' crea o sobrescribe; write() agrega texto; cierre automático con context manager.

??? example "Ver solución"
    ```python
    # Enunciado: Crea un fichero llamado `saludo.txt` y escribe dentro la frase "Hola mundo".
    
    with open("saludo.txt", "w", encoding="utf-8") as f:
        f.write("Hola mundo")
    
    print("Creado saludo.txt")
    ```

### Ejercicio 2

Idea clave: Modo 'r' abre lectura; read() obtiene todo contenido como string.

??? example "Ver solución"
    ```python
    # Enunciado: Lee el contenido de `saludo.txt` y muéstralo por pantalla.
    
    with open("saludo.txt", "r", encoding="utf-8") as f:
        contenido = f.read()
    
    print(contenido)
    ```

### Ejercicio 3

Idea clave: range(1, 11) genera números; str() convierte a string para escribir en fichero.

??? example "Ver solución"
    ```python
    # Enunciado: Crea un fichero `numeros.txt` y escribe los números del 1 al 10, uno por línea.
    
    with open("numeros.txt", "w", encoding="utf-8") as f:
        for num in range(1, 11):
            f.write(str(num) + "\n")
    
    print("Creado numeros.txt")
    ```

### Ejercicio 4

Idea clave: int(linea.strip()) convierte a número; suma acumulativa con += en loop.

??? example "Ver solución"
    ```python
    # Enunciado: Lee `numeros.txt` y calcula la suma de todos los números.
    
    suma = 0
    
    with open("numeros.txt", "r", encoding="utf-8") as f:
        for linea in f:
            numero = int(linea.strip())
            suma += numero
    
    print("Suma:", suma)
    ```

### Ejercicio 5

Idea clave: % 2 == 0 detecta números pares; itera línea a línea sin cargar todo.

??? example "Ver solución"
    ```python
    # Enunciado: Lee `numeros.txt` y muestra solo los números pares.
    
    with open("numeros.txt", "r", encoding="utf-8") as f:
        for linea in f:
            numero = int(linea.strip())
            if numero % 2 == 0:
                print(numero)
    ```

### Ejercicio 6

Idea clave: input() en loop recolecta nombres; write() agrega línea con salto automático.

??? example "Ver solución"
    ```python
    # Enunciado: Crea un fichero `nombres.txt` y guarda 5 nombres pedidos por teclado, uno por línea.
    
    with open("nombres.txt", "w", encoding="utf-8") as f:
        for i in range(5):
            nombre = input(f"Nombre {i+1}: ")
            f.write(nombre + "\n")
    
    print("Creado nombres.txt")
    ```

### Ejercicio 7

Idea clave: Conteo iterando fichero línea a línea sin necesidad de readlines().

??? example "Ver solución"
    ```python
    # Enunciado: Lee `nombres.txt` y muestra cuántos nombres hay.
    
    num = 0
    
    with open("nombres.txt", "r", encoding="utf-8") as f:
        for _ in f:
            num += 1
    
        #alternativa
        #num = len(f.readlines())
    print("Cantidad de nombres:", num)
    ```

### Ejercicio 8

Idea clave: Inicializa variable vacía; compara len() de strings; mantiene más largo.

??? example "Ver solución"
    ```python
    # Enunciado: Lee `nombres.txt` y muestra el nombre más largo.
    
    mas_largo = ""
    
    with open("nombres.txt", "r", encoding="utf-8") as f:
        for linea in f:
            nombre = linea.strip()
            if len(nombre) > len(mas_largo):
                mas_largo = nombre
    
    print("Nombre más largo:", mas_largo)
    ```

### Ejercicio 9

Idea clave: Append modo 'a' sin perder líneas; datetime con formato específico.

??? example "Ver solución"
    ```python
    # Enunciado: Crea un fichero `log.txt` y añade (append) una línea con un mensaje y la hora actual.
    
    from datetime import datetime
    
    mensaje = input("Mensaje para el log: ")
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{hora}] {mensaje}\n")
    
    print(f"Añadido a log.txt [{hora}] {mensaje}")
    ```

### Ejercicio 10

Idea clave: Append agrega palabra sin sobrescribir; input() pide dato, write() lo guarda.

??? example "Ver solución"
    ```python
    # Enunciado: Pide al usuario una palabra y guárdala en `palabras.txt` sin borrar el contenido anterior.
    
    palabra = input("Introduce una palabra: ")
    
    with open("palabras.txt", "a", encoding="utf-8") as f:
        f.write(palabra + "\n")
    
    print(f"Guardado en palabras.txt la palabra: {palabra}")
    ```

### Ejercicio 11

Idea clave: Conteo líneas iterando fichero; cada línea incrementa contador acumulativo.

??? example "Ver solución"
    ```python
    # Enunciado: Lee `palabras.txt` y cuenta cuántas líneas tiene.
    
    lineas = 0
    
    with open("palabras.txt", "r", encoding="utf-8") as f:
        for _ in f:
            lineas += 1
    
    print("Número de líneas:", lineas)
    ```

### Ejercicio 12

Idea clave: Escribe frases en loop; luego lee mostrando con strip() para eliminar saltos.

??? example "Ver solución"
    ```python
    # Enunciado: Crea `frases.txt` con 3 frases y luego muéstralas sin saltos de línea.
    
    with open("frases.txt", "w", encoding="utf-8") as f:
        for i in range(3):
            frase = input(f"Frase {i+1}: ")
            f.write(frase + "\n")
    
    print("\nFrasess:")
    with open("frases.txt", "r", encoding="utf-8") as f:
        for linea in f:
            print(linea.strip())
    ```

### Ejercicio 13

Idea clave: lower() minúsculas para búsqueda case-insensitive; detecta letra 'a' en frases.

??? example "Ver solución"
    ```python
    # Enunciado: Lee `frases.txt` y muestra solo las frases que contienen la letra 'a'.
    
    with open("frases.txt", "r", encoding="utf-8") as f:
        for linea in f:
            frase = linea.strip()
            if "a" in frase.lower():
                print(frase)
    ```

### Ejercicio 14

Idea clave: split(',') separa nombre-edad; read() procesa parejas iterando líneas.

??? example "Ver solución"
    ```python
    # Enunciado: Crea `datos.csv` con 3 líneas `nombre,edad` y luego muestra cada par.
    
    with open("datos.csv", "w", encoding="utf-8") as f:
        for _ in range(3):
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            f.write(nombre + "," + edad + "\n")
    
    print("\nFichero creado")
    print("Contenido: ")
    with open("datos.csv", "r", encoding="utf-8") as f:
        for linea in f:
            nombre, edad = linea.strip().split(",")
            print("Nombre:", nombre, "- Edad:", edad)
    ```

### Ejercicio 15

Idea clave: Parsea CSV con split(','); int(edad) convierte; diccionario {nombre: edad}.

??? example "Ver solución"
    ```python
    # Enunciado: Lee `datos.csv` y crea un diccionario {nombre: edad}. Muéstralo.
    
    personas = {}
    
    with open("datos.csv", "r", encoding="utf-8") as f:
        for linea in f:
            nombre, edad = linea.strip().split(",")
            personas[nombre] = int(edad)
    
    print(personas)
    ```

### Ejercicio 16

Idea clave: Lee-suma-escribe ciclo: int(read), +=, str(write); inicializa si no existe.

??? example "Ver solución"
    ```python
    # Enunciado: Crea `contador.txt` con un número inicial, léelo, suma 1 y vuelve a guardarlo.
    
    from pathlib import Path
    
    ruta = Path("contador.txt")
    
    # Si no existe, lo inicializamos a 0
    if not ruta.exists():
        with open("contador.txt", "w", encoding="utf-8") as f:
            f.write("0")
    
    
    with open("contador.txt", "r", encoding="utf-8") as f:
        valor = int(f.read().strip())
    
    
    valor += 1
    
    
    with open("contador.txt", "w", encoding="utf-8") as f:
        f.write(str(valor))
    
    print("Nuevo valor:", valor)
    ```

### Ejercicio 17

Idea clave: split('=') parsea línea a clave-valor; diccionario almacena config.

??? example "Ver solución"
    ```python
    # Enunciado: Crea `config.txt` con `clave=valor`, léelo y crea un diccionario con esa configuración.
    
    # Creamos un ejemplo de config (si ya existe, se sobrescribe)
    with open("config.txt", "w", encoding="utf-8") as f:
        f.write("usuario=admin\n")
        f.write("modo=produccion\n")
        f.write("puerto=8080\n")
    
    config = {}
    
    with open("config.txt", "r", encoding="utf-8") as f:
        for linea in f:
            clave, valor = linea.strip().split("=")
            config[clave] = valor
    
    print(config)
    ```

### Ejercicio 18

Idea clave: Búsqueda en diccionario; in verifica existencia antes de acceder valor.

??? example "Ver solución"
    ```python
    # Enunciado: Lee `config.txt` y pregunta una clave. Si existe, muestra el valor.
    
    config = {}
    
    with open("config.txt", "r", encoding="utf-8") as f:
        for linea in f:
            clave, valor = linea.strip().split("=")
            config[clave] = valor
    
    clave_buscada = input("Introduce una clave: ")
    
    if clave_buscada in config:
        print("Valor:", config[clave_buscada])
    else:
        print("La clave no existe.")
    ```

### Ejercicio 19

Idea clave: read() fichero origen, write() destino; content como intermediario.

??? example "Ver solución"
    ```python
    # Enunciado: Crea `backup.txt` copiando el contenido de `saludo.txt`.
    
    with open("saludo.txt", "r", encoding="utf-8") as origen:
        contenido = origen.read()
    
    with open("backup.txt", "w", encoding="utf-8") as destino:
        destino.write(contenido)
    
    print("Copia creada en backup.txt")
    ```

### Ejercicio 20

Idea clave: try/except FileNotFoundError captura error; manejo graceful de fichero inexistente.

??? example "Ver solución"
    ```python
    # Enunciado: Lee un fichero indicado por el usuario y controla si no existe.
    
    nombre = input("Introduce el nombre del fichero a leer: ")
    
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("El fichero no existe. Revisa el nombre y la ruta.")
    ```
