# Librerías útiles para administradores de sistemas en Python 

## Qué vas a aprender

A partir de esta unidad no queremos usar Python solo para ejercicios matemáticos. Queremos empezar a escribir pequeños scripts útiles para administración de sistemas.

Python incluye una **librería estándar** muy amplia. Eso significa que muchas herramientas ya vienen instaladas con Python y podemos usarlas con `import`.

## Importar una librería

```python
import platform

print(platform.system())
```

También podemos importar algo concreto:

```python
from pathlib import Path

ruta = Path(".")
print(ruta.exists())
```

 A continuación se explican las librerías más importantes y se incluyen ejemplos prácticos. 
 Recuerda ir a cada uno de los enlaces de las librerías correspondientes y explorarlas para entender su funcionamiento. 


## [`sys`: información del intérprete y argumentos](https://docs.python.org/es/3.13/library/sys.html) 

Permite acceder a variables y funciones del intérprete de Python. Útil para obtener información del sistema o finalizar la ejecución del programa. 

Funciones importantes: 

`sys.version` — versión de Python 

`sys.platform` — tipo de sistema operativo 

`sys.exit()` — termina el programa 

`sys.argv` — devuelve la lista de argumentos con los que se ejecuta un programa. `sys.argv[0]` es el nombre del script, `sys.argv[1]` es el primer argumento, etc. 

 

### Ejemplo 1: Comprobar sistema operativo

```python
import sys 
 
print("Versión de Python:", sys.version) 
print("Sistema operativo:", sys.platform) 
 
# Finalizar el programa si no es Windows 
if sys.platform != "win32": 
    print("Este script solo funciona en Windows.") 
    sys.exit() 
``` 

### Ejemplo 2: Comprobar argumentos al ejecutar el programa

```python
#archivo edad.py
import sys 

if len(sys.argv) >= 2: 
    argumento = int(sys.argv[1]) 

else: 
    print('No has introducido la edad') 
``` 

Ejecución:

```bash
python edad.py 22
```
 
### Ejemplo 3: Comprobar argumentos al ejecutar el programa

```python
# archivo saluda.py
import sys

if len(sys.argv) < 2:
    print("Uso: python saluda.py nombre")
else:
    print(f"Hola, {sys.argv[1]}")
```

Ejecución:

```bash
python saluda.py Ana
```

## [`os`: sistema operativo y variables de entorno](https://docs.python.org/es/3.13/library/os.html) 

Permite interactuar con el sistema operativo: rutas, directorios, variables de entorno, etc. A la hora de trabajar con rutas y directorios, utlizaremos mejor la librería pathlib, que es más moderna. 

Funciones importantes:

`os.getcwd()` — devuelve el directorio actual — `Path.cwd()`

`os.listdir()` — lista el contenido del directorio 

`os.getenv('PATH')` — obtiene variables de entorno 

`os.mkdir('carpeta')` — crea un directorio — `Path.mkdir()` 

### Ejemplo 1: Listar directorio y crear carpeta

```python
import os 
 
print("Directorio actual:", os.getcwd()) 
print("Contenido:", os.listdir(".")) 
 
# Crear carpeta si no existe 
if "carpeta" not in os.listdir("."): 
    os.mkdir("carpeta") 
    print("Carpeta 'carpeta' creada.") 
```

## [`datetime`: fechas y horas](https://docs.python.org/es/3.13/library/datetime.html)

Permite trabajar con fechas y horas, ideal para planificar tareas o generar nombres de archivos con fecha. 

Funciones importantes:

`datetime.now()` — obtiene fecha y hora actuales 

`date.today()` — devuelve solo la fecha actual 

`timedelta(days=1)` — permite restar o sumar días 

Revisar los atributos que tiene la clase datetime 

Revisar la función `strftime` para formatear fechas 

### Ejemplo 1: Fecha actual y calcular fechas

