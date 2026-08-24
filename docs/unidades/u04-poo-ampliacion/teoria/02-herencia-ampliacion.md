# Ampliación: herencia y métodos estáticos

## Herencia

La herencia permite crear una clase a partir de otra. La clase hija reutiliza comportamiento de la clase padre y puede ampliarlo.

```python
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"

class Administrador(Usuario):
    def reiniciar_servicio(self):
        return "Servicio reiniciado"
```

Uso:

```python
admin = Administrador("Ana")
print(admin.saludar())
print(admin.reiniciar_servicio())
```

`Administrador` hereda `saludar()` de `Usuario`.

## Sobrescribir métodos

Una clase hija puede redefinir un método:

```python
class Invitado(Usuario):
    def saludar(self):
        return f"Soy {self.nombre}, tengo permisos limitados"
```

## Métodos estáticos

Un método estático pertenece a la clase, pero no necesita acceder a `self`.

```python
class Validador:
    @staticmethod
    def es_puerto_valido(puerto):
        return 1 <= puerto <= 65535

print(Validador.es_puerto_valido(80))
```

## Aviso didáctico

La POO puede ser muy potente, pero también añade complejidad. En este módulo priorizamos scripts claros, funciones, estructuras de datos y ficheros. Esta parte queda como ampliación.
