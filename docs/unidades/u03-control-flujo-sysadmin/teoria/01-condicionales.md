# Condicionales: tomar decisiones en un programa

## Qué vas a aprender

Hasta ahora los programas se ejecutaban casi siempre de arriba abajo. Con los condicionales, un programa puede tomar decisiones.

Un condicional permite expresar ideas como:

- si la edad es mayor o igual que 18, puede acceder;
- si la contraseña está vacía, muestra error;
- si el fichero existe, procésalo;
- si no, informa al usuario.

## `if`

```python
edad = int(input("Edad: "))

if edad >= 18:
    print("Puedes acceder")
```

La condición `edad >= 18` produce `True` o `False`. Si es `True`, se ejecuta el bloque indentado.

## La indentación es obligatoria

En Python los bloques no se marcan con llaves `{}`. Se marcan con espacios.

La convención habitual es usar **4 espacios por cada nivel de indentación**.

Correcto:

```python
if edad >= 18:
    print("Mayor de edad")
    print("Acceso permitido")
```

Incorrecto:

```python
if edad >= 18:
print("Mayor de edad")
```

La indentación forma parte de la sintaxis del lenguaje.

## `else`

```python
edad = int(input("Edad: "))

if edad >= 18:
    print("Puedes acceder")
else:
    print("No puedes acceder")
```

`else` se ejecuta cuando la condición del `if` no se cumple.

## `elif`

Cuando hay varias posibilidades, usamos `elif`:

```python
nota = float(input("Nota: "))

if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
```

Python evalúa las condiciones en orden. Cuando una se cumple, ejecuta su bloque y salta el resto.

## Operadores lógicos

Podemos combinar condiciones con `and`, `or` y `not`.

```python
edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puede entrar")
```

| Operador | Significado |
|---|---|
| `and` | deben cumplirse ambas condiciones |
| `or` | basta con que se cumpla una |
| `not` | niega una condición |

Ejemplo con `or`:

```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Fin de semana")
```

## Paréntesis

En Python no es obligatorio poner paréntesis alrededor de la condición:

```python
if edad >= 18:
    print("OK")
```

También puedes usarlos para mejorar la claridad en condiciones largas:

```python
if (edad >= 18 and tiene_entrada) or es_admin:
    print("Acceso permitido")
```

## Asignación condicional

Python permite escribir una condición en una sola línea:

```python
resultado = "apto" if nota >= 5 else "no apto"
```

Equivale a:

```python
if nota >= 5:
    resultado = "apto"
else:
    resultado = "no apto"
```

No conviene abusar de esta forma si la expresión queda difícil de leer.

## Valores verdaderos y falsos

En Python algunos valores se comportan como `False` en una condición:

```python
""      # cadena vacía
0       # cero
[]      # lista vacía
None    # ausencia de valor
```

Ejemplo:

```python
nombre = input("Nombre: ").strip()

if nombre:
    print(f"Hola, {nombre}")
else:
    print("No has escrito nada")
```

## Ejemplo aplicado a sistemas

```python
espacio_libre_gb = 3

if espacio_libre_gb < 5:
    print("Aviso: queda poco espacio libre")
else:
    print("Espacio suficiente")
```

Más adelante podremos obtener datos reales del sistema usando librerías, pero la estructura de decisión será la misma.

## Errores frecuentes

### Usar `=` en vez de `==`

```python
if edad = 18:  # Error
    print("Tiene 18")
```

Correcto:

```python
if edad == 18:
    print("Tiene 18")
```

### Olvidar los dos puntos

```python
if edad >= 18
    print("OK")
```

Correcto:

```python
if edad >= 18:
    print("OK")
```

## Antes del cuestionario comprueba que sabes...

- Usar `if`, `elif` y `else`.
- Entender que los bloques se definen por indentación.
- Usar operadores `and`, `or` y `not`.
- Diferenciar `=` y `==`.
- Escribir una asignación condicional sencilla.
- Saber que no son obligatorios los paréntesis en el `if`.
