# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En este bloque conviene fijarse en cómo se expresan las condiciones y en cómo se separan los distintos casos posibles.

### Ejercicio 1

Idea clave: Usa argumentos de línea de comandos con sys.argv, calcula porcentaje comparando con umbral.

??? example "Ver solución"
    ```python
    # Alerta por uso de disco
    # Pistas: shutil.disk_usage, sys.argv
    # Pide (por argumento) un umbral de uso de disco en porcentaje (por ejemplo, 85).
    # Obtén el uso de disco de la partición raíz y muestra:
    # - "ALERTA" si el porcentaje es mayor o igual que el umbral
    # - "OK" en caso contrario.
    
    import sys
    import shutil
    
    if len(sys.argv) >= 2:
        umbral = int(sys.argv[1])
    else:
        umbral = 85
    
    
    total, usado, libre = shutil.disk_usage("/")
    
    porcentaje = int((usado * 100) / total)
    
    print("Uso:", porcentaje, "%", "| Umbral:", umbral, "%")
    if porcentaje >= umbral:
        print("ALERTA: uso alto de disco")
    else:
        print("OK: dentro de límites")
    ```

### Ejercicio 2

Idea clave: datetime.now().hour devuelve la hora actual; usa elif para múltiples rangos horarios.

??? example "Ver solución"
    ```python
    # Turno de backup según hora 
    # Pistas: datetime
    # Obtén la hora actual y muestra:
    # - "Backup de mañana" si hora < 12
    # - "Backup de tarde" si 12 <= hora < 20
    # - "Backup nocturno" si hora >= 20
    from datetime import datetime
    
    ahora = datetime.now()
    print(ahora)
    hora = ahora.hour
    
    print("Hora actual:", hora)
    if hora < 12:
        print("Backup de mañana")
    elif hora < 20:
        print("Backup de tarde")
    else:
        print("Backup nocturno")
    ```

### Ejercicio 3

Idea clave: platform.system() detecta el SO; elif encadenados evalúan condiciones excluyentes.

??? example "Ver solución"
    ```python
    #Pistas: librería platform 
    #Detecta e imprime el sistema operativo, la versión y el procesador del equipo
    #  en donde se ejecuta el script. A continuación, muestra el gestor de paquetes 
    # recomendado según las siguientes indicaciones: 
    #- Windows -> "winget" 
    #- Linux -> "apt" 
    #- macOS (Darwin) -> "brew" 
    #Para otros sistemas, muestra "gestor no definido". 
    import platform
    
    so = platform.system()
    print("SO:", so)
    print("Versión: ", platform.release())
    print("Procesador: ", platform.processor())
    
    
    if so == "Windows":
        print("Gestor recomendado: winget")
    elif so == "Linux":
        print("Gestor recomendado: apt")
    elif so == "Darwin":
        print("Gestor recomendado: brew")
    else:
        print("Gestor no definido")
    ```

### Ejercicio 4

Idea clave: Combina startswith() y len() con and; la validación requiere ambas condiciones.

??? example "Ver solución"
    ```python
    # E04 - Validar hostname con ciertas características
    #Pistas: sys.argv 
    #Dado un hostname (que se pide como argumento), muestra: 
    #- "VÁLIDO" si empieza por "PC-" y su longitud es al menos 7 
    #- "NO VÁLIDO" en caso contrario 
    import sys
    
    if len(sys.argv) >= 2:
        hostname = sys.argv[1].strip() #"PC-AULA-23"
    else:
        print("Hostname no introducido")
        sys.exit()
    
    print("Hostname:", hostname)
    
    if hostname.startswith("PC-") and len(hostname) >= 7:
        print("VÁLIDO")
    else:
        print("NO VÁLIDO")
    ```

### Ejercicio 5

Idea clave: pathlib.Path.exists() y mkdir() crean carpeta si falta; condicional if/else decide.

