# Funciones

## Qué vas a aprender

Una función permite agrupar instrucciones bajo un nombre para reutilizarlas. Las funciones ayudan a escribir programas más claros y evitar repetir código.

## Definir una función

```python
def saludar():
    print("Hola")
```

La palabra clave para definir una función es `def`. La línea termina con dos puntos y el cuerpo va indentado.

Para ejecutarla hay que llamarla:

```python
saludar()
```

Si defines una función pero nunca la llamas, no se ejecuta.

## Orden de ejecución

Python ejecuta el archivo de arriba abajo. Si llamas a una función antes de que Python haya ejecutado su definición, obtendrás `NameError`.

```python
saludar()  # Error si Python todavía no conoce la función

def saludar():
    print("Hola")
```

Correcto:

```python
def saludar():
    print("Hola")

saludar()
```

## Parámetros

Una función puede recibir datos:

```python
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Ana")
```

`nombre` es un parámetro. `"Ana"` es el argumento que pasamos al llamar.

## Varios parámetros

```python
def sumar(a, b):
    print(a + b)

sumar(3, 4)
```

Los argumentos posicionales se asignan por orden: `a` recibe `3` y `b` recibe `4`.

## `return`

`return` devuelve un valor al punto donde se llamó la función.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(resultado)
```

Si una función no tiene `return`, devuelve `None`.

```python
def saludar():
    print("Hola")

valor = saludar()
print(valor)  # None
```

Una función también puede devolver varios valores a la vez. En realidad, Python los agrupa en una tupla:

```python
def datos():
    return 1, 2

resultado = datos()
print(resultado)
```

Resultado:

```python
(1, 2)
```

Después puedes desempaquetar esa tupla:

```python
x, y = datos()
print(x)
print(y)
```

## Diferencia entre imprimir y devolver

```python
def doble_mal(numero):
    print(numero * 2)

def doble_bien(numero):
    return numero * 2
```

La primera función muestra el resultado, pero no permite reutilizarlo fácilmente. La segunda devuelve el valor.

Usar `return` de forma explícita suele hacer el código más claro y más fácil de reutilizar.

```python
resultado = doble_bien(5)
print(resultado + 10)
```

## Argumentos por nombre

```python
def crear_usuario(nombre, activo):
    print(f"Usuario: {nombre}, activo: {activo}")

crear_usuario(nombre="Ana", activo=True)
```

Los argumentos con nombre mejoran la claridad en algunas llamadas.

También puedes mezclar argumentos posicionales y con nombre, pero el orden importa:

```python
def build_cpu(vendor, num_cores, freq):
    return f"{vendor} - {num_cores} cores - {freq} GHz"

print(build_cpu("AMD", 8, freq=2.7))
print(build_cpu(freq=2.7, vendor="AMD", num_cores=8))
```

Lo que no se puede hacer es poner argumentos posicionales después de argumentos con nombre.

## Valores por defecto

```python
def saludar(nombre="alumno"):
    print(f"Hola, {nombre}")

saludar()
saludar("Ana")
```

Los valores por defecto se calculan cuando se define la función, no cada vez que se llama.

## Argumentos mutables

Si pasas una lista o un diccionario a una función, la función puede modificar ese mismo objeto:

```python
def anadir_error(registros):
    registros.append("ERROR")

logs = ["OK"]
anadir_error(logs)
print(logs)
```

Esto ocurre porque las listas y los diccionarios son mutables.

Si no quieres modificar el original, trabaja con una copia y devuelve el resultado:

```python
def anadir_error_sin_tocar_original(registros):
    copia = registros.copy()
    copia.append("ERROR")
    return copia
```

## Error frecuente: olvidar los dos puntos

```python
def saludar()
    print("Hola")
```

Correcto:

```python
def saludar():
    print("Hola")
```

## Ejemplo aplicado

```python
def es_extension_python(nombre_archivo):
    return nombre_archivo.endswith(".py")

archivos = ["a.py", "b.txt", "c.py"]

for archivo in archivos:
    if es_extension_python(archivo):
        print(f"Archivo Python: {archivo}")
```

## Antes del cuestionario comprueba que sabes...

- Definir funciones con `def`.
- Crear funciones sin parámetros y con parámetros.
- Diferenciar parámetro y argumento.
- Usar argumentos posicionales y con nombre.
- Usar `return`.
- Saber que sin `return` se devuelve `None`.
- Saber que varios valores devueltos forman una tupla.
- Entender el desempaquetado de tuplas.
- Evitar modificar sin querer argumentos mutables.
- Reconocer errores de sintaxis en funciones.
