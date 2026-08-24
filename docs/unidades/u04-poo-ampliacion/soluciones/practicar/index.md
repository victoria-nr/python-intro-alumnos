# Soluciones de ampliación POO

Estas soluciones se muestran también en formato web para que puedas revisarlas desde el navegador con más contexto que una simple lista de archivos.

Los ficheros fuente correspondientes siguen estando en el repositorio público, así que después de un `git pull` también podrás abrirlos y ejecutarlos en tu equipo.

!!! note "Cómo leer estas soluciones"
    - Comprueba primero si tu clase guarda los atributos correctos.
    - Fíjate en qué comportamiento pertenece a cada método.
    - Si hay herencia, revisa qué parte se reutiliza de la clase base y qué parte se amplía.

En esta ampliación conviene fijarse en qué atributos guarda cada objeto, qué responsabilidad tiene cada método y cuándo tiene sentido reutilizar código mediante herencia.

### Ejercicio 1

Idea clave: Fíjate en cómo el constructor guarda el estado inicial del objeto y en cómo un método usa esos atributos para mostrar información.

??? example "Ver solución"
    ```python
    class Usuario:
        def __init__(self, nombre, email, activo=True):
            self.nombre = nombre
            self.email = email
            self.activo = activo

        def mostrar(self):
            print(f"{self.nombre} - {self.email} - Activo: {self.activo}")
    ```

### Ejercicio 2

Idea clave: Fíjate en cómo un método puede devolver un valor lógico a partir de un atributo ya almacenado en el objeto.

??? example "Ver solución"
    ```python
    class Equipo:
        def __init__(self, hostname, ip, sistema):
            self.hostname = hostname
            self.ip = ip
            self.sistema = sistema

        def es_linux(self):
            return self.sistema.lower() == "linux"
    ```

### Ejercicio 3

Idea clave: Fíjate en cómo `super()` reutiliza la inicialización de la clase base y deja en la subclase solo los datos y comportamientos nuevos.

??? example "Ver solución"
    ```python
    class Servidor(Equipo):
        def __init__(self, hostname, ip, sistema, servicio):
            super().__init__(hostname, ip, sistema)
            self.servicio = servicio

        def resumen(self):
            print(f"{self.hostname} ({self.ip}) ejecuta {self.servicio}")
    ```
