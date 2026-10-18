# Bucles `while`

## Qué vas a aprender

Un bucle permite repetir instrucciones. El bucle `while` repite un bloque **mientras se cumpla una condición**.

Es útil cuando no sabemos de antemano cuántas repeticiones habrá.

## Estructura básica

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Salida:

```text
1
2
3
4
5
```

Cada repetición del bucle se llama **iteración**.

## Cómo funciona

Python evalúa la condición:

```python
contador <= 5
```

- Si es `True`, ejecuta el bloque.
- Al terminar el bloque, vuelve a comprobar la condición.
- Si es `False`, sale del bucle.

## Bucle con entrada de usuario

```python
clave = ""

while clave != "python":
    clave = input("Contraseña: ")

print("Acceso concedido")
```

Este tipo de bucle se usa mucho para repetir hasta que el usuario introduzca un dato válido.

## Bucles infinitos

Un bucle infinito ocurre cuando la condición nunca deja de cumplirse.

```python
contador = 1

while contador <= 5:
    print(contador)
    # Falta actualizar contador
```

Este programa no termina porque `contador` siempre vale `1`.

A veces se usa voluntariamente `while True`, pero debe haber una forma de salir:

```python
while True:
    comando = input("Comando: ")
    if comando == "salir":
        break
    print(f"Ejecutando {comando}")
```

## `break`

`break` sale inmediatamente del bucle.

```python
while True:
    texto = input("Escribe algo: ")
    if texto == "fin":
        break
    print(texto)
```

Cuando el usuario escribe `fin`, el bucle termina.

## `continue`

`continue` salta al inicio de la siguiente iteración.

```python
numero = 0

while numero < 5:
    numero += 1
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

Cuando `numero` vale `3`, se ejecuta `continue` y no se llega al `print()`.

## `while` con `else`

Python permite añadir un bloque `else` a un `while`.

```python
contador = 1

while contador <= 3:
    print(contador)
    contador += 1
else:
    print("Bucle terminado sin break")
```

El `else` se ejecuta cuando el bucle termina de forma normal, es decir, cuando la condición pasa a ser falsa. Si el bucle termina por `break`, el `else` no se ejecuta.

```python
contador = 1

while contador <= 3:
    if contador == 2:
        break
    print(contador)
    contador += 1
else:
    print("No se ejecuta")
```

## Validar entradas

```python
edad = input("Edad: ")

while not edad.isdigit():
    print("Debes escribir un número")
    edad = input("Edad: ")

edad = int(edad)
print(f"Edad registrada: {edad}")
```

Aquí se combina `while` con métodos de cadena.

## Antes del cuestionario comprueba que sabes...

- Explicar qué es una iteración.
- Usar `while` con una condición.
- Evitar bucles infinitos no deseados.
- Usar `break` y `continue`.
- Entender cuándo se ejecuta el `else` de un `while`.
- Validar una entrada de usuario con `while`.
