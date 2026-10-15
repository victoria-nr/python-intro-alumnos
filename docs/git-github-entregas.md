# Tutorial previo: Git y GitHub para tu repositorio de entregas

Si nunca has usado Git ni GitHub, lee esta guía antes de empezar con [Entregas del curso](entregas.md).

El objetivo no es que te conviertas en experto en Git, sino que aprendas a guardar tu trabajo, trabajar en ramas separadas y entregar cada bloque para que el profesor lo revise.

!!! info "Qué hacer después"
    Cuando termines esta guía, consulta [Entregas del curso](entregas.md), donde se explican las normas que debes seguir durante el curso.

!!! warning "Tres ideas fundamentales"
    - `commit`: guarda una versión en tu ordenador.
    - `push`: sube tus commits a GitHub.
    - **Cada bloque se trabaja en una rama nueva creada desde `main` y se entrega mediante una Pull Request dirigida a `main`.**

## 1. Git y GitHub: lo mínimo que necesitas

- **Git** registra los cambios que haces en los archivos.
- **GitHub** aloja una copia de tu repositorio y permite que el profesor revise tu trabajo.
- **`main`** es la rama principal. Contiene el trabajo que ya se ha integrado.
- **Una rama** es una línea de trabajo separada para un bloque concreto.
- **Un commit** guarda un conjunto de cambios con un mensaje.
- **`push`** sube tus commits a GitHub.
- **`pull`** descarga e integra en tu rama local los cambios que ya están en GitHub.
- **Una Pull Request (PR)** solicita que se revise una rama antes de incorporar sus cambios a `main`.
- **Merge** incorpora los cambios de una rama a `main`.

No necesitas memorizar más conceptos para seguir el flujo de trabajo del curso.

## 2. Preparación inicial: se hace una sola vez

### 2.1. Crear tu repositorio desde la plantilla

1. Entra en el repositorio plantilla indicado por el profesor.
2. Pulsa **Use this template** y después **Create a new repository**.
3. Asigna el nombre que indique el profesor, por ejemplo:

```text
python-intro-entregas-nombre-apellido
```

4. Marca el repositorio como **Private**.
5. Crea el repositorio.

No uses **Fork** salvo que el profesor te lo pida expresamente.

### 2.2. Invitar al profesor como colaborador

1. Entra en tu repositorio de GitHub.
2. Ve a **Settings** y después a **Collaborators** o **Collaborators and teams**.
3. Pulsa **Add people**, busca el usuario del profesor y envía la invitación.

### 2.3. Clonar el repositorio en tu ordenador

Esto se hace una sola vez:

```bash
git clone URL_DE_TU_REPOSITORIO
cd NOMBRE_DE_TU_REPOSITORIO
```

Abre esa carpeta con Visual Studio Code. A partir de ahora, trabaja siempre dentro de esa carpeta.

## 3. El flujo de trabajo para cada bloque

**Cada bloque tiene su propia rama. Todas las ramas de bloques nuevos se crean desde `main`, nunca desde otra rama de trabajo.**

### Paso 1. Comprueba el estado del repositorio

Antes de cambiar de rama o empezar un bloque:

```bash
git status
```

Si tienes cambios sin guardar en un commit, no cambies de rama sin comprobar primero qué son. Si pertenecen al bloque en el que estás trabajando, haz commit y push antes de continuar.

### Paso 2. Actualiza `main`

```bash
git switch main
git pull
```

Así partes de la versión más reciente de `main` que tienes en GitHub.

### Paso 3. Crea una rama nueva para el bloque

Ejemplo para los ejercicios de practicar de la unidad 1:

```bash
git switch -c u01-introduccion-python-practicar
```

Ejemplo para los ejercicios de entregar:

```bash
git switch -c u01-introduccion-python-entregar
```

Usa el nombre que indique el profesor. **No crees una rama nueva desde la rama en la que estabas trabajando: vuelve primero a `main`.**