```python
from datetime import datetime, timedelta 
 
hoy = datetime.now() 
print("Fecha y hora actuales:", hoy) 
 
ayer = hoy - timedelta(days=1) 
print("Ayer fue:", ayer.strftime("%Y-%m-%d")) 
 
# Crear nombre de backup con fecha 
nombre_backup = f"backup_{hoy.strftime('%Y_%m_%d')}.zip" 
print("Nombre de backup:", nombre_backup) 
```

### Ejemplo 2: Extraer hora de la fecha

```python
from datetime import datetime

hora = datetime.now().hour

if hora < 14:
    print("Buenos días")
else:
    print("Buenas tardes")
```

### Ejemplo 3: Extraer el día de la semana 

```python
from datetime import datetime

dia = datetime.now().weekday()
print(dia)
```

`weekday()` devuelve `0` para lunes y `6` para domingo.


### Ejemplo 4: Generar nombres de backup calculando la fecha

```python
from datetime import datetime, timedelta

hoy = datetime.now()

#Generar nombres de backup para varios días
for desplazamiento in range(7):
    fecha = hoy + timedelta(days=desplazamiento)
    print(f"backup_{fecha:%Y_%m_%d}.zip")
```


## [`platform`: información del sistema](https://docs.python.org/es/3/library/platform.html)

Proporciona información sobre el sistema operativo y el hardware. 

Funciones importantes:

`platform.system()` — devuelve el nombre del SO 

`platform.release()` — versión del SO 

`platform.processor()` — tipo de procesador 

### Ejemplo 1: Ejecutar acciones en base al S.O.

```python
import platform 
 
print("Sistema operativo:", platform.system()) 
print("Versión:", platform.release()) 
print("Procesador:", platform.processor()) 
 
if platform.system() == "Windows": 
    print("Configurando entorno para Windows...") 
```

## [`pathlib`: rutas de forma moderna](https://docs.python.org/es/3.13/library/pathlib.html#module-pathlib) 

Ofrece una forma moderna de trabajar con rutas de archivos y directorios. Normalmente utlizaremos la clase `Path`

Funciones y propiedades importantes:

`Path.cwd()` — devuelve el directorio actual 

`Path.iterdir()` — itera sobre los elementos de un directorio (lo veremos más adelante) 

`Path.exists()` — comprueba si un archivo o carpeta existe 

`Path.is_dir()` — comprueba si es carpeta 

`Path.is_file()` — comprueba si es un archivo  

`Path.mkdir()` — crea carpeta 

`Path.rmdir()` — elimina carpeta 

`Path.rename()` — renombra carpeta 

`Path.stat()` — devuelve objeto con información sobre la ruta (id de usuario, id de grupo, tamaño, etc) 

`Path.suffix` — la última parte de la ruta que queda separada por un punto. Por ejemplo, si la ruta es: `“/my/library/setup.py”`, devolverá `“.py”`

`Path.parent` — el padre lógico de la ruta. Por ejemplo, si la ruta es `“/a/b/c”`, devolverá `“/a/b”` 

### Ejemplo 1: Montar rutas y crear carpetas

```python
from pathlib import Path 
 
ruta = Path.cwd() 
print("Ruta actual:", ruta) 
 
# Crear carpeta ejercicios si no existe 
carpeta_ejer = ruta / "ejercicios" 
if not carpeta_ejer.exists(): 
    carpeta_ejer.mkdir() 
    print("Carpeta 'ejercicios' creada.") 
else:
    print("Carpeta ya existe")
```

### Ejemplo 2: Crear varias carpetas anidadas

Si quieres crear varias carpetas anidadas de una vez, puedes usar `parents=True`:

```python
from pathlib import Path

ruta = Path("backups") / "2025" / "02" / "dia_01"
ruta.mkdir(parents=True, exist_ok=True)
print(ruta)
```

- `parents=True` crea también las carpetas intermedias que falten.
- `exist_ok=True` evita error si la carpeta ya existía.


### Ejemplo 3: Consultar tamaño y fechas de un archivo con `stat()`

