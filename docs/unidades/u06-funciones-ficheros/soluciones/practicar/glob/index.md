# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En esta sección la idea importante es relacionar cada patrón de glob con los archivos que realmente captura.

## Programas de solución

### Ejercicio 01

Idea clave: glob('*.log') busca .log; .name devuelve solo nombre; genera lista iterable.

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

### Ejercicio 02

Idea clave: glob('*.txt') carpeta específica; contador incrementa sin readlines().

??? example "Ver solución"
    ```python
    # Enunciado: Cuenta cuántos ficheros `*.txt` hay dentro de `datos/` (solo esa carpeta) y muestra el total.
    from pathlib import Path
    
    carpeta = Path("datos")
    
    if not carpeta.exists():
        print("No existe la carpeta 'datos'. Créala y añade algunos .txt para probar.")
    else:
        contador = 0
        for _ in carpeta.glob("*.txt"):
            contador += 1
        print("Total .txt:", contador)
    ```

### Ejercicio 03

Idea clave: stat().st_size accede tamaño bytes; .name muestra nombre archivo.

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

### Ejercicio 04

Idea clave: glob('*.tmp') y glob('*.bak') separados; salida acumula múltiples extensiones.

??? example "Ver solución"
    ```python
    # Enunciado: Busca en `temp/` ficheros `.tmp` o `.bak` y genera `cleanup_plan.txt` con las rutas (una por línea). No borres nada.
    from pathlib import Path
    
    carpeta = Path("temp")
    salida = []
    
    if not carpeta.exists():
        print("No existe la carpeta 'temp'. Créala y añade ficheros .tmp/.bak para probar.")
    else:
        for fichero in carpeta.glob("*.tmp"):
            salida.append(str(fichero))
        for fichero in carpeta.glob("*.bak"):
            salida.append(str(fichero))
    
        with open("cleanup_plan.txt", "w", encoding="utf-8") as f:
            for ruta in salida:
                f.write(ruta + "\n")
    
        print("Generado cleanup_plan.txt con", len(salida), "rutas.")
    ```

### Ejercicio 05

Idea clave: rglob('*.conf') recursivo subcarpetas; relative_to() da ruta relativa desde base.

??? example "Ver solución"
    ```python
    # Enunciado: En `configs/` (con subcarpetas), busca `*.conf` con `rglob()` y guarda en `conf_list.txt` su ruta relativa.
    from pathlib import Path
    
    base = Path("configs")
    
    if not base.exists():
        print("No existe la carpeta 'configs'. Créala con subcarpetas y ficheros .conf para probar.")
    else:
        rutas_relativas = []
        for fichero in base.rglob("*.conf"):
            rutas_relativas.append(str(fichero.relative_to(base)))
    
        Path("conf_list.txt").write_text("\n".join(rutas_relativas) + ("\n" if rutas_relativas else ""), encoding="utf-8")
        print("Generado conf_list.txt con", len(rutas_relativas), "ficheros .conf")
    ```

### Ejercicio 06

Idea clave: glob('*') obtiene todo; ' ' in p.name detecta espacios en nombres.

??? example "Ver solución"
    ```python
    # Enunciado: En `shared/`, encuentra ficheros cuyo nombre contenga espacios y muestra un aviso por pantalla.
    from pathlib import Path
    
    carpeta = Path("shared")
    
    if not carpeta.exists():
        print("No existe la carpeta 'shared'. Créala y añade ficheros con espacios para probar.")
    else:
        encontrados = 0
        for p in carpeta.glob("*"):
            if " " in p.name:
                print("Nombre con espacios:", p.name)
                encontrados += 1
        if encontrados == 0:
            print("No se encontraron nombres con espacios.")
    ```

### Ejercicio 07

Idea clave: glob('*') con is_file() filtra ficheros; p.suffix da extensión.

??? example "Ver solución"
    ```python
    # Enunciado: En `inventario/`, crea un diccionario {extension: cantidad} usando `glob('*')`.
    from pathlib import Path
    
    carpeta = Path("inventario")
    
    if not carpeta.exists():
        print("No existe la carpeta 'inventario'. Créala y añade ficheros de distintos tipos.")
    else:
        conteo = {}
    
        for p in carpeta.glob("*"):
            if p.is_file():
                ext = p.suffix
                if ext == "":
                    ext = "(sin_ext)"
                if ext not in conteo:
                    conteo[ext] = 0
                conteo[ext] += 1
    
        print(conteo)
    ```

### Ejercicio 08

Idea clave: glob('*.log.*') patrón para rotados; contador incrementa en loop.

??? example "Ver solución"
    ```python
    # Enunciado: En `logs/`, busca ficheros rotados con el patrón `*.log.*` y cuenta cuántos hay.
    from pathlib import Path
    
    carpeta = Path("logs")
    
    if not carpeta.exists():
        print("No existe la carpeta 'logs'.")
    else:
        contador = 0
        for _ in carpeta.glob("*.log.*"):
            contador += 1
        print("Logs rotados encontrados:", contador)
    ```

