# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En estos ejercicios conviene mirar el recorrido, la condición de parada y qué variable se modifica en cada iteración.

### Ejercicio 1

Idea clave: iterdir() de pathlib recorre archivos; endswith() filtra extensión dentro del condicional.

??? example "Ver solución"
    ```python
    # Ejer1 - Contar logs en el directorio (for, pathlib)
    # Enunciado:
    # Recorre el directorio actual y cuenta cuántos archivos terminan en '.log'.
    # Muestra el total encontrado.
    # Librerías: from pathlib import Path
    
    from pathlib import Path
    
    carpeta = Path.cwd()
    contador = 0
    
    for elemento in carpeta.iterdir():
        if elemento.is_file():
            nombre = str(elemento.name)
            if nombre.endswith(".log"):
                contador = contador + 1
    
    print("Total de .log:", contador)
    ```

### Ejercicio 2

Idea clave: Acumula tamaños iterando archivos; stat().st_size suma bytes para comparar con 1 MB.

??? example "Ver solución"
    ```python
    # Ejer2 - Tamaño total de logs (for, pathlib, condicional)
    # Enunciado:
    # Suma el tamaño (en bytes) de todos los ficheros '.log' del directorio actual.
    # Muestra la suma y, si es mayor o igual que 1 MB, imprime 'ALTO VOLUMEN', si no, 'OK'.
    # Librerías: from pathlib import Path
    
    from pathlib import Path
    
    carpeta = Path.cwd()
    suma = 0
    
    for elemento in carpeta.iterdir():
        if elemento.is_file():
            if str(elemento.name).endswith(".log"):
                suma = suma + elemento.stat().st_size
    
    print("Suma de .log (bytes):", suma)
    if suma >= 1_048_576:
        print("ALTO VOLUMEN")
    else:
        print("OK")
    ```

### Ejercicio 3

Idea clave: while True con break; solo incrementa contador si la cadena no está vacía.

??? example "Ver solución"
    ```python
    # Ejer3 - Entrada de hostnames hasta FIN (while, cadenas)
    # Enunciado:
    # Pide hostnames al usuario hasta que escriba 'FIN'.
    # Cuenta cuántos has introducido y muestra el total al final.
    # No uses listas; solo un contador y cadenas.
    
    contador = 0
    while True:
        texto = input("Hostname (FIN para terminar): ")
        if texto == "FIN":
            break
        if len(texto) > 0:
            contador = contador + 1
    
    print("Total hostnames:", contador)
    ```

### Ejercicio 4

Idea clave: range(0, 7) genera 7 fechas; timedelta suma días, strftime() formatea resultado.

??? example "Ver solución"
    ```python
    # Ejer4 - Nombres de backup para los próximos 7 días (for, datetime)
    # Enunciado:
    # Muestra 7 nombres de backup a partir de hoy en formato 'backup_AAAA_MM_DD.zip'.
    # Librerías: from datetime import datetime, timedelta
    
    from datetime import datetime, timedelta
    
    hoy = datetime.now()
    for i in range(0, 7):
        fecha = hoy + timedelta(days=i)
        nombre = "backup_" + fecha.strftime("%Y_%m_%d") + ".zip"
        print(nombre)
    ```

### Ejercicio 5

Idea clave: while < 3 intentos con contador; isdigit() valida rango 0-100 antes de asignar.

??? example "Ver solución"
    ```python
    # Ejer5 - Umbral de disco con intentos (while, shutil.disk_usage, sys.argv)
    # Enunciado:
    # Pide un umbral de uso de disco (0-100). Si no es válido, vuelve a pedir (máximo 3 intentos).
    # Luego muestra el porcentaje real de uso del '/' y di si supera o no el umbral.
    # Librerías: import shutil
    import shutil
    
    intentos = 0
    umbral = -1
    
    while intentos < 3:
        texto = input("Umbral 0-100: ")
        if texto.isdigit():
            valor = int(texto)
            if valor >= 0 and valor <= 100:
                umbral = valor
                break
        intentos = intentos + 1
    
    total, usado, libre = shutil.disk_usage("/")
    porcentaje = int((usado * 100) / total)
    print("Uso:", porcentaje, "%")
    
    if umbral >= 0 and porcentaje >= umbral:
        print("ALERTA")
    elif umbral >= 0:
        print("OK")
    else:
        print("Umbral no válido")
    ```

