# Objetos predefinidos, funciones y métodos

## Qué vas a aprender

En esta unidad no vamos a estudiar programación orientada a objetos completa. La idea es más sencilla: en Python usamos constantemente **objetos ya creados** y operaciones asociadas a esos objetos.

Una cadena, un número o una lista son objetos. Cada objeto tiene un tipo, y algunos tipos ofrecen métodos útiles.

## Función frente a método

Una función se llama así:

```python
print("Hola")
len("Python")
type(10)
```

Un método se llama sobre un objeto usando punto:

```python
texto = "python"
print(texto.upper())
```

`upper()` es un método de las cadenas. Se escribe después del objeto:

```text
objeto.metodo()
```

## Ejemplo con cadenas

```python
mensaje = "  hola ana  "
limpio = mensaje.strip()
mayusculas = limpio.upper()

print(limpio)
print(mayusculas)
```

Salida:

```text
hola ana
HOLA ANA
```

La variable `mensaje` apunta a una cadena. Como las cadenas son inmutables, `strip()` y `upper()` no modifican la cadena original: devuelven una nueva.

```python
mensaje = "  hola  "
mensaje.strip()
print(mensaje)  # Sigue teniendo espacios
```

Para conservar el resultado:

```python
mensaje = mensaje.strip()
```

## Métodos con parámetros

Algunos métodos necesitan información adicional:

```python
texto = "python es genial"
print(texto.replace("python", "Python"))
```

`replace()` necesita saber qué texto buscar y por cuál sustituirlo.

También puede recibir un tercer parámetro para limitar el número de sustituciones:

```python
proverbio = "mal, mal, mal"
print(proverbio.replace("mal", "bien", 1))
```

Salida:

```text
bien, mal, mal
```

## Métodos que devuelven booleanos

Muchos métodos responden con `True` o `False`:

```python
texto = "abc"
print(texto.isalpha())   # True
print(texto.isdigit())   # False
print(texto.startswith("a"))  # True
```

Esto será muy útil en condicionales:

```python
codigo = input("Código: ")

if codigo.isdigit():
    print("Código numérico")
else:
    print("Código no válido")
```

## Consultar métodos disponibles

Puedes explorar métodos con ayuda del editor, con documentación o con:

```python
help(str)
```

No necesitas memorizar todos los métodos. Es más importante aprender a buscar, probar y leer ejemplos.

## Error frecuente: olvidar los paréntesis

```python
texto = "hola"
print(texto.upper)    # Muestra una referencia al método, no lo ejecuta
print(texto.upper())  # Ejecuta el método
```

## Antes de seguir comprueba que sabes...

- Diferenciar función y método.
- Reconocer la sintaxis `objeto.metodo()`.
- Entender que muchos métodos devuelven un nuevo valor.
- Saber que las cadenas son inmutables.
- Usar métodos en pequeños programas.
