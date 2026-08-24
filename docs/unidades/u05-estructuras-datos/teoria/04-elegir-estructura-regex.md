# Elegir estructura de datos y primera idea de expresiones regulares

## Elegir la estructura adecuada

No todas las estructuras sirven para lo mismo.

| Necesidad | Estructura recomendada |
|---|---|
| Lista ordenada de elementos modificables | `list` |
| Grupo fijo de valores | `tuple` |
| Relación clave-valor | `dict` |
| Elementos únicos sin duplicados | `set` |

Ejemplos:

```python
# Lista: varios archivos en orden
archivos = ["a.txt", "b.txt", "c.txt"]

# Tupla: coordenada que no cambia
posicion = (10, 20)

# Diccionario: contar extensiones
conteo = {"txt": 3, "py": 2}

# Conjunto: extensiones únicas
extensiones = {"txt", "py", "log"}
```

## Combinaciones

En programas reales se combinan estructuras:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 4},
]

for alumno in alumnos:
    if alumno["nota"] >= 5:
        print(f"{alumno['nombre']} ha aprobado")
```

## Expresiones regulares: idea básica

Una expresión regular es un patrón para buscar texto.

En Python se usan con el módulo `re`:

```python
import re

texto = "El servidor web01 tiene IP 192.168.1.10"
resultado = re.search(r"\d+\.\d+\.\d+\.\d+", texto)

if resultado:
    print(resultado.group())
```

No profundizaremos demasiado, pero conviene saber que existen porque son muy útiles para buscar patrones en logs, nombres de archivo o textos.

## Antes de seguir comprueba que sabes...

- Elegir entre lista, tupla, diccionario y conjunto.
- Combinar listas y diccionarios.
- Entender para qué sirve una expresión regular.