### Ejercicio 09

Idea clave: rglob('*.conf') con shutil.copy2() preserva metadatos; mkdir(exist_ok=True).

??? example "Ver solución"
    ```python
    # Enunciado: Copia todos los `*.conf` encontrados en `configs/` (recursivo) a `backup_configs/` usando `shutil.copy2`.
    from pathlib import Path
    import shutil
    
    origen = Path("configs")
    destino = Path("backup_configs")
    
    if not origen.exists():
        print("No existe la carpeta 'configs'.")
    else:
        destino.mkdir(exist_ok=True)
    
        copiados = 0
        for fichero in origen.rglob("*.conf"):
            destino_fichero = destino / fichero.name
            shutil.copy2(fichero, destino_fichero)
            copiados += 1
    
        print("Copiados", copiados, "ficheros .conf a", destino)
    ```

### Ejercicio 10

Idea clave: glob('*.py'), glob('*.txt'), is_dir() valida estructura mínima proyecto.

??? example "Ver solución"
    ```python
    # Enunciado: Comprueba en `proyecto/` si existe al menos un `*.py`, un `*.txt` y la carpeta `data/`.
    from pathlib import Path
    
    base = Path("proyecto")
    
    tiene_py = False
    tiene_txt = False
    tiene_data = False
    
    if not base.exists():
        print("No existe la carpeta 'proyecto'.")
    else:
        for _ in base.glob("*.py"):
            tiene_py = True
            break
    
        for _ in base.glob("*.txt"):
            tiene_txt = True
            break
    
        data_dir = base / "data"
        if data_dir.exists() and data_dir.is_dir():
            tiene_data = True
    
        if tiene_py and tiene_txt and tiene_data:
            print("OK: estructura mínima encontrada.")
        else:
            if not tiene_py:
                print("Falta: al menos un fichero .py en proyecto/")
            if not tiene_txt:
                print("Falta: al menos un fichero .txt en proyecto/")
            if not tiene_data:
                print("Falta: la carpeta proyecto/data/")
    ```

## Archivos de prueba

Estos archivos de prueba sirven para comprobar si los patrones localizan exactamente los nombres esperados y excluyen los que no corresponden.

### Archivo de prueba: configs/app.conf

Idea clave: Fichero .conf capturado por glob('*.conf') o rglob('*.conf').

??? example "Ver archivo de apoyo"
    ```ini
    port=8080
    mode=prod
    ```

### Archivo de prueba: configs/db.conf

Idea clave: Otro .conf en raíz; ambos aparecen en mismo glob('*.conf').

??? example "Ver archivo de apoyo"
    ```ini
    host=localhost
    user=admin
    ```

### Archivo de prueba: configs/sub1/nginx.conf

Idea clave: En subcarpeta; solo aparece rglob('*.conf'), no glob().

??? example "Ver archivo de apoyo"
    ```ini
    worker_processes=1
    ```

### Archivo de prueba: configs/sub1/notes.txt

Idea clave: Fichero .txt subcarpeta; no coincide *.conf recursivo.

??? example "Ver archivo de apoyo"
    ```text
    no conf
    ```

### Archivo de prueba: configs/sub1/site.conf

Idea clave: En subcarpeta; capturado solo por rglob('*.conf').

??? example "Ver archivo de apoyo"
    ```ini
    server_name=example
    ```

### Archivo de prueba: datos/datos_1.txt

Idea clave: Primer .txt; aparece glob('*.txt') dentro datos/.

??? example "Ver archivo de apoyo"
    ```text
    Linea 1
    Linea 2
    Archivo 1
    ```

### Archivo de prueba: datos/datos_2.txt

Idea clave: Segundo .txt en glob('*.txt') junto datos_1 y datos_3.

??? example "Ver archivo de apoyo"
    ```text
    Linea 1
    Linea 2
    Archivo 2
    ```

### Archivo de prueba: datos/datos_3.txt

Idea clave: Tercero .txt; todos cuentan en glob('*.txt') total.

??? example "Ver archivo de apoyo"
    ```text
    Linea 1
    Linea 2
    Archivo 3
    ```

### Archivo de prueba: datos/notas.csv

Idea clave: Fichero .csv; NO coincide glob('*.txt'), extensión diferente.

??? example "Ver archivo de apoyo"
    ```csv
    a,b,c
    1,2,3
    ```

### Archivo de prueba: GUIDE.md

Idea clave: Fichero .md; no coincide patrones log, txt, conf, tmp, bak.

