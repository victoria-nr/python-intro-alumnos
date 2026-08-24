# Librerías útiles para administradores de sistemas

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

## `platform`: información del sistema

```python
import platform

print(platform.system())
print(platform.release())
print(platform.machine())
print(platform.python_version())
```

Ejemplo de uso:

```python
sistema = platform.system()

if sistema == "Windows":
    print("Estás usando Windows")
elif sistema == "Linux":
    print("Estás usando Linux")
elif sistema == "Darwin":
    print("Estás usando macOS")
else:
    print("Sistema no reconocido")
```

## `sys`: información del intérprete y argumentos

```python
import sys

print(sys.version)
print(sys.platform)
print(sys.argv)
```

`sys.argv` contiene los argumentos con los que se ejecuta un programa:

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

## `os`: sistema operativo y variables de entorno

```python
import os

print(os.getcwd())
print(os.name)
print(os.environ.get("USER"))
```

`os` permite interactuar con el sistema operativo. En código moderno, para rutas y ficheros usaremos preferiblemente `pathlib`, pero `os` sigue apareciendo en muchos scripts.

Por ejemplo, para listar el contenido de la carpeta actual:

```python
import os

for nombre in os.listdir("."):
    print(nombre)
```

## `pathlib`: rutas de forma moderna

```python
from pathlib import Path

ruta = Path(".")
print(ruta.resolve())
print(ruta.exists())
print(ruta.is_dir())
```

Listar elementos de una carpeta:

```python
from pathlib import Path

for elemento in Path(".").iterdir():
    print(elemento.name)
```

Comprobar extensiones:

```python
for archivo in Path(".").iterdir():
    if archivo.is_file() and archivo.suffix == ".py":
        print(archivo.name)
```

Montar rutas y crear carpetas:

```python
from pathlib import Path

logs = Path(".") / "logs"

if not logs.exists():
    logs.mkdir()
    print("Carpeta creada")
else:
    print("Carpeta ya existe")
```

Si quieres crear varias carpetas anidadas de una vez, puedes usar `parents=True`:

```python
from pathlib import Path

ruta = Path("backups") / "2025" / "02" / "dia_01"
ruta.mkdir(parents=True, exist_ok=True)
print(ruta)
```

- `parents=True` crea también las carpetas intermedias que falten.
- `exist_ok=True` evita error si la carpeta ya existía.

Consultar tamaño y fechas de un archivo con `stat()`:

```python
from pathlib import Path

archivo = Path("informe.log")

if archivo.exists():
    datos = archivo.stat()
    print(datos.st_size)
    print(datos.st_mtime)
```

## `shutil`: operaciones de alto nivel con archivos

```python
import shutil

shutil.copy("origen.txt", "copia.txt")
```

También permite copiar árboles de carpetas, mover archivos o eliminar directorios completos. Hay que usarlo con cuidado porque puede modificar muchos archivos.

Otra función muy útil es `disk_usage()`, que permite consultar el espacio de un disco:

```python
import shutil

total, usado, libre = shutil.disk_usage("/")
porcentaje = usado / total * 100

print(f"Uso: {porcentaje:.2f}%")
```

## `datetime`: fechas y horas

```python
from datetime import datetime, timedelta

ahora = datetime.now()
print(ahora)
print(ahora.strftime("%Y-%m-%d %H:%M"))

manana = ahora + timedelta(days=1)
print(manana)
```

Ejemplo aplicado:

```python
from datetime import datetime

hora = datetime.now().hour

if hora < 14:
    print("Buenos días")
else:
    print("Buenas tardes")
```

Obtener el día de la semana:

```python
from datetime import datetime

dia = datetime.now().weekday()
print(dia)
```

`weekday()` devuelve `0` para lunes y `6` para domingo.

Generar nombres de backup para varios días:

```python
from datetime import datetime, timedelta

hoy = datetime.now()

for desplazamiento in range(7):
    fecha = hoy + timedelta(days=desplazamiento)
    print(f"backup_{fecha:%Y_%m_%d}.zip")
```

## `random` y `time`

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

## `zfill()` para numerar nombres

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

## `glob` y patrones de archivos

Más adelante profundizaremos en `pathlib.glob()` y `pathlib.rglob()`. De momento, observa este ejemplo:

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
- reconocer ejemplos;
- consultar documentación;
- adaptar código sencillo;
- entender qué hace tu script.

## Antes de seguir comprueba que sabes...

- Importar una librería con `import`.
- Usar `platform.system()`.
- Consultar argumentos con `sys.argv`.
- Crear rutas con `Path`.
- Recorrer archivos con `iterdir()`.
- Crear carpetas con `mkdir()`.
- Crear estructuras anidadas con `mkdir(parents=True, exist_ok=True)`.
- Obtener información básica de un archivo con `stat()`.
- Filtrar por extensión con `suffix`.
- Consultar el uso de disco con `shutil.disk_usage()`.
- Usar fechas básicas con `datetime`.
- Obtener el día de la semana y sumar días con `timedelta`.
- Usar `random`, `time.sleep()` y `zfill()` en ejemplos sencillos.
