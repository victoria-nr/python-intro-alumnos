# Módulos y paquetes

## Qué vas a aprender

Un módulo es un archivo de Python que contiene código reutilizable. Usar módulos permite organizar mejor los programas.

## Qué es un módulo

Si tienes un archivo llamado `utilidades.py`, ese archivo puede ser un módulo.

```python
# utilidades.py
def saludar(nombre):
    return f"Hola, {nombre}"
```

Desde otro archivo:

```python
import utilidades

print(utilidades.saludar("Ana"))
```

## Importar un módulo completo

```python
import math

print(math.sqrt(25))
```

Esta forma mantiene claro de dónde viene cada función.

## Importar elementos concretos

```python
from math import sqrt

print(sqrt(25))
```

También puedes importar un nombre concreto con alias:

```python
from math import sqrt as raiz

print(raiz(9))
```

Existe otra posibilidad:

```python
from math import *
```

Esto importa todos los nombres públicos del módulo, pero normalmente no se recomienda porque hace más difícil saber de dónde viene cada función.

## Alias con `as`

`as` permite usar un alias:

```python
import pathlib as pl

ruta = pl.Path(".")
```

También se usa mucho en librerías externas:

```python
import pandas as pd
```

## Ventajas de los módulos

- Evitan archivos enormes.
- Permiten reutilizar código.
- Facilitan las pruebas.
- Separan responsabilidades.
- Ayudan a mantener proyectos ordenados.

## `sys.path`

Cuando Python importa un módulo, lo busca en una serie de rutas almacenadas en `sys.path`.

```python
import sys
print(sys.path)
```

Si dos módulos tienen el mismo nombre en distintas rutas, Python usará el primero que encuentre según el orden de `sys.path`. Por eso no conviene llamar a tus archivos igual que módulos estándar, por ejemplo `math.py` o `random.py`.

Puedes añadir una ruta temporalmente así:

```python
import sys

sys.path.append("/mi/ruta")
```

Si quieres dar prioridad a una ruta concreta, puedes ponerla al principio:

```python
sys.path.insert(0, "/mi/ruta")
```

Otra forma de modificar las rutas de búsqueda es la variable de entorno `PYTHONPATH`.

## `sys.argv`

`sys.argv` guarda los argumentos con los que se ha ejecutado el programa:

```python
import sys

print(sys.argv)
```

Si ejecutas:

```bash
python programa.py datos.txt
```

`sys.argv` valdrá aproximadamente esto:

```python
["programa.py", "datos.txt"]
```

Es muy útil cuando un script recibe el nombre de un fichero por línea de comandos.

## Paquetes

Un paquete es una carpeta que agrupa módulos.

```text
mi_paquete/
├── __init__.py
├── usuarios.py
└── ficheros.py
```

En proyectos modernos `__init__.py` no siempre es obligatorio, pero sigue siendo habitual verlo.

Desde otro archivo podrías importar un módulo del paquete así:

```python
from herramientas import validaciones

print(validaciones.es_puerto_valido(22))
```

## Qué pasa al importar

Cuando importas un módulo, Python ejecuta su código una vez y deja sus nombres disponibles para usarlos.

Por eso conviene que el código principal de prueba o de ejecución no quede suelto en el archivo, sino protegido con el bloque `if __name__ == "__main__":`.

## `__name__` y ejecución directa

Este patrón permite distinguir si un archivo se ejecuta directamente o se importa desde otro:

```python
def main():
    print("Programa principal")

if __name__ == "__main__":
    main()
```

Cuando ejecutas el archivo directamente, `__name__` vale `"__main__"`.

En muchos proyectos el archivo de entrada se llama `main.py`. Suele contener los imports al principio, las funciones auxiliares después y el bloque `if __name__ == "__main__":` al final.

## Algunos módulos útiles de la biblioteca estándar

```python
import os
import platform
from datetime import datetime

print(platform.system())
print(os.cpu_count())
print(datetime.now())
```

Este tipo de módulos resulta útil en scripts de automatización, informes y pequeñas tareas de administración.

## Ejemplo aplicado

```python
# validaciones.py
def es_puerto_valido(puerto):
    return 1 <= puerto <= 65535
```

```python
# programa.py
from validaciones import es_puerto_valido

puerto = int(input("Puerto: "))

if es_puerto_valido(puerto):
    print("Puerto válido")
else:
    print("Puerto no válido")
```

## Antes del cuestionario comprueba que sabes...

- Explicar qué es un módulo.
- Usar `import modulo`.
- Usar `from modulo import elemento`.
- Usar alias con `as`.
- Saber qué es `sys.path`.
- Saber para qué sirve `sys.argv`.
- Reconocer cómo se añade una ruta con `sys.path.append(...)`.
- Entender que `PYTHONPATH` también influye en la búsqueda.
- Entender qué es un paquete.
- Reconocer el patrón `if __name__ == "__main__"`.
