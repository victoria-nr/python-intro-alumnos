# Cadenas y listas: `split()`, `join()` y recorridos

## Qué vas a aprender

Muchas veces recibimos información como texto y necesitamos convertirla en una lista para procesarla. O al revés: tenemos una lista y queremos convertirla en una cadena.

## `split()`

`split()` divide una cadena y devuelve una lista.

```python
texto = "Ana Luis Marta"
alumnos = texto.split()
print(alumnos)
```

Resultado:

```python
['Ana', 'Luis', 'Marta']
```

Por defecto separa por espacios.

Puedes indicar separador:

```python
datos = "a,b,c,d"
print(datos.split(","))
```

También puedes indicar un máximo de divisiones:

```python
print('a,b,c,d'.split(',', 2))
```

Resultado:

```python
['a', 'b', 'c,d']
```

## `splitlines()`

Divide un texto por líneas:

```python
texto = "uno\ndos\ntres"
print(texto.splitlines())
```

Resultado:

```python
['uno', 'dos', 'tres']
```

## `partition()`

`partition()` divide una cadena en tres partes: antes del separador, separador y después.

```python
print('3+4'.partition('+'))
```

Resultado:

```python
('3', '+', '4')
```

Devuelve una tupla.

## `join()`

`join()` une una lista de cadenas:

```python
valores = ['A', 'B', 'C']
print(','.join(valores))
```

Resultado:

```text
A,B,C
```

Todos los elementos deben ser cadenas. Esto falla:

```python
numeros = [1, 2, 3]
print(','.join(numeros))  # TypeError
```

Solución:

```python
numeros = [1, 2, 3]
textos = []

for numero in numeros:
    textos.append(str(numero))

print(','.join(textos))
```

## `split()` y `join()` son operaciones opuestas

De forma simplificada:

```python
texto = "a,b,c"
lista = texto.split(",")
otro_texto = ",".join(lista)
```

`split()` rompe una cadena en lista. `join()` une una lista de cadenas.

## Ordenar listas

Si además de crear listas quieres ordenarlas, tienes dos opciones habituales:

```python
nombres = ['Luis', 'Ana', 'Marta']

ordenados = sorted(nombres)
print(ordenados)
print(nombres)

nombres.sort()
print(nombres)
```

- `sorted(lista)` devuelve una lista nueva ordenada.
- `lista.sort()` ordena la lista original y no devuelve una nueva lista.

## `enumerate()` y `zip()`

`enumerate()` permite recorrer una lista obteniendo índice y valor:

```python
print(list(enumerate(['a', 'b'], 10)))
```

Resultado:

```python
[(10, 'a'), (11, 'b')]
```

`zip()` combina elementos por posición:

```python
print(list(zip(['a', 'b'], [1, 2])))
```

Resultado:

```python
[('a', 1), ('b', 2)]
```

## Comparar listas

Python compara listas elemento a elemento desde el principio:

```python
print(['a', 'c'] > ['a', 'b'])
print([1, 2] == [1, 2])
```

Primero compara el primer elemento. Si son iguales, sigue con el siguiente.

## Copias y referencias

Con `=` no se crea una copia independiente. Solo otra referencia al mismo objeto:

```python
original = [1, 2, 3]
alias = original

alias[0] = 99
print(original)
```

Si quieres una copia independiente, usa `copy()`:

```python
original = [1, 2, 3]
copia = original.copy()

copia[0] = 0
print(original)
print(copia)
```

## `all()` y `any()`

Estas funciones trabajan muy bien con listas de condiciones:

```python
condiciones = [True, True, False]

print(all(condiciones))
print(any(condiciones))
print(any([]))
```

- `all()` devuelve `True` solo si todas las condiciones son verdaderas.
- `any()` devuelve `True` si al menos una lo es.
- `any([])` devuelve `False`.

## Listas por comprensión

Una lista por comprensión permite crear listas de forma más concisa:

```python
numeros = [int(v) for v in '1,2,3'.split(',')]
print(numeros)
```

Resultado:

```python
[1, 2, 3]
```

También pueden llevar condición:

```python
vocales = [x for x in 'python' if x in 'aeiou']
print(vocales)
```

Resultado:

```python
['o']
```

Son útiles porque suelen ser más concisas y expresivas que un bucle muy repetitivo.

## `sys.argv` también es una lista

En scripts de consola, `sys.argv` guarda los argumentos de línea de comandos dentro de una lista:

```python
import sys

print(sys.argv)
```

Puedes acceder a sus elementos igual que en cualquier otra lista.

## Ejemplo práctico: procesar una línea CSV sencilla

```python
linea = "ana,20,ASIR"
campos = linea.split(",")

nombre = campos[0]
edad = int(campos[1])
grupo = campos[2]

print(f"{nombre} tiene {edad} años y estudia {grupo}")
```

## Antes del cuestionario comprueba que sabes...

- Usar `split()` sin separador y con separador.
- Interpretar `split(',', 2)`.
- Usar `splitlines()`.
- Saber qué devuelve `partition()`.
- Usar `join()`.
- Saber que `join()` requiere cadenas.
- Relacionar `split()` y `join()`.
- Diferenciar `sorted()` y `sort()`.
- Usar `enumerate()` y `zip()`.
- Entender cómo se comparan listas.
- Diferenciar referencia compartida y copia con `copy()`.
- Usar `all()`, `any()` y listas por comprensión.
- Saber que `sys.argv` es una lista de argumentos.
