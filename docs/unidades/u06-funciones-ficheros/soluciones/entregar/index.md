# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En estos ejercicios conviene fijarse en las rutas, el modo de apertura y la separación entre lectura, procesamiento y escritura.

### Ejercicio 1

Idea clave: Observa cómo capturar info del sistema con platform.system(), platform.version() y os.cpu_count().

??? example "Ver solución"
    ```python
    # Enunciado: Genera un informe system_report.txt con fecha/hora, SO (platform) y CPUs (os.cpu_count()).
    
    import platform
    import os
    from datetime import datetime
    
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    so = platform.system()
    version = platform.version()
    cpus = os.cpu_count()
    
    with open("system_report.txt", "w", encoding="utf-8") as f:
        f.write("SYSTEM REPORT\n")
        f.write(f"Fecha: {fecha}\n")
        f.write(f"Sistema: {so}\n")
        f.write(f"CPUs: {cpus}\n")
    
    print("Informe creado: system_report.txt")
    ```

### Ejercicio 2

Idea clave: Modo append añade líneas sin borrar; usa datetime.now().strftime() para timestamps automáticos.

??? example "Ver solución"
    ```python
    # Enunciado: Crea (si no existe) admin_log.txt y añade una línea con fecha/hora y un mensaje del usuario.
    
    from datetime import datetime
    
    mensaje = input("Mensaje para el log: ").strip()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("admin_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{fecha}] {mensaje}\n")
    
    print("Mensaje añadido a admin_log.txt")
    ```

### Ejercicio 3

Idea clave: Lee todas las líneas con readlines() y accede a última con [-1]; verifica existencia primero.

??? example "Ver solución"
    ```python
    # Enunciado: Lee admin_log.txt y muestra cuántas líneas contiene y cuál es la última.
    
    from pathlib import Path
    
    ruta = Path("admin_log.txt")
    
    if not ruta.exists():
        print("No existe admin_log.txt. Ejecuta antes el ejercicio 2.")
    else:
    
        with open('admin_log.txt', 'r') as f:
            lineas= f.readlines()
    
        print("Número de líneas:", len(lineas))
    
        if len(lineas) > 0:
            print("Última línea:", lineas[-1])
        else:
            print("El fichero está vacío.")
    ```

### Ejercicio 4

Idea clave: Procesa fichero validando rutas: lee línea, crea Path, usa exists(), is_dir(), is_file().

??? example "Ver solución"
    ```python
    # Enunciado: Crea paths.txt con rutas y genera paths_status.txt indicando si cada ruta existe y su tipo.
    
    from pathlib import Path
    
    # Rutas de ejemplo (puedes cambiarlas)
    rutas = ["/", "/home", "/var", "/tmp", "/noexiste"]
    
    with open("paths.txt", "w", encoding="utf-8") as f:
        for r in rutas:
            f.write(r + "\n")
    
    salida = []
    
    with open("paths.txt", "r", encoding="utf-8") as f:
        for linea in f:
            r = linea.strip()
            p = Path(r)
    
            if p.exists():
                if p.is_dir():
                    estado = "Directorio"
                elif p.is_file():
                    estado = "Archivo"
                else:
                    estado = "Otro"
            else:
                estado = "No existe"
    
            salida.append(f"{r} -> {estado}")
    
    with open("paths_status.txt", "w", encoding="utf-8") as f:
        for linea in salida:
            f.write(linea + "\n")
    
    print("Generado paths_status.txt")
    ```

### Ejercicio 5

Idea clave: split('=', 1) permite '=' en valores; lee config a diccionario para búsqueda eficiente.

??? example "Ver solución"
    ```python
    # Enunciado: Crea service.conf con clave=valor, léelo a un diccionario y consulta una clave por teclado.
    
    
    # Creamos una config de ejemplo
    with open("service.conf", "w", encoding="utf-8") as f:
        conf="port=8080\nmode=prod\nuser=admin\n"
        f.write(conf)
    
    
    config = {}
    
    with open("service.conf", "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue
            clave, valor = linea.split("=", 1)
            config[clave] = valor
    
    clave_buscada = input("Introduce una clave (port/mode/user): ").strip()
    
    if clave_buscada in config:
        print("Valor:", config[clave_buscada])
    else:
        print("La clave no existe en service.conf")
    ```

### Ejercicio 6

Idea clave: Lee fichero primero para detectar duplicados antes de append; almacena en diccionario temporal.

