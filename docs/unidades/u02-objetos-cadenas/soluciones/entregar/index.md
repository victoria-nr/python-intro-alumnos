# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En esta unidad conviene fijarse en operaciones con cadenas, métodos, slicing y construcción de mensajes a partir de piezas más pequeñas.

### Ejercicio 1

Idea clave: Encadena strip() y replace() para limpiar espacios y símbolos; upper() normaliza caso.

??? example "Ver solución"
    ```python
    #Normalizar hostname de aula (strip, replace)
    # Enunciado:
    # De '   pc -- aula -  07  \n' obtener 'PC-AULA-07' sin bucles ni condicionales.
    
    texto = "   pc -- aula -  07  \n"
    print("Texto inicial: ", texto)
    
    limpio = texto.strip()
    sin_espacios = limpio.replace(" ", "")
    sin_doble = sin_espacios.replace("--", "-")
    
    normalizado = sin_doble.upper()
    
    print("Texto normalizado: ", normalizado)
    ```

### Ejercicio 2

Idea clave: find() ubica separadores; slicing extrae partes entre ellos sin bucles.

??? example "Ver solución"
    ```python
    # Prefijo y extracción de aula y número (startswith, find, [:]])
    hostname = "PC-AULA-23"
    print("Hostname: ", hostname)
    
    tiene_prefijo = hostname.startswith("PC-")
    print("Tiene el prefijo 'PC-'?: ",  tiene_prefijo)
    
    pos1 = hostname.find("-")
    resto = hostname[pos1 + 1:]
    pos2_rel = resto.find("-")
    aula = resto[:pos2_rel]
    numero = resto[pos2_rel + 1:]
    
    print("Aula: ", aula)
    print("Número: ", numero)
    ```

### Ejercicio 2b

Idea clave: find() con segundo parámetro busca desde posición; optimiza búsqueda de múltiples separadores.

??? example "Ver solución"
    ```python
    # Prefijo y extracción de aula y número (startswith, find, [:]])
    hostname = "PC-AULA-23"
    print("Hostname: ", hostname)
    
    tiene_prefijo = hostname.startswith("PC-")
    print("Tiene el prefijo 'PC-'?: ",  tiene_prefijo)
    
    pos1 = hostname.find("-")
    pos2 = hostname.find("-", pos1+1)
    aula = hostname[pos1+1:pos2]
    numero = hostname[pos2+1:]
    
    
    print("Aula:", aula)
    print("Número:", numero)
    ```

### Ejercicio 3

Idea clave: Encadena find() relativos para particionar ruta; slicing complejo pero sin bucles.

??? example "Ver solución"
    ```python
    #Partes de una ruta Windows (find, index, [:]])
    ruta = "C:\\Users\\alumno\\Desktop\\proyecto"
    print("Ruta: ", ruta)
    
    pos1 = ruta.find("\\")
    unidad = ruta[0]
    
    resto1 = ruta[pos1 + 1:]
    pos2_rel = resto1.find("\\") #hasta Users
    resto2 = resto1[pos2_rel + 1:] #desde alumno
    
    pos3_rel = resto2.find("\\") 
    usuario = resto2[:pos3_rel]
    
    resto3 = resto2[pos3_rel + 1:] # desde Desktop
    pos4_rel = resto3.find("\\")
    desktop = resto3[:pos4_rel]
    
    print("Unidad: ", unidad)
    print("Usuario: ", usuario)
    print("Carpeta: ", desktop)
    ```

### Ejercicio 3b

Idea clave: Busca todas las posiciones con find() antes de hacer slicing; estrategia predefinida.

??? example "Ver solución"
    ```python
    #Partes de una ruta Windows (find, index, [:]])
    ruta = "C:\\Users\\alumno\\Desktop\\proyecto"
    print("Ruta: ", ruta)
    
    unidad = ruta[0]
    
    pos1 = ruta.find("\\")
    
    pos2 = ruta.find("\\", pos1+1)
    
    pos3 = ruta.find("\\", pos2+1)
    
    pos4 = ruta.find("\\", pos3+1)
    
    usuario= ruta[pos2+1:pos3]
    carpeta = ruta[pos3+1:pos4]
    
    print("Unidad: ", unidad)
    print("Usuario: ", usuario)
    print("Carpeta: ", carpeta)
    ```

### Ejercicio 4

Idea clave: count() verifica estructura; find() localiza puntos; slicing extrae octetos secuencialmente.

??? example "Ver solución"
    ```python
    #Analizar y trocear IP v4 (strip, count, find, [:]])
    ip_texto = "  192.168.001.010  "
    
    print("IP: ", ip_texto)
    
    ip = ip_texto.strip()
    num_puntos = ip.count(".")
    print("Num puntos: ", num_puntos)
    
    p1 = ip.find(".")
    primer_octeto = ip[:p1]
    
    resto1 = ip[p1 + 1:]
    p2_rel = resto1.find(".")
    resto2 = resto1[p2_rel + 1:]
    p3_rel = resto2.find(".")
    ultimo_octeto = resto2[p3_rel + 1:]
    
    print("Primer octeto: ", primer_octeto)
    print("Último octeto: ", ultimo_octeto)
    ```

### Ejercicio 4b

Idea clave: find() con segunda posición evita partir la cadena; más directo para octetos.