### Ejercicio 5b

Idea clave: for range(3) alternativa a while contador; break sale si valor válido.

??? example "Ver solución"
    ```python
    # Ejer5 - Umbral de disco con intentos (while, shutil.disk_usage, sys.argv)
    # Enunciado:
    # Pide un umbral de uso de disco (0-100). Si no es válido, vuelve a pedir (máximo 3 intentos).
    # Luego muestra el porcentaje real de uso del '/' y di si supera o no el umbral.
    # Librerías: import shutil
    import shutil
    
    intentos = 0
    umbral = -1
    
    for intento in range(3):
        texto = input("Umbral 0-100: ")
        if texto.isdigit():
            valor = int(texto)
            if valor >= 0 and valor <= 100:
                umbral = valor
                break
    
    
    total, usado, libre = shutil.disk_usage("/")
    porcentaje = int((usado * 100) / total)
    print("Uso:", porcentaje, "%")
    
    if umbral >= 0 and porcentaje >= umbral:
        print("ALERTA")
    elif umbral >= 0:
        print("OK")
    else:
        print("Umbral no válido")
    ```

### Ejercicio 6

Idea clave: for range(1, n+1) crea N carpetas; mkdir() falla silenciosamente si ya existe.

??? example "Ver solución"
    ```python
    # Ejer6 - Crear carpetas de backup numeradas (for, pathlib)
    # Enunciado:
    # Pide un número N y crea carpetas 'backup_1' ... 'backup_N' en el directorio actual.
    # Si alguna ya existe, no pasa nada.
    # Librerías: from pathlib import Path
    
    from pathlib import Path
    
    n = int(input("¿Cuántas carpetas quieres crear? "))
    
    base = Path.cwd()
    print("Directorio base: ", base)
    for i in range(1, n + 1):
        carpeta = base / ("backup_" + str(i))
        if not carpeta.exists():
            carpeta.mkdir()
            print("Creada:", carpeta.name)
        else:
            print("Ya existe:", carpeta.name)
    ```

### Ejercicio 7

Idea clave: while True busca archivo; exists() e is_file() verifican, stat().st_size obtiene tamaño.

??? example "Ver solución"
    ```python
    # Ejer7 - Pedir archivo hasta que exista (while, pathlib)
    # Enunciado:
    # Pide al usuario un nombre de archivo hasta que exista en el directorio actual.
    # Cuando exista, muestra su tamaño en bytes.
    # Librerías: from pathlib import Path
    
    from pathlib import Path
    
    while True:
        nombre = input("Archivo en el directorio actual: ")
        p = Path.cwd() / nombre
        if p.exists() and p.is_file():
            tam = p.stat().st_size
            print("Tamaño (bytes):", tam)
            break
        else:
            print("No existe. Intenta de nuevo.")
    ```

### Ejercicio 8

Idea clave: while True con if/elif/else para menú; break en opción salida termina.

??? example "Ver solución"
    ```python
    # Ejer8 - Menú simple de administración (while, pathlib)
    # Enunciado:
    # Muestra un menú en bucle con opciones:
    # 1) Listar archivos del directorio actual
    # 2) Crear carpeta 'logs'
    # 3) Salir
    # Usa while True y condicionales.
    from pathlib import Path
    
    while True:
        print("1) Listar archivos del directorio actual")
        print("2) Crear carpeta 'logs'")
        print("3) Salir")
        op = input("Opción: ")
        if op == "1":
            for e in Path.cwd().iterdir():
                print(e.name)
        elif op == "2":
            logs = Path.cwd() / "logs"
            if not logs.exists():
                logs.mkdir()
                print("Creada carpeta 'logs'")
            else:
                print("Ya existe 'logs'")
        elif op == "3":
            print("Adiós")
            break
        else:
            print("Opción no válida")
    ```

### Ejercicio 9

Idea clave: for anidado con range; zfill(2) formatea; parents=True crea carpetas padre.