??? example "Ver solución"
    ```python
    # Enunciado: Pide un usuario y guarda en users.txt el nombre y /home/<usuario>. Si ya existe, no lo repitas.
    
    from pathlib import Path
    
    usuario = input("Nombre de usuario: ").strip()
    
    # Home "estimada" 
    home = str(Path("/home") / usuario)
    
    ruta = Path("users.txt")
    usuarios_guardados = {}
    
    if ruta.exists():
        with open('users.txt' , 'r') as f:
            for linea in f:
                partes = linea.split(",", 1)
                if len(partes) >= 1:
                    usuarios_guardados[partes[0].strip()]=partes[1].strip()
    
    if usuario in usuarios_guardados:
        print("Ese usuario ya estaba en users.txt")
    else:
        with open("users.txt", "a", encoding="utf-8") as f:
            f.write(f"{usuario},{home}\n")
        print("Usuario añadido a users.txt")
    ```

### Ejercicio 7

Idea clave: Valida existencia de directorios: Path.exists() e is_dir(); genera reporte de comprobaciones.

??? example "Ver solución"
    ```python
    # Enunciado: Lee users.txt y crea homes_check.txt indicando si el home existe.
    
    from pathlib import Path
    
    ruta = Path("users.txt")
    
    if not ruta.exists():
        print("No existe users.txt. Ejecuta antes el ejercicio 6.")
    else:
        salida = []
    
        with open('users.txt' , 'r') as f:
    
            for linea in f:
                usuario, home = linea.strip().split(",", 1)
                home_path = Path(home.strip())
    
                if home_path.exists() and home_path.is_dir():
                    estado = "OK"
                else:
                    estado = "NO existe"
    
                salida.append(f"{usuario.strip()} -> {home_path} -> {estado}")
    
        with open('homes_check.txt' , 'w') as f:
            for linea in salida:
                f.write(f'{linea}\n')
                
        
        print("Generado homes_check.txt")
    ```

### Ejercicio 8

Idea clave: Numera líneas con enumerate(fichero, start=1); rstrip() elimina saltos del formato.

??? example "Ver solución"
    ```python
    # Enunciado: Crea commands.txt y genera commands_numbered.txt numerando cada línea.
    
    from pathlib import Path
    
    # Comandos de ejemplo 
    comandos = [
        "ls -la",
        "df -h",
        "uname -a",
        "ps aux"
    ]
    
    Path("commands.txt").write_text("\n".join(comandos) + "\n", encoding="utf-8")
    
    salida = []
    
    with open("commands.txt", "r", encoding="utf-8") as f:
        for i, linea in enumerate(f, start=1):
            salida.append(f"{i}: {linea.rstrip()}")
    
    with open("commands_numbered.txt", "w", encoding="utf-8") as f:
        for linea in salida:
            f.write(linea + "\n")
            
    # Forma alternativa de escribir el fichero
    # Path("commands_numbered.txt").write_text("\n".join(salida) + "\n", encoding="utf-8")
    print("Generado commands_numbered.txt")
    ```

### Ejercicio 9

Idea clave: Path.iterdir() cuenta elementos de directorio; procesa lista de rutas para análisis.

??? example "Ver solución"
    ```python
    # Enunciado: Crea cleanup_plan.txt y genera cleanup_report.txt con existencia y recuento de elementos.
    
    from pathlib import Path
    
    carpetas = ["/tmp", "/var/tmp", "/noexiste"]
    
    Path("cleanup_plan.txt").write_text("\n".join(carpetas) + "\n", encoding="utf-8")
    
    salida = []
    
    with open("cleanup_plan.txt", "r", encoding="utf-8") as f:
        for linea in f:
            ruta = Path(linea.strip())
    
            if ruta.exists() and ruta.is_dir():
                cantidad = 0
                for elem in ruta.iterdir():
                    cantidad+=1
                    
                salida.append(f"{ruta} -> existe -> elementos: {cantidad}")     
                    
            else:
                salida.append(f"{ruta} -> NO existe")
    
    with open("cleanup_report.txt", "w", encoding="utf-8") as f:
        for linea in salida:
            f.write(linea + "\n")
    
    #Alternativa        
    #Path("cleanup_report.txt").write_text("\n".join(salida) + "\n", encoding="utf-8")
    print("Generado cleanup_report.txt")
    ```

### Ejercicio 10

Idea clave: sys.argv[1] recibe fichero; maneja FileNotFoundError; analiza líneas, palabras, caracteres.

