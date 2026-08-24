# `pathlib`, rutas y búsqueda de archivos con `glob`

## Qué vas a aprender

En administración de sistemas es habitual trabajar con rutas, carpetas y ficheros. Python permite hacerlo de varias formas, pero en código moderno se recomienda usar `pathlib`.

## Crear rutas con `Path`

```python
from pathlib import Path

ruta = Path("datos")
print(ruta)
```

Una ruta no tiene por qué existir. `Path("datos")` solo representa la ruta.

## Comprobar rutas

```python
from pathlib import Path

ruta = Path("datos")

print(ruta.exists())
print(ruta.is_file())
print(ruta.is_dir())
```

## Combinar rutas

```python
from pathlib import Path

carpeta = Path("datos")
fichero = carpeta / "alumnos.txt"

print(fichero)
```

El operador `/` permite construir rutas de forma cómoda y multiplataforma.

## Propiedades útiles

```python
ruta = Path("datos/alumnos.txt")

print(ruta.name)    # alumnos.txt
print(ruta.stem)    # alumnos
print(ruta.suffix)  # .txt
print(ruta.parent)  # datos
```

También puedes consultar información del fichero con `stat()`:

```python
ruta = Path("datos/alumnos.txt")

print(ruta.stat().st_size)
```

`st_size` indica el tamaño en bytes.

## Leer y escribir texto con `pathlib`

```python
from pathlib import Path

ruta = Path("saludo.txt")
ruta.write_text("Hola\n", encoding="utf-8")

contenido = ruta.read_text(encoding="utf-8")
print(contenido)
```

Para ejercicios sencillos es cómodo. Para ficheros grandes, sigue siendo mejor recorrer línea a línea con `open()`.

## Crear carpetas

```python
from pathlib import Path

carpeta = Path("salidas")
carpeta.mkdir(exist_ok=True)
```

Con `parents=True` puede crear carpetas intermedias:

```python
Path("datos/2026/julio").mkdir(parents=True, exist_ok=True)
```

## Recorrer una carpeta

```python
from pathlib import Path

for elemento in Path(".").iterdir():
    print(elemento.name)
```

Filtrar ficheros:

```python
for elemento in Path(".").iterdir():
    if elemento.is_file():
        print(elemento.name)
```

## Buscar con `glob()`

`glob()` busca elementos que cumplen un patrón en una carpeta.

```python
from pathlib import Path

for archivo in Path(".").glob("*.py"):
    print(archivo.name)
```

Busca archivos `.py` en la carpeta actual.

Otros patrones:

```python
Path(".").glob("*.txt")
Path(".").glob("datos_*.csv")
Path(".").glob("*.log")
```

## Búsqueda recursiva con `rglob()`

`rglob()` busca también dentro de subcarpetas:

```python
from pathlib import Path

for archivo in Path(".").rglob("*.py"):
    print(archivo)
```

Esto es muy útil para analizar proyectos o carpetas grandes.

Si necesitas guardar una ruta relativa respecto a una carpeta base, puedes usar `relative_to()`:

```python
base = Path("configs")

for archivo in base.rglob("*.conf"):
    print(archivo.relative_to(base))
```

## Copiar ficheros

Para copiar ficheros de una carpeta a otra puedes apoyarte en `shutil`:

```python
from pathlib import Path
from shutil import copy2

origen = Path("configs/app.conf")
destino = Path("backup_configs")
destino.mkdir(exist_ok=True)

copy2(origen, destino / origen.name)
```

`copy2()` copia el fichero y conserva metadatos básicos.

## Ejemplo: contar archivos por extensión

```python
from pathlib import Path

conteo = {}

for archivo in Path(".").rglob("*"):
    if archivo.is_file():
        extension = archivo.suffix.lower()
        conteo[extension] = conteo.get(extension, 0) + 1

for extension, cantidad in conteo.items():
    print(f"{extension}: {cantidad}")
```

Este ejemplo combina:

- rutas;
- bucles;
- condicionales;
- diccionarios;
- métodos de cadenas;
- f-strings.

## Ejemplo: buscar logs con errores

```python
from pathlib import Path

for archivo in Path("logs").rglob("*.log"):
    with open(archivo, "r", encoding="utf-8") as fichero:
        for numero_linea, linea in enumerate(fichero, 1):
            if "ERROR" in linea:
                print(f"{archivo}:{numero_linea}: {linea.strip()}")
```

Este tipo de script se parece mucho a tareas reales de administración de sistemas.

## Antes de seguir comprueba que sabes...

- Crear rutas con `Path`.
- Usar `exists()`, `is_file()` e `is_dir()`.
- Combinar rutas con `/`.
- Obtener `name`, `stem`, `suffix` y `parent`.
- Consultar el tamaño de un fichero con `stat().st_size`.
- Usar `read_text()` y `write_text()` en casos sencillos.
- Recorrer carpetas con `iterdir()`.
- Buscar archivos con `glob()` y `rglob()`.
- Obtener rutas relativas con `relative_to()`.
