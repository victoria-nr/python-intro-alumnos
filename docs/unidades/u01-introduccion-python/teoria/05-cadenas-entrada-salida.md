# Cadenas de texto, entrada y salida, f-strings

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

## Formatear texto

En muchos programas necesitamos mostrar mensajes que combinan texto y datos almacenados en variables.

Por ejemplo:

```python
nombre = "Ana"
edad = 20
```

Queremos mostrar:

```text
Ana tiene 20 años
```

Podríamos escribir directamente:

```python
print("Ana tiene 20 años")
```

Pero eso solo funciona para esos valores concretos. Si cambian los datos, tendríamos que modificar el mensaje manualmente.

Para construir mensajes de forma dinámica utilizamos **f-strings**.

### ¿Qué es una f-string?

Una **f-string** (*formatted string literal*) es una cadena de texto que permite insertar variables y expresiones directamente dentro del texto.

Para crear una f-string se añade una `f` delante de las comillas:

```python
nombre = "Ana"
edad = 20

print(f"{nombre} tiene {edad} años")
```

Salida:

```text
Ana tiene 20 años
```

Todo lo que aparece entre llaves `{}` es sustituido por su valor.

Si olvidamos la letra `f`, Python no sustituirá las variables:

```python
nombre = "Ana"
edad = 20

print("{nombre} tiene {edad} años")
```

Salida:

```text
{nombre} tiene {edad} años
```

Si queremos mostrar llaves como texto normal, debemos escribirlas dos veces:

```python
valor = 10

print(f"El diccionario es {{'valor': {valor}}}")
```

Salida:

```text
El diccionario es {'valor': 10}
```

### Ventajas de las f-strings

Son la forma recomendada de crear mensajes porque:

* Son fáciles de leer.
* Evitan concatenaciones con `+`.
* Convierten automáticamente los valores a texto.
* Permiten incluir cálculos y expresiones.

Por ejemplo:

```python
a = 5
b = 3

print(f"La suma es {a + b}")
```

Salida:

```text
La suma es 8
```

### Formatear valores

Las f-strings permiten controlar cómo se muestran algunos datos.

Un caso muy habitual es limitar el número de decimales:

```python
precio = 19.995

print(f"Precio final: {precio:.2f} €")
```

Salida:

```text
Precio final: 20.00 €
```

El formato `.2f` indica que queremos mostrar el número con **dos decimales**.

Otro ejemplo:

```python
numero = 3.14159265

print(f"{numero:.3f}")
```

Salida:

```text
3.142
```

### Resumen

* Una f-string comienza con `f`.
* Las expresiones se escriben entre llaves `{}`.
* Permiten combinar texto y variables de forma sencilla.
* También pueden incluir cálculos.
* Facilitan el formateo de números, especialmente los decimales.



## Antes del cuestionario comprueba que sabes...

- Crear cadenas con comillas simples, dobles y triples.
- Saber qué es una cadena vacía.
- Convertir con `str()`, `int()` y `float()`.
- Entender que `input()` siempre devuelve `str`.
- Usar `print()` con `sep` y `end`.
- Concatenar, repetir, indexar y trocear cadenas.
- Saber que las cadenas son inmutables.
- Reconocer `\n`, `ord()` y `chr()`.