```python
from pathlib import Path

archivo = Path("informe.log")

if archivo.exists():
    datos = archivo.stat()
    print(datos.st_size)
    print(datos.st_mtime)
```

### Ejemplo 4: Listar elementos de una carpeta:

```python
from pathlib import Path

for elemento in Path(".").iterdir():
    print(elemento.name)
```

### Ejemplo 5: Comprobar extensiones:

```python
for archivo in Path(".").iterdir():
    if archivo.is_file() and archivo.suffix == ".py":
        print(archivo.name)
```


## [`shutil`: operaciones de alto nivel con archivos](https://docs.python.org/es/3.13/library/shutil.html) 

Permite copiar, mover o eliminar archivos y carpetas fácilmente. 

Funciones importantes:

`shutil.copy('origen', 'destino')` — copia un archivo 

`shutil.move('origen', 'destino')` — mueve un archivo 

`shutil.rmtree('carpeta')` — elimina una carpeta 

`shutil.disk_usage('carpeta')` —retorna las estadísticas de uso de disco sobre la ruta de acceso dada como un named tuple con los atributos `total`, `used` y `free`, que son las cantidades del espacio total, el usado y el libre, en bytes. 'carpeta' puede ser un archivo o un directorio. 

### Ejemplo 1: Copiar fichero

```python
import shutil 
from pathlib import Path 
 
origen = Path("backup.zip") 
destino = Path("copias/backup.zip") 
 
# Crear carpeta destino si no existe 
destino.parent.mkdir(exist_ok=True) 
 
if origen.exists(): 
    shutil.copy(origen, destino) 
    print("Backup copiado a carpeta 'copias'.") 
```

### Ejemplo 2: Calcular porcentaje de espacio usado en disco

```python
import shutil

total, usado, libre = shutil.disk_usage("/")
porcentaje = usado / total * 100

print(f"Uso: {porcentaje:.2f}%")
```

## Otras librerías y herramientas útiles

### `random` y `time`

En algunos ejercicios también nos viene bien generar valores aleatorios o pausar un programa.

```python
import random
import time

numero = random.randint(1, 100)
simbolo = random.choice("!#$%&*")

print(numero)
print(simbolo)
time.sleep(1)
```

- `random.randint(a, b)` genera un entero aleatorio entre `a` y `b`.
- `random.choice(secuencia)` elige un elemento al azar.
- `time.sleep(segundos)` pausa el programa durante el tiempo indicado.

### `zfill()` para numerar nombres

Cuando queremos nombres como `PC-01`, `PC-02` o `AULA-03`, resulta útil completar con ceros a la izquierda:

```python
for numero in range(1, 4):
    print(str(numero).zfill(2))
```

Salida:

```text
01
02
03
```

### `glob` y patrones de archivos

Más adelante en la unidad sobre archivos profundizaremos en `pathlib.glob()` y `pathlib.rglob()`. De momento, observa este ejemplo:

```python
from pathlib import Path

for archivo in Path(".").glob("*.py"):
    print(archivo.name)
```

Busca archivos `.py` en la carpeta actual.

Con `rglob()` busca de forma recursiva:

```python
for archivo in Path(".").rglob("*.log"):
    print(archivo)
```

## Ejemplo integrador

```python
from pathlib import Path
from datetime import datetime
import platform

print(f"Sistema: {platform.system()}")
print(f"Fecha: {datetime.now():%Y-%m-%d}")

carpeta = Path(".")
contador_py = 0

for archivo in carpeta.iterdir():
    if archivo.is_file() and archivo.suffix == ".py":
        contador_py += 1

print(f"Archivos Python encontrados: {contador_py}")
```

Aquí aparecen ideas de la unidad:

- variables;
- condicionales;
- bucles;
- librerías;
- rutas;
- f-strings.

## Qué debes memorizar y qué no

No tienes que memorizar todas las funciones de estas librerías. Lo importante es:

- saber que existen;
- saber importarlas;
- saber usarlas;
- reconocer ejemplos;
- consultar documentación;
- adaptar código sencillo;
- entender qué hace tu script.

