# Bucles `for`, `range()` y recorridos

## Qué vas a aprender

El bucle `for` sirve para recorrer elementos de una secuencia o iterable: cadenas, listas, rangos, líneas de un fichero, etc.

A diferencia de `while`, normalmente usamos `for` cuando sí sabemos qué conjunto de elementos queremos recorrer.

## Recorrer una cadena

```python
for letra in "Python":
    print(letra)
```

Salida:

```text
P
y
t
h
o
n
```

Sí: un `for` puede recorrer cadenas de texto.

## Recorrer una lista

```python
alumnos = ["Ana", "Luis", "Marta"]

for alumno in alumnos:
    print(alumno)
```

## `range()`

`range()` genera una secuencia de números. Es muy habitual en bucles.

```python
for numero in range(5):
    print(numero)
```

Salida:

```text
0
1
2
3
4
```

`range(5)` empieza en 0 y llega hasta 5 sin incluirlo.

También puedes indicar inicio, fin y paso:

```python
for numero in range(1, 6, 2):
    print(numero)
```

Salida:

```text
1
3
5
```

`range(1, 6, 2)` significa: empieza en 1, llega hasta antes de 6, avanzando de 2 en 2.

También puede usarse con paso negativo para contar hacia atrás:

```python
for numero in range(2, -1, -1):
    print(numero)
```

Salida:

```text
2
1
0
```

Aquí `range(2, -1, -1)` empieza en `2`, baja de uno en uno y se detiene antes de `-1`.

## `range()` no devuelve una lista

En Python 3, `range()` devuelve un objeto de tipo `range`, no una lista.

```python
valores = range(5)
print(valores)        # range(0, 5)
print(list(valores))  # [0, 1, 2, 3, 4]
```

Esto permite trabajar de forma eficiente con rangos grandes.

## Índices con `enumerate()`

Si necesitas el índice y el valor, usa `enumerate()`:

```python
alumnos = ["Ana", "Luis", "Marta"]

for indice, alumno in enumerate(alumnos):
    print(indice, alumno)
```

También puedes indicar el índice inicial:

```python
for indice, alumno in enumerate(alumnos, 1):
    print(indice, alumno)
```

Si no necesitas usar la variable del bucle, es habitual escribir `_`:

```python
for _ in range(3):
    print("Repetir")
```

El guion bajo no tiene un significado mágico especial, pero se usa como convención para indicar: "esta variable no me interesa".

## `break` en un `for`

`break` termina el bucle:

```python
for numero in range(1, 10):
    if numero == 5:
        break
    print(numero)
```

Salida:

```text
1
2
3
4
```

## `continue` en un `for`

`continue` salta a la siguiente iteración:

```python
for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)
```

Salida:

```text
1
2
4
5
```

## `for` con `else`

Igual que ocurre con `while`, un bucle `for` puede llevar un bloque `else`.

El `else` se ejecuta cuando el bucle termina de forma normal, es decir, sin pasar por un `break`.

```python
numero = 7

for divisor in range(2, numero):
    if numero % divisor == 0:
        print("No es primo")
        break
else:
    print("Es primo")
```

Este patrón es útil cuando recorres varios valores buscando un caso especial. Si lo encuentras, haces `break`. Si no aparece ninguno, se ejecuta el `else`.

## Bucles anidados

Un bucle puede estar dentro de otro:

```python
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"Fila {fila}, columna {columna}")
```

Hay que usarlos con cuidado porque multiplican el número de iteraciones.

## Ejemplo aplicado

```python
archivos = ["log1.txt", "foto.png", "log2.txt", "datos.csv"]

for archivo in archivos:
    if archivo.endswith(".txt"):
        print(f"Procesar {archivo}")
```

Este patrón se repetirá mucho en administración de sistemas: recorrer elementos, comprobar una condición y actuar.

## Antes del cuestionario comprueba que sabes...

- Recorrer cadenas y listas con `for`.
- Usar `range(fin)`, `range(inicio, fin)` y `range(inicio, fin, paso)`.
- Usar `range()` con paso negativo para contar hacia atrás.
- Saber que `range()` no devuelve directamente una lista.
- Usar `break` y `continue`.
- Entender cuándo se ejecuta un bloque `else` asociado a un `for`.
- Reconocer el uso de `_` cuando no hace falta aprovechar la variable del bucle.
- Usar `enumerate()` para obtener índice y valor.