??? example "Ver solución"
    ```python
    # Enunciado: Por sys.argv recibe un fichero y muestra líneas, palabras y caracteres. Error si no existe.
    
    import sys
    from pathlib import Path
    
    if len(sys.argv) < 2:
        print("Uso: python ejer10.py <fichero.txt>")
    else:
        ruta = Path(sys.argv[1])
    
        if not ruta.exists():
            print("El fichero no existe:", ruta)
        else:
            texto = ruta.read_text(encoding="utf-8")
            num_lineas = len(texto.splitlines())
            num_palabras = len(texto.split())
            num_caracteres = len(texto)
    
            print("Fichero:", ruta)
            print("Líneas:", num_lineas)
            print("Palabras:", num_palabras)
            print("Caracteres:", num_caracteres)
    ```

### Ejercicio 11

Idea clave: Lee lista de ficheros y genera comandos cp simulados; escribe salida en nuevo fichero.

??? example "Ver solución"
    ```python
    # Enunciado: Crea daily_backup_list.txt y genera backup_commands.txt simulando comandos cp (solo texto).
    
    from pathlib import Path
    
    # Lista de ejemplo (puedes editarla)
    ficheros = ["saludo.txt", "numeros.txt", "config.txt"]
    Path("daily_backup_list.txt").write_text("\n".join(ficheros) + "\n", encoding="utf-8")
    
    destino = "/backup"
    comandos = []
    
    with open("daily_backup_list.txt", "r", encoding="utf-8") as f:
        for linea in f:
            nombre = linea.strip()
            if nombre != "":
                comandos.append(f"cp {nombre} {destino}/")
    
    with open("backup_commands.txt", "w", encoding="utf-8") as f:
        for linea in comandos:
            f.write(linea + "\n")
            
    #Alternativa
    #Path("backup_commands.txt").write_text("\n".join(comandos) + "\n", encoding="utf-8")
    print("Generado backup_commands.txt")
    ```

### Ejercicio 12

Idea clave: Append contenido de fichero a otro; usa separador visual (guiones) entre anexiones.

??? example "Ver solución"
    ```python
    # Enunciado: Lee system_report.txt y lo añade a system_report_history.txt separando con guiones.
    
    from pathlib import Path
    
    informe = Path("system_report.txt")
    
    if not informe.exists():
        print("No existe system_report.txt. Ejecuta antes el ejercicio 1.")
    else:
        contenido = informe.read_text(encoding="utf-8")
    
        with open("system_report_history.txt", "a", encoding="utf-8") as f:
            f.write(contenido)
            f.write("\n" + "-" * 30 + "\n")
    
        print("Añadido informe a system_report_history.txt")
    ```

### Ejercicio 13

Idea clave: glob('*.log') busca archivos .log; .name devuelve solo nombre sin ruta completa.

??? example "Ver solución"
    ```python
    # Enunciado: En la carpeta `logs/`, muestra por pantalla el nombre de todos los ficheros que terminen en `*.log` usando `Path.glob()`.
    from pathlib import Path
    
    carpeta = Path("logs")
    
    if not carpeta.exists():
        print("No existe la carpeta 'logs'. Créala y añade algunos .log para probar.")
    else:
        for fichero in carpeta.glob("*.log"):
            print(fichero.name)
    ```

### Ejercicio 14

Idea clave: glob('*.txt') cuenta archivos de carpeta; iteración revela cantidad coincidencias.

??? example "Ver solución"
    ```python
    # Enunciado: Cuenta cuántos ficheros `*.txt` hay dentro de `datos/` (solo esa carpeta) y muestra el total.
    from pathlib import Path
    
    
    carpeta = Path("logs")
    if not carpeta.exists():
        print("No existe la carpeta 'logs'. Créala y añade algunos .txt para probar.")
    else:
        contador = 0
        for _ in carpeta.glob("*.txt"):
            contador += 1
        print("Total .txt:", contador)
    ```

### Ejercicio 15

Idea clave: stat().st_size obtiene tamaño bytes; muestra nombre y tamaño de cada fichero.

??? example "Ver solución"
    ```python
    # Enunciado: Busca `*.log` en `logs/` y muestra por pantalla: `nombre - tamaño_en_bytes` usando `path.stat().st_size`.
    from pathlib import Path
    
    carpeta = Path("logs")
    
    if not carpeta.exists():
        print("No existe la carpeta 'logs'.")
    else:
        for fichero in carpeta.glob("*.log"):
            tam = fichero.stat().st_size
            print(fichero.name, "-", tam, "bytes")
    ```
