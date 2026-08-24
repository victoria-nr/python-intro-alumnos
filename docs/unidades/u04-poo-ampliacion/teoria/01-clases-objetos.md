# Ampliación: clases y objetos propios

## Por qué esta unidad es ampliación

La programación orientada a objetos completa corresponde al RA4, que en esta programación se trabaja principalmente en empresa. Aun así, se deja esta unidad como ampliación para alumnado que quiera avanzar.

No es necesario dominar este contenido para seguir el resto del curso, pero sí ayuda a entender mejor Python.

## Objeto y clase

Una clase es una plantilla. Un objeto es un elemento creado a partir de esa plantilla.

```python
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def esta_aprobado(self):
        return self.nota >= 5
```

Crear objetos:

```python
ana = Alumno("Ana", 8)
luis = Alumno("Luis", 4)

print(ana.nombre)
print(ana.esta_aprobado())
print(luis.esta_aprobado())
```

## Constructor `__init__`

`__init__` se ejecuta al crear el objeto. Sirve para inicializar sus datos.

```python
ana = Alumno("Ana", 8)
```

En ese momento, Python guarda:

```python
self.nombre = "Ana"
self.nota = 8
```

## Atributos y métodos

Un atributo almacena información del objeto:

```python
ana.nombre
ana.nota
```

Un método es una función asociada al objeto:

```python
ana.esta_aprobado()
```

## Ejemplo aplicado

```python
class Servidor:
    def __init__(self, nombre, activo):
        self.nombre = nombre
        self.activo = activo

    def estado(self):
        if self.activo:
            return f"{self.nombre} está activo"
        return f"{self.nombre} está inactivo"

srv1 = Servidor("web01", True)
print(srv1.estado())
```

## Antes de seguir comprueba que sabes...

- Diferenciar clase y objeto.
- Crear un constructor `__init__`.
- Usar atributos.
- Crear métodos sencillos.
- Instanciar objetos.
