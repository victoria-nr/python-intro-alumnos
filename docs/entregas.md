# Entregas del curso: repositorio privado de ejercicios

Durante el curso usarás un repositorio privado como **cuaderno de programación y portfolio**. Allí guardarás los ejercicios de todas las unidades y el historial de tu trabajo mediante commits.

!!! info "Si es tu primera vez con Git"
    Lee primero [Tutorial previo: Git y GitHub para tu repositorio de entregas](git-github-entregas.md). Explica los comandos y cómo trabajar con ramas y Pull Requests.

!!! warning "Regla principal de las entregas"
    **Cada bloque se trabaja en una rama independiente creada desde `main`. Al terminarlo, se abre una Pull Request hacia `main` y se añade al profesor como revisor.** No hagas merge hasta que el profesor te lo indique.

## 1. Cómo trabajaremos

- El repositorio de apuntes es público y sirve para consultar teoría, enunciados y soluciones publicadas.
- Tu repositorio de entregas será privado y personal.
- Debes invitar al profesor como colaborador.
- Cada unidad tiene su carpeta y debes guardar cada ejercicio en la ubicación correspondiente.
- Haz commits frecuentes y descriptivos.
- Cada bloque de trabajo tiene su propia rama y su propia PR.
- **Puedes empezar otro bloque aunque el profesor todavía no haya revisado una PR anterior.**
- Si una PR está pendiente de revisión, las correcciones que te pida el profesor se hacen en la misma rama y en la misma PR.
- Si quieres corregir por iniciativa propia un ejercicio que ya se fusionó en `main`, sigue el procedimiento del apartado 8.

No entregues ejercicios modificando el repositorio público de apuntes.

## 2. Crear el repositorio desde la plantilla

1. Entra en el repositorio plantilla indicado por el profesor. Para Introducción a la Programación en Python: https://github.com/victoria-nr/python-intro-entregas-template
2. Pulsa **Use this template** y después **Create a new repository**.
3. Ponle el nombre que indique el profesor, por ejemplo:

```text
python-intro-entregas-nombre-apellido
```

4. Marca el repositorio como **Private** y créalo.

## 3. Invitar al profesor

1. Entra en tu repositorio privado de GitHub.
2. Ve a **Settings → Collaborators** o **Collaborators and teams**.
3. Pulsa **Add people**, busca el usuario del profesor y envía la invitación.

El profesor indicará en clase cuál es su usuario de GitHub.

## 4. Clonar tu repositorio

Copia la URL de tu repositorio y clónalo en tu ordenador. Esto se hace una sola vez:

```bash
git clone URL_DE_TU_REPOSITORIO
cd NOMBRE_DE_TU_REPOSITORIO
```

Abre esa carpeta con Visual Studio Code.

## 5. Estructura del repositorio

Tu repositorio tendrá una estructura similar a esta:

```text
python-intro-entregas-nombre-apellido/
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
│   └── ...
└── .github/
    └── workflows/
        └── tests.yml
```

Cada unidad tiene su carpeta. Dentro de `ejercicios/`, existen 2 bloques de ejercicios,  `practicar` y  `entregar`, en sus carpetas correspondientes. No mezcles ejercicios de unidades o bloques distintos.

Para cada bloque, crearemos una nueva rama que partirá desde `main`. Esa rama tendrá el nombre de la unidad y bloque correspondiente. Por ejemplo, en la unidad 1 crearemos las ramas  `u01-introduccion-python-practicar` y `u01-introduccion-python-entregar`, en la unidad 2 crearemos las ramas `u02-objetos-cadenas-practicar` y `u02-objetos-cadenas-entregar`, etc.

A continuación, se explica con detalle el procedimiento para cada bloque.

## 6. Procedimiento para cada bloque

Sigue siempre estos pasos en el mismo orden. Los ejemplos usan el bloque `u01-introduccion-python-practicar`; adapta el nombre al bloque que estés haciendo.

### 1. Comprueba el estado y actualiza `main`

```bash
git status
git switch main
git pull
```

Si `git status` muestra cambios sin guardar en un commit, no cambies de rama sin comprobar primero a qué trabajo pertenecen. Si son del bloque actual, haz commit y push antes de continuar.

### 2. Crea una rama nueva desde `main`

```bash
git switch -c u01-introduccion-python-practicar
```

Usa un nombre distinto para cada bloque, por ejemplo `u01-introduccion-python-entregar` para el bloque de ejercicios de la carpeta entregar.

**No crees la rama nueva desde la rama en la que estabas trabajando. Vuelve siempre a `main` antes de crear una rama para un bloque nuevo.**

Si vas a continuar un bloque cuya PR sigue abierta, vuelve a la rama de ese bloque; no crees una segunda rama ni una PR nueva para el mismo trabajo.

### 3. Trabaja en la carpeta correcta y haz commits

Por ejemplo:

```text
unidades/u01-introduccion-python/ejercicios/practicar/
```

Cuando completes una parte del trabajo:

```bash
git status
git add .
git commit -m "Completa ejercicio 1 del bloque practicar de la unidad 1"
```

Ejemplos de mensajes claros:

```text
Completa ejercicio 1 de practicar de la unidad 1
Corrige entregable 1 de cadenas
Añade pruebas del ejercicio 16 de glob
Completa la reflexión de la unidad 1
```

Evita mensajes como `cosas`, `final`, `ejercicios` o `cambios`.

### 4. Sube la rama a GitHub

La primera vez que subes esa rama:

