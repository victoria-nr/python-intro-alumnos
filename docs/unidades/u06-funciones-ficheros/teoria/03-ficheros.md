# Ficheros: lectura y escritura

## Qué vas a aprender

Un fichero es un conjunto de bytes almacenados en un dispositivo. En programación usamos ficheros para guardar y recuperar información: configuraciones, logs, datos, informes, resultados, etc.

El **sistema de ficheros** organiza esos ficheros en carpetas y rutas.

En esta unidad trabajaremos principalmente con **ficheros de texto**.

## Abrir ficheros con `open()`

```python
fichero = open("datos.txt", "r", encoding="utf-8")
contenido = fichero.read()
fichero.close()
print(contenido)
```

Es mejor usar `with`, porque cierra el fichero automáticamente:

```python
with open("datos.txt", "r", encoding="utf-8") as fichero:
    contenido = fichero.read()

print(contenido)
```

La variable `fichero` es un manejador: un objeto que representa el fichero abierto y permite leerlo o escribirlo.

## Modos de apertura

| Modo | Intención |
|---|---|
| `r` | leer |
| `w` | escribir desde cero, borrando lo anterior |
| `a` | añadir al final |
| `x` | crear, fallando si ya existe |

También existen modos binarios como `rb` o `wb`, pero aquí nos centraremos en texto.

## Fichero inexistente

Si intentas abrir en modo lectura un fichero que no existe, Python lanza `FileNotFoundError`.

```python
with open("no_existe.txt", "r", encoding="utf-8") as fichero:
    print(fichero.read())
```

## `read()`, `readlines()` y recorrido línea a línea

`read()` lee todo el contenido como una cadena:

```python
with open("datos.txt", "r", encoding="utf-8") as fichero:
    contenido = fichero.read()
```

`readlines()` devuelve una lista de líneas:

```python
with open("datos.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
```

`readline()` lee solo una línea cada vez:

```python
with open("datos.txt", "r", encoding="utf-8") as fichero:
    primera = fichero.readline()
    segunda = fichero.readline()
```

Cada vez que llamas a `readline()`, el puntero de lectura avanza. Cuando llega al final del fichero, devuelve una cadena vacía.

Si quieres volver al principio para releerlo, puedes usar `seek(0)`:

```python
with open("datos.txt", "r", encoding="utf-8") as fichero:
    primera = fichero.readline()
    fichero.seek(0)
    otra_vez = fichero.readline()
```

Cuando lees líneas, normalmente aparecen saltos de línea representados por `\n`.

Para ficheros grandes, conviene recorrer línea a línea sin cargar todo en memoria:

```python
with open("datos.txt", "r", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea.strip())
```

Esta técnica es recomendable si el fichero puede ocupar muchos MB o varios GB.

Los manejadores de ficheros son iterables, por eso se pueden recorrer con `for`. Si además quieres numerar las líneas, usa `enumerate()`:

```python
with open("log.txt", "r", encoding="utf-8") as fichero:
    for numero_linea, linea in enumerate(fichero, 1):
        print(numero_linea, linea.strip())
```

## Escribir ficheros

```python
with open("salida.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Primera línea\n")
    fichero.write("Segunda línea\n")
```

Modo `w` borra el contenido anterior. Para añadir al final, usa `a`:

```python
with open("salida.txt", "a", encoding="utf-8") as fichero:
    fichero.write("Nueva línea\n")
```

`write()` espera una cadena. Si quieres guardar un número, debes convertirlo antes:

```python
numero = 42

with open("contador.txt", "w", encoding="utf-8") as fichero:
    fichero.write(str(numero))
```

Al escribir en una ruta como `informes/salida.txt`, el fichero puede crearse si no existe, pero las carpetas intermedias deben existir previamente.

En escritura, `with` es especialmente importante porque se asegura de cerrar bien el fichero incluso si ocurre un error.

## Ejemplo: añadir una línea a un log con fecha y hora

```python
from datetime import datetime

with open("log.txt", "a", encoding="utf-8") as fichero:
    fichero.write(f"{datetime.now()} - Inicio de tarea\n")
```

## Procesar líneas

```python
contador = 0

with open("log.txt", "r", encoding="utf-8") as fichero:
    for linea in fichero:
        if "ERROR" in linea:
            contador += 1

print(f"Errores encontrados: {contador}")
```

## Capturar errores

```python
try:
    with open("datos.txt", "r", encoding="utf-8") as fichero:
        print(fichero.read())
except FileNotFoundError:
    print("No se ha encontrado el fichero")
```

## Antes del cuestionario comprueba que sabes...

- Explicar qué es un fichero y un sistema de ficheros.
- Diferenciar modos `r`, `w`, `a` y `x`.
- Saber qué ocurre al abrir en lectura un fichero inexistente.
- Reconocer `FileNotFoundError`.
- Diferenciar `read()` y `readlines()`.
- Saber para qué sirve `readline()`.
- Entender cómo avanza el puntero de lectura.
- Saber que `seek(0)` vuelve al inicio.
- Saber qué representa `\n`.
- Leer ficheros grandes línea a línea.
- Usar `enumerate()` para numerar líneas.
- Recordar que `write()` necesita cadenas.
- Usar `with open(...)`.