Si ya existe una rama para el mismo bloque porque la PR sigue abierta o el profesor te ha pedido corregirla, no crees otra: vuelve a esa rama y continúa allí.

### Paso 4. Trabaja en los archivos del bloque

Guarda los archivos en la carpeta de la unidad y del bloque que corresponda. No mezcles ejercicios de otros bloques.

Comprueba de vez en cuando dónde estás:

```bash
git status
```

La primera línea indica la rama actual.

### Paso 5. Haz commits frecuentes

Cuando completes una parte del trabajo:

```bash
git add .
git commit -m "Completa ejercicio 1 del bloque practicar de la unidad 1"
```

Usa mensajes que expliquen el cambio. Evita mensajes como `cosas`, `final` o `cambios`.

### Paso 6. Sube la rama a GitHub

La primera vez que subas esa rama, usa su nombre:

```bash
git push -u origin NOMBRE_DE_LA_RAMA
```

En los siguientes envíos de esa misma rama, normalmente basta con:

```bash
git push
```

Recuerda: `commit` guarda en tu ordenador; `push` sube los cambios a GitHub.

### Paso 7. Abre una Pull Request

Cuando termines el bloque:

1. Entra en tu repositorio de GitHub.
2. Pulsa **Compare & pull request** si aparece. Si no aparece, ve a **Pull requests → New pull request**.
3. Comprueba que la rama base o destino sea **`main`** y que la rama de origen sea la del bloque que acabas de terminar.
4. Revisa **Files changed**: deben aparecer únicamente los cambios que quieres entregar en ese bloque.
5. Añade al profesor como **Reviewer**.
6. Escribe un título y una descripción breves y pulsa **Create pull request**.
7. No hagas merge por tu cuenta: espera a que el profesor te lo indique.

No abras una PR nueva por cada commit. Abre una PR por bloque y rama.

## 4. ¿Tengo que esperar a que el profesor revise la PR para empezar otro bloque?

**No. Puedes empezar otro bloque mientras una o varias PR están pendientes de revisión.** No esperes a que el profesor las revise.

Para empezar el nuevo bloque:

```bash
git switch main
git pull
git switch -c NOMBRE_DEL_NUEVO_BLOQUE
```

La nueva rama parte de lo que haya en `main` en ese momento. Si una PR anterior todavía no se ha fusionado, sus cambios aún no estarán en `main`; no intentes copiar manualmente esos cambios a la nueva rama.

Organiza los bloques en archivos o carpetas diferentes siempre que sea posible. Si dos ramas modifican el mismo archivo, puede que más adelante haya que resolver un conflicto. Si GitHub informa de un conflicto que no sabes resolver, no improvises: consulta al profesor.

## 5. ¿Qué hago si el profesor pide cambios en una PR?

Si el profesor solicita cambios en una PR que sigue abierta:

1. Lee los comentarios de la revisión.
2. Cambia a la **misma rama** de esa PR.
3. Corrige los archivos y comprueba que funcionan.
4. Haz commit y push a esa misma rama:

```bash
git add .
git commit -m "Corrige comentarios de la revisión"
git push
```

La PR se actualizará automáticamente. No crees otra PR para el mismo bloque ni cierres la que ya está abierta.

Puedes tener abierta la PR de un bloque y trabajar en otra rama para un bloque posterior. Antes de cambiar entre ellas, comprueba con `git status` que sabes qué cambios tienes y en qué rama estás.

## 6. ¿Qué hago si quiero corregir un ejercicio que ya se fusionó en `main`?

Si el ejercicio ya estaba en una PR fusionada y después quieres corregirlo —por ejemplo, porque has visto la solución publicada por el profesor—, en este curso harás la corrección **directamente en `main`**. No recuperes la rama antigua ni abras otra PR solo para esa corrección.

1. Comprueba que los cambios de tu bloque actual están guardados en commits y subidos a GitHub.
2. Cambia a `main` y actualízala:

```bash
git status
git switch main
git pull
```

