# Soluciones

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu programa sigue la misma secuencia de pasos.
    - Fíjate en qué datos se leen, cuándo se convierten y dónde se calcula el resultado.
    - Si tu versión no coincide, revisa la idea del ejercicio antes de reescribir todo el programa.

En estos ejercicios conviene prestar atención a la estructura de datos elegida y a cómo se recorre para construir el resultado.

### Ejercicio 01

Idea clave: Observa cómo sorted() ordena valores sin preservar las claves que los contextualizan.

??? example "Ver solución"
    ```python
    # Ejercicio 1
    ''' Muestra información del sistema operativo (sistema, versión, nodo y procesador) y almacena los datos en un diccionario. Crea una lista con los valores y muéstralos ordenados alfabéticamente.'''
    
    import platform
    
    sistema = {
        'Sistema': platform.system(),
        'Versión': platform.version(),
        'Nombre del nodo': platform.node(),
        'Procesador': platform.processor()
    }
    
    valores = sorted(sistema.values())
    
    print("Valores del sistema ordenados:")
    for valor in valores:
        print(valor)
    ```

### Ejercicio 02

Idea clave: Usa .items() para recorrer claves y valores del diccionario simultáneamente.

??? example "Ver solución"
    ```python
    # Ejercicio 2: 
    '''Solicita por teclado 3 nombres de usuario mediante un bucle y almacénalos en una lista. A continuación, almacena sus home directory en un diccionario usando `os.path.expanduser`. Muestra el contenido del diccionario formateado.'''
    import os
    
    usuarios = []
    for i in range(3):
        nombre = input(f"Nombre del usuario {i+1}: ")
        usuarios.append(nombre)
    
    homes = {}
    for usuario in usuarios:
        homes[usuario] = os.path.expanduser(f'~{usuario}')
    
    print("Directorios home de usuarios:")
    for usuario, ruta in homes.items():
        print(f"{usuario}: {ruta}")
    ```

### Ejercicio 03

Idea clave: Los métodos .is_file() y .is_dir() de Path determinan tipo sin excepciones.

??? example "Ver solución"
    ```python
    # Ejercicio 3: 
    '''Pide al usuario 4 nombres de archivo o directorio. Usa la librería `pathlib` para determinar si existen y su tipo (fichero o directorio) y almacena esa información en un diccionario. Es decir, el diccionario debe contener para cada ruta si es archivo, directorio o si no existe.'''
    
    from pathlib import Path
    info = {}
    for i in range(4):
        ruta = Path(input(f"Introduce la ruta {i+1}: "))
        if ruta.is_file():
            info[ruta] = 'Archivo'
        elif ruta.is_dir():
            info[ruta] = 'Directorio'
        else:
            info[ruta] = 'No existe'
    
    for ruta, tipo in info.items():
        print(f"{ruta}: {tipo}")
    ```

### Ejercicio 04

Idea clave: .iterdir() genera elementos; filtra con .is_file()/.is_dir() antes de guardar.

??? example "Ver solución"
    ```python
    # Ejercicio 4: 
    '''Ejercicio 4: Usa `pathlib` para listar los archivos y carpetas del directorio actual y guarda esa información (si son archivo o directorio) en un diccionario, tal y como se ha hecho en el ejercicio anterior.'''
    
    from pathlib import Path
    
    ruta = Path('.')
    elementos = list(ruta.iterdir())
    
    info = {}
    for e in elementos:
        if e.is_file():
            info[e.name] = 'Archivo'
        elif e.is_dir():
            info[e.name] = 'Directorio'
    
    for nombre, tipo in info.items():
        print(f"{nombre}: {tipo}")
    ```

### Ejercicio 05

Idea clave: Verifica .exists() antes de .mkdir(); registra si se creó o ya existía.

??? example "Ver solución"
    ```python
    # Ejercicio 5: 
    '''Crea 3 nombres de carpeta que se situarán en el directorio actual en una lista y convierte a tipo `Path`. A continuación, para cada carpeta, si no existe, la creas y guarda en un diccionario si las carpetas fueron creadas o ya existían. Muestra el contenido del diccionario recorriendo sus elementos.'''
    from pathlib import Path
    carpetas = [Path('./logs'), Path('./data'), Path('./temp')]
    estado = {}
    
    for carpeta in carpetas:
        if not carpeta.exists():
            carpeta.mkdir()
            estado[carpeta] = 'Creada'
        else:
            estado[carpeta] = 'Ya existía'
    
    for carpeta, e in estado.items():
        print(f"{carpeta}: {e}")
    ```

### Ejercicio 06

Idea clave: shutil.disk_usage() devuelve tupla; conviértela a GB dentro de diccionarios.

