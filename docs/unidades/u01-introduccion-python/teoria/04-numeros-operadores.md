# Números, booleanos y operadores

## Qué vas a aprender

Los programas hacen cálculos continuamente: sumar precios, comprobar edades, calcular porcentajes, comparar valores o repetir procesos. Para eso necesitas conocer los tipos numéricos, los booleanos y los operadores.

## Booleanos

Un booleano solo puede tener dos valores:

```python
True
False
```

Deben escribirse con la primera letra en mayúscula. Esto es correcto:

```python
activo = True
```

Esto es incorrecto:

```python
activo = true  # Error: true no existe
```

Los booleanos vienen de la lógica booleana, asociada históricamente a George Boole. En programación se usan para representar condiciones: aprobado/no aprobado, activo/inactivo, existe/no existe.

En operaciones numéricas, Python trata `True` como `1` y `False` como `0`:

```python
print(True + 3)   # 4
print(False + 3)  # 3
```

No conviene abusar de esto, pero ayuda a entender cómo funcionan internamente.

## Enteros

Los enteros se representan con `int`:

```python
edad = 20
saldo = -50
```

Puedes usar guiones bajos para hacer números grandes más legibles:

```python
poblacion = 47_000_000
```

Python no permite escribir enteros con un cero inicial como `08`:

```python
numero = 08  # Error de sintaxis
```

## Bases numéricas

Python permite escribir números en distintas bases:

```python
binario = 0b1010   # 10 en decimal
octal = 0o12       # 10 en decimal
hexadecimal = 0xA  # 10 en decimal
```

El prefijo `0b` indica base binaria.

## Flotantes

Los números decimales se representan con `float`:

```python
precio = 19.99
temperatura = -3.5
```

También pueden escribirse en notación científica:

```python
valor = 0.4e1
print(valor)  # 4.0
```

Cuando mezclas un entero y un flotante, el resultado suele ser flotante:

```python
resultado = 3 + 2.5
print(resultado)        # 5.5
print(type(resultado))  # <class 'float'>
```

## Operadores aritméticos

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `+` | suma | `3 + 2` | `5` |
| `-` | resta | `3 - 2` | `1` |
| `*` | multiplicación | `3 * 2` | `6` |
| `/` | división real | `9 / 2` | `4.5` |
| `//` | división entera | `9 // 2` | `4` |
| `%` | resto | `9 % 4` | `1` |
| `**` | potencia | `2 ** 3` | `8` |

Ejemplos:

```python
print(9 // 2)  # 4
print(9 % 4)   # 1
print(2 ** 3)  # 8
```

Ejemplos prácticos muy habituales:

```python
minutos_totales = 1000
horas = minutos_totales // 60
minutos = minutos_totales % 60
print(horas, minutos)  # 16 40

numero = 23
decenas = numero // 10
unidades = numero % 10
print(unidades * 10 + decenas)  # 32
```

La potencia también sirve para representar raíces con exponentes fraccionarios:

```python
cateto1 = 3
cateto2 = 4
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
print(hipotenusa)  # 5.0

numero = 27
raiz_cubica = numero ** (1 / 3)
print(raiz_cubica)  # 3.0
```

La división entre cero produce un error:

```python
print(10 / 0)  # ZeroDivisionError
```

## Prioridad de operadores

Python sigue reglas de prioridad. Los paréntesis tienen la prioridad más alta porque fuerzan que esa parte se calcule antes. Después, la potencia `**` tiene prioridad alta. Luego van multiplicación, división y resto. Finalmente suma y resta.

```python
resultado = 2 + 3 * 4
print(resultado)  # 14
```

Si quieres otro orden, usa paréntesis:

```python
resultado = (2 + 3) * 4
print(resultado)  # 20
```

## Asignación aumentada

Estas dos instrucciones son equivalentes:

```python
x = x + 3
x += 3
```

También existen:

```python
x -= 1
x *= 2
x /= 4
x //= 2
x %= 3
```

## Funciones numéricas útiles

```python
print(abs(-7))      # 7
print(round(3.1416, 2))  # 3.14
print(int(3.9))     # 3
print(float("3.5")) # 3.5
```

`int(3.9)` no redondea: elimina la parte decimal.

`round()` sí sirve para redondear.

## Comparaciones

Las comparaciones devuelven booleanos:

```python
edad = 18
print(edad >= 18)  # True
print(edad < 18)   # False
```

Operadores habituales:

| Operador | Significado |
|---|---|
| `==` | igual |
| `!=` | distinto |
| `<` | menor |
| `<=` | menor o igual |
| `>` | mayor |
| `>=` | mayor o igual |

No confundas `=` con `==`:

```python
edad = 18       # asigna
edad == 18      # compara
```

## Antes del cuestionario comprueba que sabes...

- Usar `True` y `False` correctamente.
- Saber que `True` equivale a `1` y `False` a `0` en operaciones numéricas.
- Calcular con `//`, `%` y `**`.
- Entender `x += 3`.
- Saber qué hacen `abs()`, `round()`, `int()` y `float()`.
- Reconocer errores como división por cero o enteros con cero inicial.
