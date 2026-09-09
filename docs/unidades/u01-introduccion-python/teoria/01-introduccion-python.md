# Introducción a la programación y a Python

## Qué vas a aprender

En este apartado vas a situarte: qué significa programar, por qué usamos lenguajes de programación, qué papel ocupa Python y qué ocurre de forma simplificada cuando ejecutas un programa.

Antes de escribir código conviene entender una idea básica: **programar es dar instrucciones a un ordenador para que realice una tarea**. Esas instrucciones deben estar escritas con una sintaxis concreta, porque el ordenador no interpreta frases ambiguas como una persona.

## Programar no es memorizar instrucciones

Aprender a programar no consiste en aprender de memoria muchas órdenes. Consiste en aprender a resolver problemas paso a paso.

Por ejemplo, si queremos calcular el precio final de un producto con IVA, el razonamiento podría ser:

1. Pedir o conocer el precio sin IVA.
2. Calcular el IVA.
3. Sumar el IVA al precio inicial.
4. Mostrar el resultado.

En Python podríamos escribirlo así:

```python
precio = 100
iva = precio * 0.21
precio_final = precio + iva
print(precio_final)
```

La parte importante no es solo saber escribir `print()`, sino entender el proceso completo.

## Lenguajes de alto y bajo nivel

Los ordenadores trabajan internamente con instrucciones muy cercanas al **código máquina**, formado por valores binarios que la CPU puede ejecutar. Para las personas, escribir directamente en código máquina sería muy incómodo.

Por eso usamos lenguajes más cercanos a nuestro razonamiento. Cuanto más cercano está un lenguaje al hardware, decimos que es de **bajo nivel**. Cuanto más cercano está a la forma de pensar de una persona, decimos que es de **alto nivel**.

De forma simplificada:

| Tipo de lenguaje | Característica |
|---|---|
| Código máquina | Lo ejecuta directamente la CPU |
| Ensamblador | Muy cercano al procesador |
| C | Suele considerarse de nivel medio o intermedio |
| Python | Alto nivel, legible y expresivo |

Python es un lenguaje de alto nivel. Por eso esta instrucción se entiende bastante bien incluso sin saber programar:

```python
print("Hola, mundo")
```

## Código fuente, bytecode e intérprete

Cuando escribes un programa Python, normalmente guardas un archivo con extensión `.py`. Ese archivo contiene **código fuente**.

Por ejemplo:

```python
nombre = "Ana"
print("Hola", nombre)
```

Python no ejecuta ese texto exactamente tal cual. De forma simplificada, ocurre esto:

1. Tú escribes código fuente en un archivo `.py`.
2. Python lo analiza.
3. Python genera una representación intermedia llamada **bytecode**.
4. La máquina virtual de Python interpreta ese bytecode.

Por eso se suele decir que Python es un lenguaje **interpretado**, aunque internamente exista ese paso intermedio.

De forma muy resumida, un **compilador** traduce un programa completo antes de ejecutarlo, mientras que un **intérprete** va ejecutando el código durante la ejecución del programa. En Python aparece además el **bytecode**, que actúa como código intermedio.

!!! note "Idea importante"
    Python no se compila directamente a código máquina como otros lenguajes. Normalmente se ejecuta mediante el intérprete de Python, que se encarga de procesar el código.

## Características de Python

Python se utiliza mucho para aprender programación porque tiene una sintaxis clara. Es un lenguaje de propósito general: no está pensado para una sola tarea. También se usa profesionalmente en administración de sistemas, automatización, análisis de datos, inteligencia artificial, desarrollo web, scripting, pruebas y muchas otras áreas.

Algunas características importantes:

- Es legible.
- Tiene una gran librería estándar.
- Permite escribir scripts pequeños rápidamente.
- Es multiplataforma.
- Es multiparadigma: permite programar de forma imperativa, orientada a objetos y también usar ideas funcionales.
- Tiene una comunidad enorme.
- Se puede usar desde nivel principiante hasta proyectos profesionales.

Python fue creado por Guido van Rossum y hoy se usa tanto para aprender como en empresas y servicios reales. Por ejemplo, Google ha usado Python en distintos proyectos y herramientas internas.

Para ASIR nos interesa especialmente porque permite crear pequeños programas para automatizar tareas: revisar ficheros, procesar logs, consultar rutas, organizar carpetas o comprobar información del sistema.

## Una idea importante del estilo Python

Python intenta favorecer el código claro. Esta idea aparece en el llamado **Zen de Python**, una colección de principios de estilo muy conocida entre programadores de Python.

No hace falta memorizarlo entero, pero sí quedarse con dos ideas muy útiles:

- lo simple suele ser mejor que lo complicado;
- la legibilidad importa.

Eso significa que, cuando puedas elegir, normalmente conviene escribir una solución fácil de leer y de mantener antes que una solución rebuscada.

## Primer programa

Un primer programa clásico es:

```python
print("Hola, mundo")
```

`print()` muestra información por pantalla. El texto va entre comillas porque es una cadena de texto.

También podemos mostrar varios valores:

```python
nombre = "Ana"
edad = 20
print("Nombre:", nombre)
print("Edad:", edad)
```

Salida:

```text
Nombre: Ana
Edad: 20
```

## Comentarios

Los comentarios sirven para explicar el código. Python no los ejecuta.

```python
# Precio sin IVA
precio = 100

# Cálculo del precio final
precio_final = precio * 1.21
print(precio_final)
```

Un buen comentario no debe repetir lo obvio. Este comentario aporta poco:

```python
# Suma 1 a edad
edad = edad + 1
```

Este otro puede ser más útil:

```python
# En 2030 el alumno tendrá 4 años más que en 2026
edad_2030 = edad_actual + 4
```

## Errores frecuentes al empezar

### Olvidar las comillas

```python
print(Hola)
```

Python interpreta `Hola` como si fuera el nombre de una variable. Si no existe, dará error.

Correcto:

```python
print("Hola")
```

### Escribir instrucciones con mayúsculas incorrectas

Python distingue mayúsculas y minúsculas:

```python
Print("Hola")  # Error
print("Hola")  # Correcto
```

### No leer el mensaje de error

Los errores no son enemigos. Son pistas. Cuando Python falla, suele indicar:

- el archivo;
- la línea aproximada;
- el tipo de error;
- una breve explicación.

## Cómo se aprende a programar de verdad

Aprender a programar no consiste en resolver todo a la primera. Lo normal es avanzar poco a poco, equivocarse, corregir y buscar información cuando hace falta.

Algunas ideas prácticas:

- la constancia durante semanas ayuda más que hacer mucho trabajo un solo día;
- buscar documentación, ejemplos o explicaciones en la web es parte normal del trabajo;
- pedir ayuda cuando estás bloqueado también forma parte de aprender.

## Antes del cuestionario comprueba que sabes...

- Explicar qué significa programar.
- Distinguir código fuente, bytecode e intérprete.
- Entender por qué Python es de alto nivel.
- Reconocer que Python no se compila directamente a código máquina en el uso habitual.
- Escribir y ejecutar un primer `print()`.
- Usar comentarios sencillos en un programa.
