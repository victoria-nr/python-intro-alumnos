# Instalación del entorno

## 1. Herramientas necesarias

Para este curso usaremos:

- Python 3.
- Visual Studio Code.
- Git.
- Una cuenta de GitHub.

## 2. Python

Abre una terminal y ejecuta:

```bash
python --version
```

En algunos sistemas puede ser:

```bash
python3 --version
```

Si no tienes python instalado deberás instalarlo. Busca cómo hacerlo en fuentes oficiales según tu sistema operativo.

## 3. Git

Antes de empezar a trabajar con Git y GitHub debes instalar Git y configurar tu identidad.

### 3.1 Instalar Git

#### Ubuntu / Linux Mint

```bash
sudo apt update
sudo apt install git
```

#### Windows

Descarga e instala Git desde:

https://git-scm.com/downloads

Durante la instalación puedes dejar las opciones por defecto.

#### Comprobar la instalación

Abre una terminal y ejecuta:

```bash
git --version
```

Deberías ver una salida similar a:

```text
git version 2.43.0
```

---

### 3.2 Configurar tu nombre y correo

Git guarda en cada commit el nombre y correo de la persona que lo realiza.

Configura estos datos una sola vez:

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "tu_correo@example.com"
```

Por ejemplo:

```bash
git config --global user.name "Ana García"
git config --global user.email "ana.garcia@gmail.com"
```

Puedes comprobar la configuración con:

```bash
git config --global --list
```

---

### 3.3 Configurar autenticación SSH con GitHub

Para trabajar con GitHub utilizaremos claves SSH.

De esta forma no tendrás que introducir usuario y contraseña cada vez que hagas `push` o `pull`.

#### Comprobar si ya tienes una clave SSH

Ejecuta:

```bash
ls -la ~/.ssh
```

Si aparecen archivos como:

```text
id_ed25519
id_ed25519.pub
```

ya tienes una clave SSH creada.

Si no existen, crea una nueva.

---

#### Crear una nueva clave SSH

Ejecuta:

```bash
ssh-keygen -t ed25519 -C "tu_correo@example.com"
```

Por ejemplo:

```bash
ssh-keygen -t ed25519 -C "ana.garcia@gmail.com"
```

Cuando pregunte dónde guardar la clave, pulsa simplemente Enter.

Cuando pregunte una contraseña para la clave:

- Puedes dejarla vacía pulsando Enter.
- O establecer una contraseña adicional para mayor seguridad.

Al finalizar se crearán dos archivos:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

---

#### Iniciar el agente SSH

Ejecuta:

```bash
eval "$(ssh-agent -s)"
```

Después añade la clave:

```bash
ssh-add ~/.ssh/id_ed25519
```

---

#### Copiar la clave pública

Muestra el contenido de la clave pública:

```bash
cat ~/.ssh/id_ed25519.pub
```

Obtendrás una línea similar a:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI... ana.garcia@gmail.com
```

Copia toda la línea.

---

#### Añadir la clave a GitHub

En GitHub:

1. Haz clic sobre tu foto de perfil.
2. Ve a **Settings**.
3. Selecciona **SSH and GPG keys**.
4. Pulsa **New SSH key**.
5. Escribe un nombre descriptivo (por ejemplo: *Portátil personal*).
6. Pega la clave copiada anteriormente.
7. Pulsa **Add SSH key**.

---

#### Comprobar que funciona

Ejecuta:

```bash
ssh -T git@github.com
```

La primera vez aparecerá un mensaje similar a:

```text
Are you sure you want to continue connecting (yes/no)?
```

Escribe:

```text
yes
```

Si todo está correcto verás algo parecido a:

```text
Hi usuario! You've successfully authenticated.
```



## 4. Extensiones recomendadas de VS Code

- Python.
- Pylance.
- Ruff.
- GitHub Pull Requests and Issues.

## 5. Primer proyecto

Crea una carpeta de trabajo, ábrela con VS Code y crea un fichero:

```text
hola.py
```

Con este contenido:

```python
print("Hola, Python")
```

Ejecútalo desde la terminal:

```bash
python hola.py
```