??? example "Ver solución"
    ```python
    # Ejer9 - Estructura de PCs por aula  (pathlib)
    # Enunciado:
    # Pide el nombre del aula (texto) y un número de equipos M.
    # Crea carpetas: <AULA>/PC-01, <AULA>/PC-02 ... <AULA>/PC-0M con pathlib.
    # Usa un for con range y formatea con dos dígitos.
    
    from pathlib import Path
    
    aula = input("Nombre del aula: ")
    num = int(input("Número de PCs: "))
    
    
    base = Path.cwd() / aula
    if not base.exists():
        base.mkdir()
    
    for i in range(1, num + 1):
        nombre = "PC-" + str(i).zfill(2)
        carpeta = base / nombre
        if not carpeta.exists():
            carpeta.mkdir()
            print("Creada:", carpeta)
        else:
            print("Ya existe:", carpeta)
    ```

### Ejercicio 10

Idea clave: while True con break; múltiples contadores clasifican extensiones con endswith().

??? example "Ver solución"
    ```python
    # Ejer10 - Clasificar nombres de backup introducidos (while, pathlib.suffix)
    # Enunciado:
    # Pide nombres de archivos hasta 'FIN'.
    # Cuenta cuántos terminan en '.zip' y cuántos en '.tar.gz' o '.tgz' y muéstralo al final.
    # Librerías: from pathlib import Path
    from pathlib import Path
    
    zip_count = 0
    tar_count = 0
    otros_count = 0
    
    while True:
        nombre = input("Archivo (FIN para terminar): ")
        if nombre == "FIN":
            break
        p = Path(nombre)
        # se puede utilizar también:  p.suffix
        if str(p.name).endswith(".tar.gz") or str(p.name).endswith(".tgz"):
            tar_count = tar_count + 1
        elif str(p.name).endswith(".zip"):
            zip_count = zip_count + 1
        else:
            otros_count += 1
    
    print("ZIP:", zip_count)
    print("TAR.GZ:", tar_count)
    print("OTROS:", otros_count)
    ```

### Ejercicio 11

Idea clave: for range(ini, fin+1); % 2 == 0 filtra pares; concatena partes IP.

??? example "Ver solución"
    ```python
    # Ejer11 - Rango de IPs pares (for, condicional)
    # Enunciado:
    # Pide una IP base (por ejemplo '192.168.1.') y dos números: inicio y fin del último octeto.
    # Muestra por pantalla las IPs con último octeto par entre ese rango (incluidos).
    base = input("IP base (ej: 192.168.1.): ")
    ini = int(input("Inicio: "))
    fin = int(input("Fin: "))
    
    for x in range(ini, fin + 1):
        if x % 2 == 0:
            print(base + str(x))
    ```

### Ejercicio 12

Idea clave: while True valida dos condiciones; for recorre cadena con isdigit().

??? example "Ver solución"
    ```python
    # Ejer12 - Validar contraseña simple con bucles (while + for sobre cadena)
    # Enunciado:
    # Pide una contraseña hasta que cumpla:
    # - Al menos 6 caracteres
    # - Contiene al menos un dígito
    # Usa while para repetir y un for para comprobar si algún carácter es dígito.
    while True:
        pwd = input("Contraseña: ")
        tiene_digito = False
    
        for ch in pwd:
            if ch.isdigit():
                tiene_digito = True
    
        if len(pwd) >= 6 and tiene_digito:
            print("OK")
            break
        else:
            print("No válida. Intenta de nuevo.")
    ```

### Ejercicio 13

Idea clave: for itera carpeta; stat().st_mtime compara tiempos; mantén máximo.

??? example "Ver solución"
    ```python
    # Ejer13 - Último modificado en carpeta (for, pathlib.stat)
    # Enunciado:
    # Recorre el directorio actual y muestra el archivo  con fecha de modificación más reciente.
    # Si no hay archivos, muestra "Sin archivos".
    # Librerías: from pathlib import Path
    from pathlib import Path
    
    base = Path.cwd()
    ultimo_archivo = ""
    ultimo_mtime = 0.0
    
    for elem in base.iterdir():
        if elem.is_file():
            m = elem.stat().st_mtime
            print(elem.name, "fecha: ", m)
            #si el número m es mayor, el archivo es más reciente
            if m > ultimo_mtime:
                ultimo_mtime = m
                ultimo_archivo = elem.name
    
    if ultimo_archivo != "":
        print("Archivo más reciente:", ultimo_archivo)
    else:
        print("Sin archivos")
    ```

