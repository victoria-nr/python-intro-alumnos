# Diccionarios y conjuntos

## Diccionarios

Un diccionario almacena pares **clave-valor**.

```python
alumno = {
    "nombre": "Ana",
    "edad": 20,
    "grupo": "ASIR"
}
```

Acceder a un valor:

```python
print(alumno["nombre"])
```

## Claves

Las claves deben ser de un tipo inmutable y hashable, como cadenas, números o tuplas inmutables.

```python
notas = {
    "Ana": 8,
    "Luis": 6
}
```

Las claves no pueden repetirse. Si asignas de nuevo una clave existente, se sustituye el valor:

```python
notas["Ana"] = 9
```

## Crear diccionarios vacíos

```python
datos = {}
otros_datos = dict()
```

## Acceso con corchetes y `get()`

Con corchetes:

```python
print(notas["Marta"])
```

Si la clave no existe, aparece `KeyError`.

Con `get()`:

```python
print(notas.get("Marta"))
```

Si la clave no existe, devuelve `None`.

Puedes indicar un valor por defecto:

```python
print(notas.get("Marta", "No encontrado"))
```

## Añadir y modificar

```python
notas["Marta"] = 7      # añade
notas["Ana"] = 10       # modifica
```

## `fromkeys()`

Crea un diccionario a partir de claves, asignando el mismo valor inicial:

```python
claves = ["Ana", "Luis", "Marta"]
notas = dict.fromkeys(claves, 0)
print(notas)
```

Resultado:

```python
{'Ana': 0, 'Luis': 0, 'Marta': 0}
```

## `keys()`, `values()` e `items()`

```python
print(notas.keys())
print(notas.values())
print(notas.items())
print(list(notas.items()))
```

- `keys()` devuelve las claves.
- `values()` devuelve los valores.
- `items()` devuelve pares clave-valor.
- Si conviertes `items()` con `list(...)`, obtienes una lista de tuplas `(clave, valor)`.

Recorrer un diccionario:

```python
for nombre, nota in notas.items():
    print(nombre, nota)
```

## Tamaño y pertenencia

```python
print(len(notas))
print('Ana' in notas)
print('Marta' in notas)
```

- `len(diccionario)` devuelve cuántos pares clave-valor hay.
- `clave in diccionario` comprueba si la clave existe.

## Borrar claves

Con `del`:

```python
del notas['Luis']
```

Con `pop()`:

```python
valor = notas.pop('Ana')
print(valor)
```

- `del` borra la clave.
- `pop()` borra la clave y devuelve el valor eliminado.

## Vaciar, reasignar y copiar

```python
datos = {'a': 1, 'b': 2}
alias = datos

datos.clear()
print(alias)
```

`clear()` vacía el mismo diccionario. Esto importa si otra variable apunta al mismo objeto.

Si haces esto:

```python
datos = {}
```

la variable pasa a referirse a un diccionario nuevo.

Si quieres una copia independiente, usa `copy()`:

```python
original = {'a': 1, 'b': 2}
copia = original.copy()

copia['a'] = 5
print(original)
print(copia)
```

## Combinar y actualizar diccionarios

Puedes combinar dos diccionarios en uno nuevo con `|`:

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 5, 'c': 3}

print(d1 | d2)
```

También puedes modificar uno existente con `update()`:

```python
d = {'a': 1, 'b': 2}
d.update({'a': 5, 'c': 3})
print(d)
```

## Comparar diccionarios

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)
```

Dos diccionarios son iguales si tienen el mismo contenido, aunque el orden no sea el mismo.

## `hash()` y claves hashables

Las claves deben ser hashables. Por eso una tupla puede ser clave y una lista no.

```python
print(hash(('srv', 80)))
```

`hash()` devuelve un entero que Python usa internamente para gestionar claves de diccionario de forma eficiente.

## Comprensión de diccionarios

También podemos construir diccionarios con comprensiones:

```python
longitudes = {w: len(w) for w in ('uno', 'dos')}
print(longitudes)
```

Resultado:

```python
{'uno': 3, 'dos': 3}
```

## Diccionarios anidados

Un valor de un diccionario puede ser otro diccionario:

```python
estudiantes = {
    'Ana': {'nota1': 7, 'nota2': 8, 'nota3': 9},
    'Luis': {'nota1': 5, 'nota2': 6, 'nota3': 7},
}

for nombre, notas_alumno in estudiantes.items():
    media = (notas_alumno['nota1'] + notas_alumno['nota2'] + notas_alumno['nota3']) / 3
    print(nombre, media)
```

## Conjuntos

Un conjunto guarda elementos únicos, sin duplicados.

```python
extensiones = {".py", ".txt", ".py"}
print(extensiones)
```

Los conjuntos son útiles para eliminar duplicados o comprobar pertenencia rápidamente.

```python
usuarios = ["ana", "luis", "ana"]
unicos = set(usuarios)
print(unicos)
```

## Ejemplo práctico

```python
archivos = ["a.py", "b.txt", "c.py", "d.log"]
conteo = {}

for archivo in archivos:
    extension = archivo.split(".")[-1]
    conteo[extension] = conteo.get(extension, 0) + 1

print(conteo)
```

## Antes del cuestionario comprueba que sabes...

- Crear diccionarios.
- Acceder a valores por clave.
- Saber qué pasa si una clave no existe.
- Usar `get()` con y sin valor por defecto.
- Saber que las claves no se repiten.
- Usar `fromkeys()`, `keys()` e `items()`.
- Usar `len()`, `in`, `del`, `pop()` y `clear()`.
- Diferenciar `clear()` de reasignar con `{}`.
- Combinar diccionarios con `|` y modificarlos con `update()`.
- Hacer copias con `copy()` y comparar contenido con `==`.
- Entender qué significa que una clave sea hashable.
- Reconocer una comprensión de diccionario.
- Entender para qué sirve un conjunto.
