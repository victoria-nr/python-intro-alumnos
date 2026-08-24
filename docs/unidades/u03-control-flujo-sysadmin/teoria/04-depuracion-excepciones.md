# Depuración, errores y excepciones

## Qué vas a aprender

Programar implica equivocarse. La diferencia entre un principiante y alguien que progresa no es no cometer errores, sino aprender a localizarlos, entenderlos y corregirlos.

## Tipos de errores

### Errores de sintaxis

Ocurren cuando el código no respeta las reglas del lenguaje.

```python
if edad >= 18
    print("OK")
```

Faltan los dos puntos. Python no puede ejecutar el programa.

### Errores en tiempo de ejecución

El programa empieza, pero falla mientras se ejecuta.

```python
numero = int("abc")
```

Esto produce `ValueError` porque `"abc"` no puede convertirse a entero.

### Errores lógicos

El programa no falla, pero el resultado es incorrecto.

```python
precio = 100
iva = 21
precio_final = precio + iva  # funciona, pero quizá debería ser precio * 0.21
```

Estos son los más difíciles porque Python no avisa.

## Leer trazas de error

Cuando Python falla, muestra una traza. Debes fijarte en:

- el tipo de error;
- la línea indicada;
- la última llamada de la traza;
- el mensaje final.

Ejemplo típico:

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

La pista es clara: se intentó convertir `abc` a entero.

## Probar con casos pequeños

No escribas 50 líneas y pruebes al final. Es mejor probar poco a poco.

```python
edad = input("Edad: ")
print(f"DEBUG: {edad=}")
```

Las f-strings con `=` ayudan a ver valores durante la ejecución.

## `try` y `except`

Podemos capturar errores previsibles:

```python
texto = input("Número: ")

try:
    numero = int(texto)
    print(numero * 2)
except ValueError:
    print("Debes escribir un número entero")
```

No uses `try/except` para ocultar errores que no entiendes. Primero intenta entender qué puede fallar.

## `raise`

Puedes lanzar una excepción cuando una situación no es válida:

```python
edad = -5

if edad < 0:
    raise ValueError("La edad no puede ser negativa")
```

## `assert`

`assert` permite comprobar condiciones durante el desarrollo:

```python
edad = 20
assert edad >= 0
```

Si la condición es falsa, Python lanza `AssertionError`.

```python
edad = -1
assert edad >= 0, "La edad no puede ser negativa"
```

Las aserciones son útiles para detectar errores internos mientras desarrollas, no para validar siempre datos de usuario en producción.

## Depuración paso a paso

En VS Code puedes usar puntos de interrupción. También puedes imprimir valores temporalmente:

```python
print(f"DEBUG: {variable=}")
```

Una estrategia sencilla:

1. Reproduce el error.
2. Lee la traza.
3. Localiza la línea.
4. Imprime o inspecciona variables.
5. Prueba con un caso pequeño.
6. Corrige y vuelve a probar.

## Antes de seguir comprueba que sabes...

- Diferenciar error de sintaxis, ejecución y lógica.
- Leer el tipo de error al final de una traza.
- Usar `try/except` con `ValueError`.
- Saber para qué sirven `raise` y `assert`.
- Usar mensajes de depuración sencillos.