### Ejercicio 14

Idea clave: for anidado meses-días; zfill(2) formatea; parents=True crea ancestros.

??? example "Ver solución"
    ```python
    # Ejer14 - Árbol de backups por mes y día (for anidado, pathlib)
    # Enunciado:
    # Pide el año (ej. 2025), el mes inicial y final (números) y el número de días a crear por mes (ej. 5).
    # Crea con pathlib la estructura: backups/<AÑO>/<MM>/dia_<DD>
    # Usa dos bucles for anidados (meses y días). Si existe, no pasa nada. Muestra cada ruta creada.
    from pathlib import Path
    
    año = input("Año (ej. 2025): ")
    mes_ini = int(input("Mes inicial (1-12): "))
    mes_fin = int(input("Mes final (1-12): "))
    dias = int(input("Días a crear por mes (ej. 5): "))
    
    
    base = Path.cwd() / "backups" / año
    
    for mes in range(mes_ini, mes_fin + 1):
        mes_str = str(mes).zfill(2)
        carpeta_mes = base / mes_str
        if not carpeta_mes.exists():
            carpeta_mes.mkdir(parents=True) #parents=True significa que si las carpetas padres no están creadas se crean
        for dia in range(1, dias + 1):
            dia_str = str(dia).zfill(2)
            carpeta_dia = carpeta_mes / ("dia_" + dia_str)
            if not carpeta_dia.exists():
                carpeta_dia.mkdir()
            print("Creada:", carpeta_dia)
    ```

### Ejercicio 15

Idea clave: for anidado AULA/PC; contadores por aula; suma .log totales.

??? example "Ver solución"
    ```python
    # Ejer15 - Contar logs por aula y PC (for anidado, pathlib)
    # Enunciado:
    # Pide cuántas aulas (A) y cuántos PCs por aula (P). Estructura esperada: AULA-01/PC-01 ... AULA-0A/PC-0P
    # Para cada PC, si existe la carpeta, cuenta cuántos archivos .log tiene (solo nivel actual).
    # Muestra total por aula y total general.
    from pathlib import Path
    
    A = int(input("Número de aulas: "))
    P = int(input("PCs por aula: "))
    
    base = Path.cwd()
    total_general = 0
    
    for a in range(1, A + 1):
        aula_nombre = "AULA-" + str(a).zfill(2)
        aula_dir = base / aula_nombre
        total_aula = 0
        for p in range(1, P + 1):
            pc_nombre = "PC-" + str(p).zfill(2)
            pc_dir = aula_dir / pc_nombre
            print("Carpeta: ", pc_dir)
            if pc_dir.exists() and pc_dir.is_dir():
                contador = 0
                for e in pc_dir.iterdir():
                    if e.is_file():
                        if str(e.name).endswith(".log"):
                            contador = contador + 1
                total_aula = total_aula + contador
        print("Aula:", aula_nombre, "-> logs:", total_aula)
        total_general = total_general + total_aula
    
    print("Total general de .log:", total_general)
    ```

### Ejercicio 16

Idea clave: for anidado subred:host; continue salta múltiplos de 5 con %.

??? example "Ver solución"
    ```python
    # Ejer16 - Plan de IPs por subred y host (for anidado, cadenas)
    # Enunciado:
    # Pide base tipo '192.168.'; rango subred (tercer octeto) inicio y fin; y máximo host (último octeto).
    # Para cada subred: muestra gateway x.x.<subred>.1 y luego hosts del 2 al máximo, saltando múltiplos de 5.
    
    base = input("Base (ej. 192.168.): ")
    sub_ini = int(input("Subred inicio (tercer octeto): "))
    sub_fin = int(input("Subred fin (tercer octeto): "))
    max_host = int(input("Máximo host (último octeto): "))
    
    for subred in range(sub_ini, sub_fin + 1):
        print("Subred:", base + str(subred) + ".0/24")
        print("Gateway:", base + str(subred) + ".1")
        for host in range(2, max_host + 1):
            if host % 5 == 0:
                continue
            print("Host:", base + str(subred) + "." + str(host))
    ```