??? example "Ver solución"
    ```python
    # Ejercicio 6: 
    '''Usa `shutil.disk_usage` para mostrar en un diccionario el espacio total, usado y libre en GB (redondeando a un decimal) de tres rutas del sistema que pedirás por teclado. Muestra el contenido del diccionario recorriendo sus elementos.'''
    import shutil
    import os
    rutas = []
    for _ in range(3):
        #una ruta puede ser '/', '/tmp', '/home', etc
        rutas.append(input("Introduce ruta: "))
        
    uso_disco = {}
    
    for ruta in rutas:
        if not os.path.exists(ruta):
            total, usado, libre = 0,0,0
        else:
            total, usado, libre = shutil.disk_usage(ruta)
        uso_disco[ruta] = {'total': round(total/1024**3,1), 'usado': round(usado/1024**3,1), 'libre': round(libre/1024**3,1)}
    
    for ruta, datos in uso_disco.items():
        print(f"{ruta} -> Total: {datos['total']} GB, Usado: {datos['usado']} GB, Libre: {datos['libre']} GB")
    ```

### Ejercicio 07

Idea clave: Combina list(usuario.iterdir()) con len() para contar archivos por usuario.

??? example "Ver solución"
    ```python
    # Ejercicio 7: 
    '''Usa la librería `pathlib` para listar los usuarios en `/home`. Crea un diccionario con su nombre y cuántos archivos tienen en su carpeta de usuario. Muestra el contenido del diccionario recorriendo sus elementos.'''
    from pathlib import Path
    
    ##Se puede usar directorio alternativo dentro del propio home porque no os va a dejar acceder a los home de otros usuarios
    usuarios = Path('/home').iterdir()
    conteo_archivos = {}
    
    for usuario in usuarios:
        if usuario.is_dir():
            archivos = list(usuario.iterdir())
            conteo_archivos[usuario] = len(archivos)
        
    
    for usuario, cantidad in conteo_archivos.items():
        print(f"{usuario}: {cantidad} archivos")
    ```

### Ejercicio 08

Idea clave: if-elif-else con .exists(), .is_file(), .is_dir() clasifica rutas.

??? example "Ver solución"
    ```python
    # Ejercicio 8
    
    '''
    Vamos a realizar un análisis de las siguientes rutas críticas del sistema:
    rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
    Guarda en un diccionario si cada una existe y si es un archivo, un directorio 
    o no existe. Muestra un informe con el sistema operativo, número de CPUs, 
    fecha actual y el estado de cada ruta. Usa las librerías `pathlib`, `platform`, 
    `os` y `datetime`.'''
    
    from pathlib import Path
    import platform
    import os
    from datetime import datetime
    
    rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
    
    estado_rutas = {}
    
    for ruta_str in rutas:
        ruta = Path(ruta_str)
        if ruta.exists():
            if ruta.is_dir():
                estado_rutas[ruta_str] = "Directorio"
            elif ruta.is_file():
                estado_rutas[ruta_str] = "Archivo"
            else:
                estado_rutas[ruta_str] = "Otro tipo"
        else:
            estado_rutas[ruta_str] = "No existe"
    
    print(f"Análisis del sistema ({platform.system()}, CPUs: {os.cpu_count()})")
    print(f"Fecha del informe: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Estado rutas: ")
    for ruta, estado in estado_rutas.items():
        print(f"{ruta}: {estado}")
    ```

### Ejercicio 09

Idea clave: split(':') divide PATH; insert(0) añade inicio; ':'.join() reconstruye.

??? example "Ver solución"
    ```python
    # Ejercicio 9
    '''
    Simula la gestión de la variable de entorno PATH, que contiene varias rutas separadas por : (dos puntos).
    A partir de un string que representa un PATH, conviértelo en una lista, añade una nueva ruta al final (pídela por teclado), otra al inicio (pídela por teclado), y luego vuelve a unirlo en un solo string. Muestra el resultado final.
    '''
    ruta_path = "/usr/local/bin:/usr/bin:/bin"
    
    rutas = ruta_path.split(":")
    
    #"/opt/scripts"
    #"/custom/bin"
    rutas.append(input("Ruta para añadir al final: "))
    rutas.insert(0, input("Ruta para añadir al inicio: "))
    
    
    nuevo_path = ":".join(rutas)
    
    
    print("Rutas individuales:")
    for ruta in rutas:
        print("-", ruta)
    print("\nNuevo PATH resultante:")
    print(nuevo_path)
    ```

### Ejercicio 10

Idea clave: ' '.join(lista) concatena con espacios; construcción clara de comandos shell.

??? example "Ver solución"
    ```python
    # Ejercicio 10: 
    
    
    paquetes = ["vim", "curl", "htop"]
    
    nuevo = input("Introduce otro paquete que quieras instalar: ")
    paquetes.append(nuevo)
    
    comando = "apt install " + " ".join(paquetes)
    
    print("\nComando generado:")
    print(comando)
    ```
