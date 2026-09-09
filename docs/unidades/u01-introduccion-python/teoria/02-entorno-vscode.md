# Entorno de desarrollo: Python, VS Code y herramientas básicas

## Qué vas a aprender

Para programar necesitamos algo más que saber Python. También necesitamos preparar un entorno de trabajo: editor, intérprete, terminal, extensiones y, más adelante, herramientas de gestión de paquetes.

Un **entorno de desarrollo** es el conjunto de herramientas que usamos para escribir, ejecutar, probar y depurar programas.

## IDE, editor y terminal

Un IDE o entorno integrado de desarrollo suele incluir varias ayudas:

- resaltado de sintaxis;
- autocompletado;
- ejecución de programas;
- depuración paso a paso;
- explorador de archivos;
- integración con Git;
- gestión de extensiones.

Algunos entornos habituales para Python son:

| Herramienta | Uso habitual |
|---|---|
| Thonny | Muy sencilla para empezar |
| Visual Studio Code | Editor profesional, flexible y extensible |
| PyCharm | IDE especializado en Python |
| Jupyter Notebook | Cuadernos con texto, código y visualizaciones |
| Anaconda | Distribución muy usada en ciencia de datos |

En este módulo usaremos principalmente **Visual Studio Code** porque se parece más a un entorno profesional real y permite trabajar cómodamente con Git, terminal, extensiones y repositorios.

## Instalar Python

Para ejecutar código Python necesitas tener instalado el intérprete. Puedes comprobarlo en una terminal con:

```bash
python --version
```

En algunos sistemas se usa:

```bash
python3 --version
```

Si Python está instalado, verás una versión, por ejemplo:

```text
Python 3.12.4
```

## Ejecutar un archivo Python

Si tienes un archivo llamado `programa.py`, puedes ejecutarlo desde la terminal:

```bash
python programa.py
```

O, según el sistema:

```bash
python3 programa.py
```

También puedes ejecutarlo desde VS Code usando el botón de ejecución o la terminal integrada.

## Extensiones útiles de VS Code

Para trabajar con Python en VS Code conviene instalar la extensión oficial de Python. También pueden ser útiles:

- Python;
- Pylance;
- Ruff;
- extensiones de Markdown;

No necesitas dominar todas desde el primer día. Lo importante es saber crear un archivo `.py`, ejecutarlo y leer los errores.

## Entornos virtuales

Un **entorno virtual** permite aislar las librerías de un proyecto. Así cada proyecto puede tener sus propias dependencias sin mezclarlas con las de otros proyectos.

Ejemplo básico:

```bash
python -m venv .venv
```

Activación en Linux/macOS:

```bash
source .venv/bin/activate
```

Activación en Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Cuando el entorno está activo, los paquetes que instales quedarán asociados a ese proyecto.

## pip, uv, pyenv y otras herramientas

`pip` es la herramienta clásica para instalar paquetes de Python:

```bash
pip install requests
```

También existen herramientas modernas como `uv`, escrita en Rust, que permite gestionar paquetes y entornos de forma muy rápida. No es imprescindible para empezar, pero conviene que te suene porque se usa cada vez más en proyectos reales.

`pyenv` permite instalar y cambiar entre distintas versiones de Python en un mismo equipo. Es útil cuando diferentes proyectos necesitan versiones distintas.

Sobre `pyenv` existe además `pyenv-virtualenv`, que combina el cambio de versión con la gestión de entornos virtuales.

Anaconda incluye Python y muchas librerías científicas preinstaladas. Se usa mucho en ciencia de datos, notebooks y análisis numérico.

## Depurar código

Depurar es ejecutar un programa paso a paso para entender qué ocurre. En VS Code puedes poner puntos de interrupción o **breakpoints** y observar el valor de las variables.

Cuando la depuración se detiene en un punto, VS Code resalta la siguiente línea que va a ejecutarse. Suele verse con una marca amarilla, que indica por dónde continuará el programa.

Durante la depuración también es habitual mirar dos zonas:

- `VARIABLES`, para ver el valor actual de los nombres que existen en ese momento;
- `WATCH`, para vigilar expresiones concretas que quieres seguir de cerca.

También existe el depurador de terminal `pdb`:

```python
import pdb

nombre = "Ana"
pdb.set_trace()
print(nombre)
```

No lo usaremos intensivamente al principio, pero es importante saber que depurar no es probar al azar: es investigar el comportamiento del programa.

## Jupyter Notebook

Jupyter permite crear documentos que mezclan:

- texto;
- código;
- resultados;
- gráficos;
- explicaciones.

Es muy útil para análisis de datos y enseñanza, aunque en este módulo trabajaremos principalmente con archivos `.py` para practicar un flujo más parecido al desarrollo real.

## Entornos online

También existen plataformas online como Replit (antes llamada repl.it), que permiten programar y compartir proyectos desde el navegador sin instalar nada en el equipo. Son útiles para pruebas rápidas o trabajo colaborativo, aunque en este módulo usaremos sobre todo VS Code en local.

## Buenas prácticas de organización

Una carpeta de trabajo sencilla podría ser:

```text
mi-proyecto-python/
├── README.md
├── ejercicios/
│   ├── ejercicio_01.py
│   └── ejercicio_02.py
└── pruebas/
```

Evita guardar todos los archivos en el escritorio sin orden. En programación, la organización del proyecto importa.

No existe un único editor correcto para todo el mundo. Se elige según la experiencia del usuario, el tipo de proyecto y las herramientas que necesites integrar.

## Antes del cuestionario comprueba que sabes...

- Explicar qué es un entorno de desarrollo.
- Diferenciar VS Code, Thonny, PyCharm, Jupyter y Anaconda.
- Ejecutar un archivo `.py`.
- Saber para qué sirve un entorno virtual.
- Saber que `pip` instala paquetes.
- Reconocer herramientas como `uv`, `pyenv` y `pdb`.
