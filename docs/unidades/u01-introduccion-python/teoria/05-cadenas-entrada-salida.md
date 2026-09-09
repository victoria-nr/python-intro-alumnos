# Cadenas de texto, entrada y salida

## Qué vas a aprender

Las cadenas de texto, o `str`, sirven para trabajar con nombres, mensajes, rutas, líneas de ficheros, comandos, textos introducidos por el usuario y muchos otros datos.

## Crear cadenas

Puedes crear cadenas con comillas simples o dobles:

```python
nombre = 'Ana'
mensaje = "Hola"
```

Ambas formas son válidas. Elige una y sé consistente.

Las cadenas multilínea suelen escribirse con triple comilla:

```python
texto = """Primera línea
Segunda línea
Tercera línea"""
```

En documentación de funciones se usan docstrings, y la guía PEP 257 recomienda comillas triples dobles para ese tipo de cadenas.

La cadena vacía se representa así:

```python
vacia = ""
```

## Unicode

Python 3 usa Unicode para representar texto. Esto permite trabajar con caracteres de muchos idiomas:

```python
texto = "áéíóú ñ 中文 😀"
print(texto)
```

Cada carácter tiene un código numérico. Puedes consultarlo con `ord()`:

```python
print(ord("A"))
```

Y puedes obtener un carácter a partir de su código con `chr()`:

```python
print(chr(65))  # A
```

## Conversión de tipos

A veces necesitamos convertir valores:

```python
numero = 10
texto = str(numero)
print(texto)
```

También podemos convertir texto a número si el contenido es válido:

```python
edad = int("20")
precio = float("3.50")
```

Si el texto no representa un número válido, Python falla:

```python
float("3.1a")  # ValueError
```

`int()` permite indicar base:

```python
print(int("1010", 2))  # 10
```

## Saltos de línea y caracteres de escape

Algunos caracteres se escriben con secuencias de escape:

| Secuencia | Significado |
|---|---|
| `\n` | salto de línea |
| `\t` | tabulación |
| `\\` | barra invertida |
| `\"` | comilla doble |

Ejemplo:

```python
print("abc\ndef")
```

Salida:

```text
abc
def
```

## Mostrar información con `print()`

`print()` muestra información por pantalla:

```python
nombre = "Ana"
edad = 20
print(nombre, edad)
```

Por defecto separa los valores con espacios. Puedes cambiar el separador con `sep`:

```python
print("Ana", "20", "ASIR", sep=";")
```

Salida:

```text
Ana;20;ASIR
```

También puedes cambiar el final con `end`:

```python
print("Hola", end=" ")
print("Ana")
```

Salida:

```text
Hola Ana
```

## Pedir información con `input()`

`input()` pide un dato al usuario y siempre devuelve una cadena de texto:

```python
nombre = input("Nombre: ")
print("Hola", nombre)
```

Aunque el usuario escriba un número, el resultado sigue siendo texto:

```python
edad = input("Edad: ")
print(type(edad))  # <class 'str'>
```

Para calcular con ese valor hay que convertirlo:

```python
edad = int(input("Edad: "))
print(edad + 1)
```

No uses `input` como nombre de variable:

```python
input = "Ana"  # Mala práctica
```

Estarías tapando la función `input()`.

## Operaciones con cadenas

### Concatenar

```python
saludo = "Hola" + " " + "Ana"
print(saludo)
```

### Repetir

```python
print("Wow" * 3)  # WowWowWow
```

### Longitud

```python
print(len("Hola"))  # 4
```

### Comprobar si un texto está dentro de otro

```python
frase = "Hola, Ana"
print("Ana" in frase)   # True
print("Luis" in frase)  # False
```

### Índices

```python
texto = "Python"
print(texto[0])  # P
print(texto[1])  # y
print(texto[-1]) # n
```

### Troceado o slicing

La sintaxis `[start:end]` toma caracteres desde `start` hasta antes de `end`:

```python
texto = "Python"
print(texto[0:2])  # Py
print(texto[2:])   # thon
print(texto[:4])   # Pyth
```

El índice final no se incluye.

## Las cadenas son inmutables

No puedes modificar directamente un carácter:

```python
texto = "python"
# texto[0] = "P"  # Error
```

Debes crear una nueva cadena:

```python
texto = "P" + texto[1:]
print(texto)  # Python
```

## Antes del cuestionario comprueba que sabes...

- Crear cadenas con comillas simples, dobles y triples.
- Saber qué es una cadena vacía.
- Convertir con `str()`, `int()` y `float()`.
- Entender que `input()` siempre devuelve `str`.
- Usar `print()` con `sep` y `end`.
- Concatenar, repetir, indexar y trocear cadenas.
- Saber que las cadenas son inmutables.
- Reconocer `\n`, `ord()` y `chr()`.
