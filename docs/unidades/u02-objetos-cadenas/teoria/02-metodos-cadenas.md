# Métodos habituales de cadenas

## Limpiar espacios: `strip()`, `lstrip()` y `rstrip()`

Cuando el usuario introduce datos, es habitual que aparezcan espacios de más.

```python
nombre = "  Ana  "
print(nombre.strip())   # "Ana"
print(nombre.lstrip())  # "Ana  "
print(nombre.rstrip())  # "  Ana"
```

- `strip()` limpia por ambos lados.
- `lstrip()` limpia por la izquierda.
- `rstrip()` limpia por la derecha.

Recuerda: no modifican la cadena original.

```python
nombre = "  Ana  "
nombre.strip()
print(nombre)  # sigue igual
```

Correcto:

```python
nombre = nombre.strip()
```

## Acceder a caracteres y trocear cadenas

Además de usar métodos, con las cadenas también trabajamos mucho con índices y troceado.

```python
frase = "Python es genial"

print(frase[0])    # P
print(frase[-1])   # l
print(frase[0:6])  # Python
print(frase[-5:])  # genial
print(frase[::2])  # Pto sgnl
print(frase[::-1]) # laineg se nohtyP
```

- `cadena[posicion]` obtiene un carácter concreto.
- Los índices negativos cuentan desde el final.
- `cadena[inicio:fin]` extrae una parte de la cadena.
- `cadena[::2]` toma saltos de 2 en 2.
- `cadena[::-1]` devuelve la cadena al revés.

Esto es muy útil para extraer prefijos, sufijos, nombres de usuario, partes de rutas o fragmentos de etiquetas como `PC-AULA-23`.

## Longitud, repetición y pertenencia

Hay operaciones básicas que aparecen mucho en ejercicios de cadenas:

```python
palabra = "hola"
frase = "Ana estudia Python"

print(len(palabra))      # 4
print(palabra * 3)       # holaholahola
print("Ana" in frase)   # True
print("Luis" in frase)  # False
```

- `len(cadena)` devuelve cuántos caracteres tiene.
- `cadena * n` repite la cadena varias veces.
- `subcadena in cadena` comprueba si un texto está dentro de otro y devuelve `True` o `False`.

## Secuencias de escape y cadenas multilínea

En algunos programas necesitamos escribir saltos de línea, tabulaciones o comillas dentro del propio texto.

```python
mensaje = "Esta es una 'cadena' con comillas dobles,\nuna nueva línea y \tuna tabulación."
print(mensaje)
```

Las secuencias más habituales son estas:

- `\n` salto de línea
- `\t` tabulación
- `\"` comillas dobles dentro de una cadena con comillas dobles

También puedes escribir texto en varias líneas con comillas triples:

```python
ficha = """Título: Python
Autor: Guido van Rossum
Año: 1991"""

print(ficha)
```

## Comprobar inicio y final

```python
archivo = "informe.pdf"
print(archivo.startswith("inf"))  # True
print(archivo.endswith(".pdf"))   # True
```

Esto resulta muy útil para validar nombres de archivo o extensiones.

## Buscar texto: `find()` e `index()`

Ambos buscan una subcadena dentro de otra:

```python
texto = "administracion de sistemas"
print(texto.find("sis"))
print(texto.index("sis"))
```

La diferencia aparece cuando no encuentran el texto:

```python
print(texto.find("redes"))   # -1
print(texto.index("redes"))  # ValueError
```

- `find()` devuelve `-1` si no encuentra.
- `index()` lanza un error si no encuentra.

## Contar apariciones

```python
texto = "banana"
print(texto.count("a"))  # 3
```

`count()` cuenta cuántas veces aparece una subcadena.

## Reemplazar texto

```python
mensaje = "hola ana"
print(mensaje.replace("ana", "Laura"))
```

También puedes limitar el número de reemplazos:

```python
proverbio = "mal mal mal"
print(proverbio.replace("mal", "bien", 1))
```

Salida:

```text
bien mal mal
```

## Mayúsculas, minúsculas y formato

```python
texto = "python"
print(texto.upper())       # PYTHON
print(texto.capitalize())  # Python
print(texto.title())       # Python
```

`capitalize()` pone en mayúscula la primera letra y el resto en minúscula:

```python
print("quien a buen árbol".capitalize())
```

## Comprobaciones de contenido

```python
print("abc".isalpha())    # True, solo letras
print("abc123".isalnum()) # True, letras o números
print("123".isdigit())    # True
print("BIG".isupper())    # True
print("big".islower())    # True
```

Estas funciones devuelven booleanos y son muy útiles para validar entradas.

## Ejemplo práctico

```python
usuario = input("Usuario: ").strip()

if usuario.isalnum():
    print("Usuario válido")
else:
    print("El usuario solo puede contener letras y números")
```

## Antes del cuestionario comprueba que sabes...

- Saber qué hacen `strip()`, `lstrip()` y `rstrip()`.
- Usar `startswith()` y `endswith()`.
- Diferenciar `find()` e `index()`.
- Usar `count()` y `replace()`.
- Comprobar texto con `isalpha()`, `isalnum()`, `isdigit()`, `isupper()` e `islower()`.