??? example "Ver solución"
    ```python
    #Analizar y trocear IP v4 (strip, count, find, [:]])
    ip_texto = "  192.168.001.010  "
    
    print("IP: ", ip_texto)
    
    ip = ip_texto.strip()
    num_puntos = ip.count(".")
    print("Num puntos: ", num_puntos)
    
    p1 = ip.find(".")
    primer_octeto = ip[:p1]
    
    
    p2 = ip.find(".", p1+1)
    p3 = ip.find(".", p2+1)
    
    
    ultimo_octeto = ip[p3 + 1:]
    
    print("Primer octeto: ", primer_octeto)
    print("Último octeto: ", ultimo_octeto)
    ```

### Ejercicio 5

Idea clave: find() busca separadores; slicing extrae componentes; replace() cambia extensión.

??? example "Ver solución"
    ```python
    #  Fecha desde nombre de backup y cambiar extensión a .zip (find, [:]], replace)
    nombre = "backup_2025_09_03.tar.gz"
    print("Nombre de archivo: ", nombre)
    
    pos1 = nombre.find("_")
    resto1 = nombre[pos1 + 1:]
    
    
    pos2_rel = resto1.find("_")
    anio = resto1[:pos2_rel]
    
    resto2 = resto1[pos2_rel + 1:]
    pos3_rel = resto2.find("_")
    mes = resto2[:pos3_rel]
    
    resto3 = resto2[pos3_rel + 1:]
    pos4_rel = resto3.find(".")
    dia = resto3[:pos4_rel]
    
    fecha = dia + "-" + mes + "-" + anio
    print("Fecha: ", fecha)
    
    nuevo = nombre.replace(".tar.gz", ".zip")
    print("Nuevo nombre: ", nuevo)
    
    
    #este nuevo nombre no se pide en el ejercicio
    inicio_nombre = nombre[:pos1]
    nuevo_nombre_fecha = inicio_nombre + "_" + fecha + ".zip"
    print("Nuevo nombre con fecha cambiada: ", nuevo_nombre_fecha)
    ####
    ```

### Ejercicio 5b

Idea clave: Localiza todos los find() primero, luego aplica slicing; estrategia predefinida diferente.

??? example "Ver solución"
    ```python
    #  Fecha desde nombre de backup y cambiar extensión a .zip (find, [:]], replace)
    nombre = "backup_2025_09_03.tar.gz"
    print("Nombre de archivo: ", nombre)
    
    pos1 = nombre.find("_")
    
    
    
    pos2 = nombre.find("_", pos1+1)
    pos3 = nombre.find("_", pos2+1)
    pos4= nombre.find(".")
    
    anio = nombre[pos1+1:pos2]
    mes = nombre[pos2+1:pos3]
    dia = nombre[pos3+1:pos4]
    
    fecha = dia + "-" + mes + "-" + anio
    print("Fecha: ", fecha)
    
    nuevo = nombre.replace(".tar.gz", ".zip")
    print("Nuevo nombre: ", nuevo)
    
    
    #este nuevo nombre no se pide en el ejercicio
    inicio_nombre = nombre[:pos1]
    nuevo_nombre_fecha = inicio_nombre + "_" + fecha + ".zip"
    print("Nuevo nombre con fecha cambiada: ", nuevo_nombre_fecha)
    ####
    ```

### Ejercicio 6

Idea clave: index() y find() ubican caracteres clave; slicing extrae usuario, dominio y TLD.

??? example "Ver solución"
    ```python
    # Partes de un email institucional (index, find, [:]])
    email = "admin.redes@centro.edu"
    print("Email: ", email)
    
    pos_arroba = email.index("@")
    usuario = email[:pos_arroba]
    print("Usuario: ", usuario)
    
    resto = email[pos_arroba + 1:]
    pos_punto = resto.find(".")
    dominio = resto[:pos_punto]
    print("Dominio: ", dominio)
    
    tld = resto[pos_punto + 1:]
    print("Tld: ", tld)
    ```

### Ejercicio 7

Idea clave: import string accede a conjuntos de caracteres; random.choice() selecciona elementos al azar.

??? example "Ver solución"
    ```python
    # Password con patrón simple (string, random)
    import string
    import random
    
    letras = string.ascii_letters
    digitos = string.digits
    simbolos = "!#$%&*"
    
    a = random.choice(letras)
    b = random.choice(letras)
    c = random.choice(letras)
    d = random.choice(letras)
    
    e = random.choice(digitos)
    f = random.choice(digitos)
    g = random.choice(digitos)
    h = random.choice(digitos)
    
    i = random.choice(simbolos)
    j = random.choice(simbolos)
    
    password = a + b + c + d + e + f + g + h + i + j
    print("Password generada: ", password)
    ```

### Ejercicio 8

Idea clave: strip() limpia espacios; slicing toma iniciales; replace() normaliza acentos para compatibilidad.

??? example "Ver solución"
    ```python
    # Username a partir de nombre y apellido (strip, replace, [:], random, string)
    import random
    import string
    
    nombre = "  Ana  "
    apellido = "  López "
    print("Nombre y apellidos: ", nombre, " ", apellido)
    
    nombre = nombre.strip()
    apellido = apellido.strip()
    
    usuario = nombre[:3]+apellido[:3]
    
    usuario_limpio = usuario.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú','u')
    
    d1 = random.choice(string.digits)
    d2 = random.choice(string.digits)
    
    username = usuario_limpio + d1 + d2
    print("Nombre de usuario: ", username)
    ```