??? example "Ver solución"
    ```python
    # Preparar carpeta de logs 
    #Pistas: librería pathlib, librería os 
    #Obtén el directorio actual con la clase Path de la librería pathlib 
    # e imprímelo por pantalla.  
    # Obtén su contenido con la función listdir de la librería os 
    # e imprime por pantalla. 
    # A continuación,  comprueba si existe la carpeta "logs" en el directorio actual.
    # Para ello, monta tú mismo la ruta para que sea de tipo Path. 
    #- Si no existe, créala y muestra "Carpeta creada". 
    #- Si existe, muestra "Carpeta ya existe". 
    
    from pathlib import Path
    import os
    
    dir_actual = Path.cwd()
    print("Directorio actual: ", dir_actual)
    
    contenido = os.listdir(dir_actual)
    print("Contenido: ", contenido)
    
    
    ruta_logs = dir_actual / "logs"
    
    if not ruta_logs.exists():
        ruta_logs.mkdir()
        print("Carpeta creada:", ruta_logs)
    else:
        print("Carpeta ya existe:", ruta_logs)
    ```

### Ejercicio 6

Idea clave: shutil.copy() duplica archivos; verifica origen con exists() antes de copiar.

??? example "Ver solución"
    ```python
    # Copiar fichero de configuración de ejemplo si falta 
    #Pistas: librerías pathlib, shutil. Para trabajar con las rutas a los ficheros,
    #  utiliza la clase Path de pathlib. Para copiar ficheros, utilizar la función copy 
    # de shutil. 
    #En el directorio actual, si NO existe un fichero llamado "config.ini", 
    # copia el fichero "config.example.ini" a "config.ini". Deberás comprobar también 
    # que el fichero "config.example.ini" exista, si no, muestra el mensaje 
    # “Falta el archivo de ejemplo”. 
    #Si ya existe "config.ini", muestra el mensaje "Config existente".
    #  
    from pathlib import Path
    import shutil
    
    ejemplo = Path.cwd() / "config.example.ini"
    destino = Path.cwd() / "config.ini"
    
    if not destino.exists():
        if ejemplo.exists():
            shutil.copy(ejemplo, destino)
            print("Copiado:", destino.name)
        else:
            print("Falta el archivo de ejemplo:", ejemplo.name)
    else:
        print("Config existente")
    ```

### Ejercicio 7

Idea clave: datetime.now().weekday() retorna 0-6 (lunes-domingo); compara si >= 5 para fin semana.

??? example "Ver solución"
    ```python
    # Mantenimiento fin de semana 
    #Pistas: librería datetime 
    #Realiza un programa que averigue qué día de la semana es el día actual y
    #  muestre  "Ventana de mantenimiento" si es sábado (día 5) o domingo (día 6). 
    # En caso contrario, muestra "Operación normal". 
    from datetime import datetime
    
    dia_semana = datetime.now().weekday()  # 0=lunes ... 6=domingo
    
    print("Día de la semana:", dia_semana)
    if dia_semana >= 5:
        print("Ventana de mantenimiento")
    else:
        print("Operación normal")
    ```

### Ejercicio 8

Idea clave: stat().st_size obtiene bytes del archivo; comparación con 1_048_576 identifica tamaño.

??? example "Ver solución"
    ```python
    # Clasificar archivo según su tamaño 
    #Pistas: librería sys y librería pathlib 
    #Pide como argumento un nombre de archivo y averigua su tamaño. 
    # Si su tamaño es >= 1 MB muestra "GRANDE", 
    # en caso contrario "PEQUEÑO". (1 MB = 1_048_576 bytes) 
    
    import sys
    from pathlib import Path
    
    if len(sys.argv) >= 2:
        archivo = Path(sys.argv[1].strip())
    else: 
        print("No se ha dado el nombre del archivo")
        sys.exit()
    
    
    size = 0
    print(Path.cwd())
    if archivo.exists():
        size = archivo.stat().st_size
    else:
        print("El archivo ", archivo, "no existe")
        sys.exit()
    
    print("Archivo: ", archivo) 
    print("Tamaño (bytes):", size)
    if size >= 1_048_576:
        print("GRANDE")
    else:
        print("PEQUEÑO")
    ```