```bash
git push -u origin u01-introduccion-python-practicar
```

En los siguientes envíos de esa misma rama:

```bash
git push
```

### 5. Abre una Pull Request hacia `main`

Cuando termines el bloque:

1. Entra en tu repositorio en GitHub.
2. Pulsa **Compare & pull request** si aparece. Si no, ve a **Pull requests → New pull request**.
3. Comprueba que la rama base o destino es `main` y que la rama de origen es la del bloque terminado.
4. En **Files changed**, comprueba que aparecen los archivos que corresponden a esa entrega y no los de otros bloques.
5. En el panel **Reviewers**, selecciona al profesor.
6. En el título y la descripción, indica qué bloque entregas, qué ejercicios incluye y si has usado IA y para qué.
7. Pulsa **Create pull request**.

No hagas merge por tu cuenta. Espera a que el profesor te lo indique.

### 6. Si el profesor solicita cambios

No crees otra rama ni otra PR. Corrige el trabajo en la misma rama, haz commit y ejecuta `git push`. La PR se actualizará automáticamente. Déjala abierta hasta que el profesor te indique qué hacer.

## 7. ¿Puedo empezar otro bloque mientras tengo una PR pendiente?

**Sí. No tienes que esperar a que el profesor revise o fusione la PR anterior.** Puedes tener varias PR pendientes y seguir trabajando.

Para empezar el siguiente bloque, crea otra rama desde `main`:

```bash
git switch main
git pull
git switch -c NOMBRE_DEL_SIGUIENTE_BLOQUE
```

La rama nueva incluirá lo que haya en `main` en ese momento. Si una PR anterior aún no se ha fusionado, sus cambios todavía no estarán en `main`. No copies esos cambios a la nueva rama.

Procura que cada bloque trabaje en archivos diferentes. Si dos ramas modifican el mismo archivo, puede aparecer un conflicto al fusionar una PR. Si ocurre y no sabes resolverlo, no borres archivos ni uses `git push --force`: pide ayuda al profesor y muestra la salida de `git status` y el mensaje de error.

## 8. ¿Cómo corrijo un ejercicio que ya se fusionó en `main`?

Si la PR del ejercicio ya se fusionó y después quieres corregirlo —por ejemplo, porque has consultado la solución publicada por el profesor—, **haz la corrección directamente en `main`**. No recuperes la rama antigua ni abras otra PR solo por esa corrección.

Antes de empezar, asegúrate de haber guardado en commits y subido a GitHub el trabajo que tengas en la rama actual.

```bash
git status
git switch main
git pull
```

Corrige el ejercicio y guarda la corrección:

```bash
git add RUTA_DEL_ARCHIVO
git commit -m "Corrige ejercicio 3 de la unidad 1 del bloque entregar"
git push
```

Después, vuelve a la rama en la que estabas trabajando:

```bash
git switch NOMBRE_DE_TU_RAMA_ACTUAL
```

**Ten en cuenta:** la corrección hecha en `main` no aparece automáticamente en las ramas que ya habías creado. Si afecta a un archivo distinto del que estás modificando en tu bloque actual, normalmente podrás seguir trabajando. Si afecta al mismo archivo o aparece un conflicto, detente y consulta al profesor.

Esta norma es para corregir ejercicios que ya se habían fusionado. Si el profesor te ha pedido cambios en una PR que sigue abierta, hazlos en la rama de esa PR, no directamente en `main`.

## 9. Completar la reflexión de cada unidad

Cada unidad tiene un archivo `reflexion.md`. Complétalo antes de dar por terminada la unidad, es decir, en la última rama de la unidad, no hace falta en cada rama. Indica:

- qué ejercicios has hecho;
- qué dificultades has tenido;
- cómo has probado tus programas;
- si has usado IA y para qué;
- qué parte del código sabes explicar mejor y cuál te ha costado más.

Ejemplo:

```md
He completado los ejercicios 1, 2, 3 y 4 de la unidad.

La principal dificultad ha sido entender que input() devuelve texto y que, para hacer operaciones matemáticas, necesitaba convertir ese texto con int() o float().

He probado los programas con varios valores distintos.

He usado IA para entender un error de conversión de tipos. Después he corregido el código y he comprobado que funcionaba.
```

## 10. Normas sobre el uso de IA

Puedes usar IA para pedir explicaciones, entender errores, comparar soluciones, obtener ejemplos parecidos, mejorar comentarios o repasar conceptos. No debes entregar código que no entiendes.

Normas obligatorias:

1. Debes entender todo el código que entregas.
2. Debes poder explicarlo oralmente o por escrito.
3. Debes indicar en `reflexion.md` si has usado IA y para qué.
4. No se aceptará una entrega que no puedas modificar o explicar.
5. Debes mantener un historial de commits razonable.

## 11. Defensa del trabajo

El profesor podrá pedirte en cualquier momento que expliques tu código, modifiques una parte o resuelvas una variante sencilla. Una entrega no se considera válida si no puedes explicar razonablemente lo que has subido.

## 12. Actualizar el repositorio de apuntes

El repositorio de apuntes es distinto de tu repositorio de entregas. Para actualizar los apuntes, entra en la carpeta local del repositorio de apuntes y ejecuta:

```bash
git pull
```

Recuerda:

- El repositorio de apuntes sirve para consultar teoría, enunciados y soluciones publicadas.
- Tu repositorio privado sirve para entregar tu trabajo.
- No entregues ejercicios modificando el repositorio de apuntes.
