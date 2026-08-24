# Entregas del curso: repositorio privado de ejercicios

Durante el curso usarás un repositorio privado para entregar tus ejercicios de Python.

Ese repositorio será tu **cuaderno de programación**: ahí irás subiendo las prácticas de todas las unidades, manteniendo un historial de tu trabajo mediante commits.

!!! info "Si es tu primera vez con Git"
    Antes de seguir, lee [Tutorial previo: Git y GitHub para tu repositorio de entregas](git-github-entregas.md). Ahí tienes el vocabulario básico y el flujo de trabajo paso a paso.

## 1. Idea general

Durante el curso trabajaremos con dos repositorios diferentes:

* El **repositorio de apuntes**, que es este, será público y de solo lectura para el alumnado.
* Tu **repositorio de entregas** será privado.
* El profesor tendrá acceso a tu repositorio privado como colaborador.
* Cada unidad tendrá su propia carpeta.
* Deberás hacer commits frecuentes, no subir todo el trabajo de golpe al final.
* El profesor podrá revisar tu progreso, tus cambios, tus Pull Requests y tu historial de commits.

No debes entregar ejercicios modificando el repositorio público de apuntes. Las entregas se realizarán únicamente en tu repositorio privado personal.

---

## 2. Crear el repositorio desde la plantilla

1. Entra en el repositorio plantilla indicado por el profesor.
2. Pulsa **Use this template**.
3. Elige **Create a new repository**.
4. Ponle este nombre:

```text
python-intro-entregas-nombre-apellido
```

Ejemplo:

```text
python-intro-entregas-ana-garcia
```

5. Marca el repositorio como **Private**.
6. Crea el repositorio.

---

## 3. Invitar al profesor

Después de crear el repositorio privado, debes invitar al profesor como colaborador.

En GitHub:

1. Entra en tu repositorio privado.
2. Ve a **Settings**.
3. Entra en **Collaborators** o **Collaborators and teams**.
4. Pulsa **Add people**.
5. Busca el usuario de GitHub del profesor.
6. Envía la invitación.

El profesor indicará en clase cuál es su usuario de GitHub.

---

## 4. Clonar tu repositorio

Copia la URL de tu repositorio y clónalo en tu ordenador:

```bash
git clone URL_DE_TU_REPOSITORIO
cd python-intro-entregas-nombre-apellido
```

Abre esa carpeta con Visual Studio Code.

---

## 5. Estructura esperada del repositorio

Tu repositorio tendrá una estructura similar a esta:

```text
python-intro-entregas-ana-garcia/
├── README.md
├── PROGRESO.md
├── unidades/
│   ├── u01-introduccion-python/
│   │   ├── README.md
│   │   ├── ejercicios/
│   │   │   ├── practicar/
│   │   │   └── entregar/
│   │   └── reflexion.md
│   ├── u02-objetos-cadenas/
│   │   ├── README.md
│   │   ├── ejercicios/
│   │   │   ├── practicar/
│   │   │   └── entregar/
│   │   └── reflexion.md
│   ├── u03-control-flujo-sysadmin/
│   │   ├── README.md
│   │   ├── ejercicios/
│   │   │   ├── practicar/
│   │   │   └── entregar/
│   │   └── reflexion.md
│   ├── u04-poo-ampliacion/
│   │   ├── README.md
│   │   ├── ejercicios/
│   │   │   ├── practicar/
│   │   │   └── entregar/
│   │   └── reflexion.md
│   ├── u05-estructuras-datos/
│   │   ├── README.md
│   │   ├── ejercicios/
│   │   │   ├── practicar/
│   │   │   └── entregar/
│   │   └── reflexion.md
│   └── u06-funciones-ficheros/
│       ├── README.md
│       ├── ejercicios/
│       │   ├── practicar/
│       │   └── entregar/
│       └── reflexion.md
└── .github/
    └── workflows/
        └── tests.yml
```

Cada unidad tendrá su propia carpeta. Dentro de `ejercicios/` separarás los ejercicios de `practicar` y los de `entregar`. No mezcles ejercicios de unidades distintas ni de tipos distintos.

Por ejemplo, en la unidad 1 trabajarás en una de estas dos carpetas según el tipo de ejercicio:

```text
unidades/u01-introduccion-python/ejercicios/practicar/
unidades/u01-introduccion-python/ejercicios/entregar/
```

---

## 6. Forma de trabajo recomendada

Antes de empezar a trabajar en un bloque de ejercicios, asegúrate de estar en la rama principal y tener el repositorio actualizado:

```bash
git checkout main
git pull
```

Después, crea una rama nueva según el tipo de ejercicios que vayas a hacer:

```bash
git checkout -b u01-introduccion-python-practicar
# o
git checkout -b u01-introduccion-python-entregar
```

Trabaja en la carpeta correspondiente:

```text
unidades/u01-introduccion-python/ejercicios/practicar/
# o
unidades/u01-introduccion-python/ejercicios/entregar/
```

---

