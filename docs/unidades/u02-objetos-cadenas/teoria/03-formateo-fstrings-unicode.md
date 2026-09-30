# Formateo de cadenas, f-strings y Unicode

## Por qué necesitamos formatear texto

Muchos programas tienen que mostrar mensajes combinando texto y variables:

```python
nombre = "Ana"
edad = 20
print("Ana tiene 20 años")
```

Pero lo normal es que esos datos cambien. Para eso usamos f-strings.

## f-strings

Una f-string empieza con `f` antes de las comillas:

```python
nombre = "Ana"
edad = 20
print(f"{nombre} tiene {edad} años")
```

Salida:

```text
Ana tiene 20 años
```

Si olvidas la `f`, Python no sustituye las variables:

```python
print("{nombre} tiene {edad} años")
```

Salida:

```text
{nombre} tiene {edad} años
```

## Llaves literales

Si quieres mostrar llaves dentro de una f-string, debes duplicarlas:

```python
valor = 10
print(f"El diccionario es {{'valor': {valor}}}")
```

## Formatear enteros, flotantes y cadenas

Las f-strings permiten indicar formato:

```python
cantidad = 7
precio = 3.5
nombre = "Ana"

print(f"Cantidad: {cantidad:d}")
print(f"Precio: {precio:.2f}")
print(f"Nombre: {nombre:s}")
```

- `d` se usa para enteros.
- `f` se usa para flotantes.
- `s` se usa para cadenas.
- `.2f` muestra dos decimales.

Ejemplo:

```python
precio = 19.995
print(f"Precio final: {precio:.2f} €")
```

## Modo debug de f-strings

Desde Python 3.8 puedes usar `=` para mostrar el nombre de la variable y su valor:

```python
edad = 20
print(f"{edad=}")
```

Salida:

```text
edad=20
```

Esto es muy útil para depurar programas pequeños.

## Unicode, `ord()` y `chr()`

Python 3 representa cadenas usando Unicode. Cada carácter tiene un código numérico.

```python
print(ord("A"))  # 65
print(chr(65))   # A
```

Esto explica por qué Python puede ordenar y comparar caracteres. En Unicode, las letras mayúsculas latinas básicas aparecen antes que las minúsculas:

```python
print("A" < "a")  # True
```

Al comparar cadenas, Python compara carácter a carácter según sus códigos Unicode.

```python
print("Ana" < "ana")
```

Este tipo de comparación puede sorprender, por eso conviene normalizar mayúsculas/minúsculas antes de comparar texto de usuarios:

```python
respuesta = input("Sí o no: ").strip().lower()
if respuesta == "si" or respuesta == "sí":
    print("Has aceptado")
```

## Ejemplo práctico

```python
nombre = input("Nombre: ").strip().title()
nota = float(input("Nota: "))

print(f"Alumno: {nombre}")
print(f"Nota final: {nota:.2f}")
print(f"Debug: {nota=}")
```

## Antes del cuestionario comprueba que sabes...

- Crear f-strings con variables.
- Saber qué pasa si olvidas la `f`.
- Mostrar llaves literales con `{{` y `}}`.
- Usar formatos `d`, `f` y `s`.
- Redondear visualmente con `.2f`.
- Usar `ord()` y `chr()`.
- Entender que las comparaciones de cadenas siguen el orden Unicode.