??? example "Ver archivo de apoyo"
    ```markdown
    # Carpeta de práctica para ejercicios de glob (pathlib)
    
    1. Copia esta carpeta en tu ordenador (o descomprime el zip).
    2. Abre una terminal en esta carpeta.
    3. Ejecuta los ejercicios desde aquí, por ejemplo:
       - python Ejercicio_01.py
    
    Estructura creada:
    - logs/ (logs y logs rotados)
    - configs/ (con subcarpetas y .conf)
    - temp/ (ficheros .tmp y .bak)
    - datos/ (varios .txt)
    - shared/ (nombres con espacios)
    - inventario/ (extensiones variadas)
    - proyecto/ (estructura mínima con data/)
    ```

### Archivo de prueba: inventario/config.conf

Idea clave: Fichero .conf aquí; extensión diferente de otros directorio.

??? example "Ver archivo de apoyo"
    ```ini
    x=1
    ```

### Archivo de prueba: inventario/datos.txt

Idea clave: Fichero .txt; glob('*') lo captura búsqueda todo.

??? example "Ver archivo de apoyo"
    ```text
    texto
    ```

### Archivo de prueba: inventario/log.log

Idea clave: Fichero .log; similar otros pero carpeta inventario.

??? example "Ver archivo de apoyo"
    ```text
    log
    ```

### Archivo de prueba: inventario/script.py

Idea clave: Fichero .py; no coincide patrones principales ejercicio.

??? example "Ver archivo de apoyo"
    ```python
    print('hola')
    ```

### Archivo de prueba: inventario/sin_extension

Idea clave: Sin extensión; detectado (sin_ext) en conteo diccionario.

??? example "Ver archivo de apoyo"
    ```text
    nada
    ```

### Archivo de prueba: logs/auth.log

Idea clave: Fichero .log capturado glob('*.log').

??? example "Ver archivo de apoyo"
    ```text
    INFO auth ok
    WARN auth slow
    ```

### Archivo de prueba: logs/auth.log.1

Idea clave: Rotado; capturado glob('*.log.*'), patrón logs antiguos.

??? example "Ver archivo de apoyo"
    ```text
    OLD auth lines
    ```

### Archivo de prueba: logs/nginx.log

Idea clave: Otro .log; junto auth.log en mismo glob.

??? example "Ver archivo de apoyo"
    ```text
    GET / 200
    GET /admin 403
    ```

### Archivo de prueba: logs/readme.txt

Idea clave: Fichero .txt carpeta logs; NO coincide glob('*.log').

??? example "Ver archivo de apoyo"
    ```text
    Esto no es un log
    ```

### Archivo de prueba: logs/sys.log

Idea clave: Fichero .log; capturado glob('*.log') como demás.

??? example "Ver archivo de apoyo"
    ```text
    INFO system boot
    ```

### Archivo de prueba: logs/sys.log.2

Idea clave: Log rotado antiguo; capturado glob('*.log.*').

??? example "Ver archivo de apoyo"
    ```text
    OLD sys lines
    ```

### Archivo de prueba: proyecto/data/input.txt

Idea clave: En subcarpeta data/; verifica directorio existe.

??? example "Ver archivo de apoyo"
    ```text
    data
    ```

### Archivo de prueba: proyecto/main.py

Idea clave: Fichero .py raíz proyecto/; verifica estructura.

??? example "Ver archivo de apoyo"
    ```python
    print('proyecto')
    ```

### Archivo de prueba: proyecto/README.txt

Idea clave: Fichero .txt proyecto/; verifica tiene .txt y .py.

??? example "Ver archivo de apoyo"
    ```text
    Proyecto de ejemplo
    ```

### Archivo de prueba: shared/Archivo con espacios.txt

Idea clave: Nombre espacios; detectado ' ' in p.name.

??? example "Ver archivo de apoyo"
    ```text
    hola
    ```

### Archivo de prueba: shared/otro archivo.log

Idea clave: Otro archivo espacios; mismo patrón detección.

??? example "Ver archivo de apoyo"
    ```text
    log
    ```

### Archivo de prueba: shared/sin_espacios.txt

Idea clave: Sin espacios; NO coincide búsqueda nombres espacios.

??? example "Ver archivo de apoyo"
    ```text
    ok
    ```

### Archivo de prueba: temp/cache.tmp

Idea clave: Fichero .tmp capturado glob('*.tmp').

??? example "Ver archivo de apoyo"
    ```text
    temp data
    ```

### Archivo de prueba: temp/config.bak

Idea clave: Fichero .bak capturado glob('*.bak').

??? example "Ver archivo de apoyo"
    ```text
    backup config
    ```

### Archivo de prueba: temp/keep.me

Idea clave: NO .tmp/.bak; aparece NO en cleanup_plan.txt.

??? example "Ver archivo de apoyo"
    ```text
    no borrar
    ```

### Archivo de prueba: temp/session.tmp

Idea clave: Otro .tmp; junto cache.tmp en glob.

??? example "Ver archivo de apoyo"
    ```text
    temp session
    ```
