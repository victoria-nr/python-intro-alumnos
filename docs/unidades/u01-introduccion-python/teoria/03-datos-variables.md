# Datos, variables, tipos y objetos

## Qué vas a aprender

En Python trabajamos constantemente con datos: números, textos, valores lógicos, listas, diccionarios y otros muchos. Para poder usarlos, necesitamos guardarlos en variables y entender su tipo.

## Qué es un dato

Un dato es una pieza de información que un programa puede manejar. Por ejemplo:

```python
42
"Ana"
3.14
True
```

Cada dato tiene un **tipo**. El tipo determina qué operaciones tienen sentido.

```python
print(type(42))       # <class 'int'>
print(type("Ana"))    # <class 'str'>
print(type(3.14))     # <class 'float'>
print(type(True))     # <class 'bool'>
```

En Python, una forma sencilla de pensar en un dato es esta: un objeto tiene **tipo**, **identidad o identificador interno** y **valor**. Más adelante veremos más detalles, pero esta idea básica ya ayuda a entender por qué `type()` e `id()` son útiles.

Algunos tipos básicos son:

| Tipo | Ejemplo | Uso |
|---|---|---|
| `int` | `10` | Enteros |
| `float` | `3.5` | Decimales |
| `str` | `"hola"` | Texto |
| `bool` | `True` | Verdadero/falso |
| `complex` | `3+5j` | Números complejos |

## En Python todo son objetos

Una idea importante de Python es que **todo son objetos**. Un número, una cadena o una lista son objetos. Por eso podemos consultar su tipo o usar métodos en algunos de ellos.

```python
texto = "python"
print(type(texto))
print(texto.upper())
```

No hace falta entender todavía la programación orientada a objetos completa. De momento basta con esta idea: los datos no son “cosas sueltas”, sino objetos con un tipo y, muchas veces, operaciones asociadas.

## Variables

Una variable es un nombre que apunta a un dato.

```python
nombre = "Ana"
edad = 20
```

La instrucción:

```python
num_items = 10
```

significa que el nombre `num_items` queda asociado al valor `10`.

El lado izquierdo de una asignación es el **identificador** o nombre de la variable. A veces se llama **LHS** (`left-hand side`). El lado derecho es el valor o expresión que se evalúa, y puede llamarse **RHS** (`right-hand side`).

```python
precio = 50 + 10
```

Primero se calcula `50 + 10`; después el resultado se guarda bajo el nombre `precio`.

## Nombres de variables

Un nombre de variable puede contener letras, números y guiones bajos, pero no puede empezar por número.

Correctos:

```python
edad = 20
nombre_alumno = "Ana"
precio2 = 15.5
```

Incorrectos:

```python
2precio = 10      # No puede empezar por número
nombre-alumno = "Ana"  # El guion se interpreta como resta
class = "ASIR"    # class es palabra reservada
```

Buenas prácticas:

- usa nombres claros;
- evita nombres demasiado cortos si no aportan;
- usa minúsculas y guiones bajos;
- no uses nombres de funciones internas como `type`, `input`, `list` o `str`.

Mejor:

```python
numero_alumnos = 25
```

Peor:

```python
na = 25
```

## Constantes

Python no tiene constantes estrictas como otros lenguajes. Por convenio, se escriben en mayúsculas:

```python
IVA = 0.21
MAX_INTENTOS = 3
```

El programa no impide modificar `IVA`, pero escribirlo en mayúsculas indica al programador que ese valor no debería cambiar.

## Asignación múltiple

Python permite asignar varios valores a la vez:

```python
nombre, edad = "Ana", 20
```

También puedes asignar el mismo valor a varias variables:

```python
a = b = c = 0
```

Hay que tener cuidado con objetos mutables, como listas, porque varias variables pueden apuntar al mismo objeto.

## Identidad y memoria: `id()`

La función `id()` devuelve un identificador asociado al objeto en memoria durante la ejecución.

```python
x = [1, 2, 3]
y = x
print(id(x))
print(id(y))
```

Si `x` e `y` apuntan al mismo objeto, modificar uno afecta al otro:

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)  # [1, 2, 3, 4]
```

## Mutabilidad

Un objeto **mutable** puede cambiar después de crearse. Una lista es mutable.

```python
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)
```

Un objeto **inmutable** no puede cambiarse directamente. Enteros, flotantes, booleanos, cadenas y tuplas son inmutables.

```python
texto = "hola"
# texto[0] = "H"  # Error
```

Si quieres cambiar una cadena, normalmente creas otra:

```python
texto = "Hola" + texto[1:]
```

## Ayuda integrada

Python permite pedir ayuda desde el intérprete:

```python
help(print)
help(str)
```

También puedes usar `type()` para comprobar tipos:

```python
valor = "10"
print(type(valor))
```

## Antes del cuestionario comprueba que sabes...

- Reconocer tipos básicos: `int`, `float`, `str`, `bool`, `complex`.
- Usar `type()`.
- Crear variables con nombres válidos.
- Distinguir variable, valor y asignación.
- Entender la idea básica de objeto.
- Saber qué es mutable e inmutable.
- Saber para qué sirven `id()` y `help()`.