## 7. Hacer commits frecuentes

No subas todo el trabajo de golpe al final.

Haz commits pequeños cada vez que completes una parte:

```bash
git status
git add .
git commit -m "Completa ejercicio 1 de la unidad 1"
git push -u origin u01-introduccion-python-practicar
```

Ejemplos de buenos mensajes de commit:

```text
Completa ejercicio 1 de practicar de la unidad 1
Corrige entregable 1 de cadenas
Añade pruebas manuales del bloque de glob
Completa reflexión de la unidad 1
```

Ejemplos de malos mensajes de commit:

```text
cosas
final
ejercicios
cambios
```

Un historial de commits razonable forma parte del trabajo. No se valorará igual una entrega construida poco a poco que una entrega subida completa en un único commit final.

---

## 8. Abrir una Pull Request

Cuando termines un bloque de ejercicios de practicar o entregar:

1. Entra en GitHub.
2. Abre una **Pull Request** desde tu rama hacia `main`.
3. En la descripción indica qué ejercicios has completado y si esa rama corresponde a `practicar` o a `entregar`.
4. Indica si has usado IA y para qué.
5. No hagas merge hasta que el profesor lo indique.

La Pull Request permite al profesor ver los cambios realizados, revisar el código y dejar comentarios si es necesario.

Mientras la Pull Request esté abierta, el profesor podrá revisarla y pedir correcciones. Si eso ocurre, debes seguir trabajando en la misma rama, hacer nuevos commits y subirlos con `git push`; la Pull Request se actualizará sola. No la cierres ni hagas merge por tu cuenta salvo que el profesor te lo indique.

Si no tienes claro cómo abrirla exactamente o cuándo reutilizar una ya abierta, consulta [Tutorial previo: Git y GitHub para tu repositorio de entregas](git-github-entregas.md#57-abre-o-actualiza-una-pull-request).

---

## 9. Completar la reflexión de cada unidad

Cada unidad tendrá un archivo llamado:

```text
reflexion.md
```

Debes completarlo antes de entregar.

En ese archivo indicarás:

* qué ejercicios has hecho;
* qué dificultades has tenido;
* cómo has probado tus programas;
* si has usado IA;
* para qué la has usado;
* qué parte del código sabes explicar mejor;
* qué parte te ha costado más.

Ejemplo de reflexión breve:

```md
He completado los ejercicios 1, 2, 3 y 4 de la unidad.

La principal dificultad ha sido entender que input() devuelve texto y que, para hacer operaciones matemáticas, necesitaba convertir ese texto con int() o float().

He probado los programas con varios valores distintos para comprobar que funcionaban correctamente.

He usado IA para que me explicara un error de conversión de tipos. Después he corregido el código y he comprobado que funcionaba.
```

---

## 10. Normas sobre el uso de IA

Puedes usar IA como apoyo para aprender, pero no para sustituir tu trabajo.

Puedes usar IA para:

* pedir una explicación;
* entender un error;
* comparar dos formas de resolver algo;
* pedir ejemplos parecidos;
* mejorar comentarios;
* repasar conceptos;
* recibir pistas cuando estés bloqueado.

No debes usar IA para entregar código que no entiendes.

Normas obligatorias:

1. Debes entender todo el código que entregas.
2. Debes poder explicarlo oralmente o por escrito.
3. Debes indicar en `reflexion.md` si has usado IA y para qué.
4. No se aceptará una entrega que no puedas modificar o explicar.
5. Es obligatorio mantener un historial de commits razonable.

Ejemplo aceptable:

```text
He usado IA para entender por qué input() devuelve texto y por qué tenía que usar int().
Después he corregido mi ejercicio y lo he probado con varias edades.
```

Ejemplo aceptable:

```text
He usado IA para que me explicara por qué fallaba un input numérico.
Después he adaptado la solución y he probado el programa con tres casos distintos.
```

Ejemplo no aceptable:

```text
Le he pedido a la IA que hiciera todos los ejercicios y he copiado el código.
```

---

## 11. Defensa del trabajo

El profesor podrá pedirte en cualquier momento que expliques tu código, que modifiques una parte o que resuelvas una variante sencilla.

Una entrega no se considera válida si no puedes explicar razonablemente lo que has subido.

Por ejemplo, el profesor podrá pedirte que:

* expliques qué hace una variable concreta;
* cambies un mensaje mostrado por pantalla;
* añadas una comprobación adicional;
* modifiques un cálculo;
* corrijas un error;
* adaptes tu solución a un caso parecido.

---

## 12. Actualizar el repositorio de apuntes

El repositorio de apuntes es distinto de tu repositorio de entregas.

Para actualizar los apuntes, entra en la carpeta del repositorio de apuntes y ejecuta:

```bash
git pull
```

Recuerda:

* El repositorio de apuntes sirve para consultar teoría, ejercicios y soluciones publicadas.
* Tu repositorio privado sirve para entregar tu trabajo.
* No entregues ejercicios modificando el repositorio de apuntes.