3. Corrige el ejercicio antiguo.
4. Guarda y sube la corrección:

```bash
git add RUTA_DEL_ARCHIVO
git commit -m "Corrige ejercicio 3 del bloque entregar de la unidad 1"
git push
```

5. Vuelve a la rama del bloque en el que estabas trabajando:

```bash
git switch NOMBRE_DE_TU_RAMA_ACTUAL
```

**Importante:** cambiar a `main` no incorpora automáticamente esa corrección a las otras ramas que ya tenías abiertas. Si la corrección afecta a un archivo distinto de los que estás modificando en tu rama actual, normalmente podrás continuar con normalidad. Si afecta al mismo archivo o aparece un conflicto, para y pide ayuda al profesor.

No hagas una corrección directamente en `main` si se trata de cambios solicitados por el profesor en una PR que todavía está abierta. En ese caso, corrige en la rama de esa PR, tal como se explica en el apartado anterior.

## 7. Problemas habituales: qué hacer

### He empezado a trabajar por error en `main`

**Si todavía no has hecho commit**, crea inmediatamente la rama correcta para conservar allí los cambios:

```bash
git switch -c NOMBRE_DEL_BLOQUE
```

Después continúa trabajando en esa rama.

**Si ya has hecho commit en `main`**, no crees una rama sin más ni ejecutes comandos para borrar commits. Detente y pide ayuda al profesor. Indica qué comandos has ejecutado y comparte la salida de `git status`.

### He creado la rama desde otra rama de trabajo

Si todavía no has hecho cambios en la rama equivocada, vuelve a `main`, actualízala y crea la rama correctamente. Si ya has trabajado en ella, no borres archivos ni commits al azar: consulta al profesor antes de reorganizarla.

### Git dice que la rama ya existe

No vuelvas a crearla. Si estás continuando el mismo bloque o corrigiendo una PR abierta, entra en esa rama:

```bash
git switch NOMBRE_DE_LA_RAMA
```

Si se trata de un bloque nuevo, utiliza un nombre nuevo y crea esa rama desde `main`.

### He hecho commit, pero no veo los cambios en GitHub

Comprueba si has hecho `push`:

```bash
git push
```

### GitHub dice que hay conflictos o no permite hacer merge

No uses `git push --force`, no borres archivos al azar y no intentes resolverlo sin entender qué ha ocurrido. Ejecuta `git status`, copia el mensaje de error y pide ayuda al profesor.

### No sé en qué rama estoy

Ejecuta:

```bash
git status
```

Comprueba la rama que aparece antes de modificar archivos o ejecutar otros comandos.

## 8. Normas para no estropear el repositorio

- Mantén privado tu repositorio de entregas.
- Trabaja en la carpeta de tu repositorio, no en la de los apuntes públicos.
- Crea una rama nueva desde `main` para cada bloque.
- Comprueba que cada PR tiene como destino `main` y contiene solo los cambios de ese bloque.
- No hagas merge de una PR sin autorización del profesor.
- No uses `git push --force` salvo que el profesor te lo indique.
- No borres ni renombres las carpetas base sin permiso.
- No subas contraseñas, tokens ni datos sensibles.

## 9. Chuleta de comandos

```bash
git status                         # Comprueba estado y rama actual
git switch main                    # Cambia a main
git pull                           # Actualiza la rama actual
git switch -c NOMBRE_DE_LA_RAMA    # Crea una rama nueva y cambia a ella
git add .                          # Prepara los cambios
git commit -m "Mensaje claro"      # Guarda los cambios en un commit
git push -u origin NOMBRE_DE_RAMA  # Publica la rama por primera vez
git push                           # Sube nuevos commits de la rama actual
```

## 10. Si necesitas ayuda

No digas solo «Git no funciona». Indica:

- qué querías hacer;
- qué comando has ejecutado;
- el mensaje de error completo;
- la salida de `git status`;
- en qué rama estabas.

Así el profesor podrá ayudarte sin arriesgar los cambios de tu repositorio.
