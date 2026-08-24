# Listas y tuplas

## Qué vas a aprender

Una estructura de datos permite guardar varios valores juntos. En esta unidad empezamos con listas y tuplas.

## Listas

Una lista guarda una colección ordenada de elementos:

```python
alumnos = ["Ana", "Luis", "Marta"]
```

Las listas:

- mantienen el orden;
- permiten elementos duplicados;
- son mutables;
- pueden contener valores de distintos tipos, aunque normalmente intentamos ser coherentes.

```python
valores = [1, 2, 2, 3]
```

## Crear listas

```python
numeros = [1, 2, 3]
vacia = []
letras = list("Python")
```

`list("Python")` devuelve:

```python
['P', 'y', 't', 'h', 'o', 'n']
```

## Índices

```python
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

print(shopping[0])   # Agua
print(shopping[1])   # Huevos
print(shopping[-1])  # Limón
```

Si accedes a un índice fuera de rango, aparece `IndexError`:

```python
print(shopping[99])  # IndexError
```

## Slicing

```python
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(shopping[1:4])
```

Resultado:

```python
['Huevos', 'Aceite', 'Sal']
```

El índice final no se incluye.

Invertir una lista mediante slicing:

```python
print(shopping[::-1])
```

## Modificar elementos

Las listas son mutables. Eso significa que podemos cambiar sus elementos:

```python
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

shopping[0] = 'Jugo'
print(shopping)
```

También podemos reemplazar un tramo completo usando slicing:

```python
shopping[1:4] = ['Atún', 'Pasta']
print(shopping)
```

En este caso se sustituyen los elementos de las posiciones 1, 2 y 3 por los nuevos valores.

## Añadir elementos

`append()` añade al final:

```python
shopping.append("Pan")
```

`insert()` añade en una posición concreta:

```python
shopping.insert(1, "Café")
```

Diferencia:

- `append(elemento)` añade al final.
- `insert(posicion, elemento)` añade en una posición.

## Extender una lista

```python
numeros = [1, 2]
numeros.extend([3, 4])
print(numeros)  # [1, 2, 3, 4]
```

`extend()` modifica la lista original.

## Borrar elementos

Por posición con `del`:

```python
lista = ['Agua', 'Huevos', 'Aceite', 'Sal']
del lista[2]
print(lista)
```

Por valor con `remove()`:

```python
lista.remove('Sal')
print(lista)
```

Eliminar y devolver con `pop()`:

```python
ultimo = lista.pop()
print(ultimo)
print(lista)
```

- `del` borra un elemento o un tramo, pero no devuelve nada.
- `pop()` elimina un elemento y sí devuelve el valor eliminado.

Vaciar una lista:

```python
lista.clear()
print(lista)
```

Si solo quieres volver a empezar con otra lista vacía, también puedes hacer:

```python
lista = []
```

## Operador `*`

```python
print(['A'] * 3)
```

Resultado:

```python
['A', 'A', 'A']
```

## Longitud, pertenencia e índice

```python
shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

print(len(shopping))
print('Aceite' in shopping)
print('Pollo' in shopping)
print(shopping.index('Aceite'))
```

- `len(lista)` devuelve cuántos elementos tiene.
- `valor in lista` comprueba si el elemento está en la lista.
- `index(valor)` devuelve la posición de la primera coincidencia.

Si el valor no existe, `index()` produce `ValueError`.

## Recorrer listas

```python
for alumno in alumnos:
    print(alumno)
```

Con índice:

```python
for indice, alumno in enumerate(alumnos):
    print(indice, alumno)
```

Con índice inicial 10:

```python
print(list(enumerate(['a', 'b'], 10)))
```

Resultado:

```python
[(10, 'a'), (11, 'b')]
```

## Ordenar listas

`sorted(lista)` devuelve una nueva lista ordenada:

```python
numeros = [3, 1, 2]
ordenada = sorted(numeros)
print(ordenada)
print(numeros)
```

`lista.sort()` modifica la lista original:

```python
numeros.sort()
print(numeros)
```

## Tuplas

Una tupla es parecida a una lista, pero inmutable:

```python
coordenada = (10, 20)
```

Se usan cuando queremos agrupar valores que no deberían cambiar.

```python
alumno = ("Ana", 20)
```

## Antes del cuestionario comprueba que sabes...

- Crear listas.
- Saber que permiten duplicados.
- Usar índices y slicing.
- Modificar elementos individuales y tramos con slicing.
- Diferenciar `append()`, `insert()` y `extend()`.
- Diferenciar `del`, `remove()`, `pop()` y `clear()`.
- Entender `lista * n`.
- Usar `len()`, `in` e `index()`.
- Usar `sorted()` y `sort()`.
- Usar `enumerate()`.
- Saber qué es una tupla.
