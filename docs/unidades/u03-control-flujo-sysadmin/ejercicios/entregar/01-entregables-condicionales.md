# Ejercicios entregables: condicionales con enfoque sysadmin

**Ejercicio 1:** Alerta por uso de disco 

*Pistas: shutil.disk_usage, sys.argv* 

Pide (por argumento) un umbral de uso de disco en porcentaje (por ejemplo, 85). 
Obtén el uso de disco de la raíz y muestra:

- "ALERTA" si el porcentaje es mayor o igual que el umbral 
- "OK" en caso contrario. 

---

**Ejercicio 2:** Turno de backup según hora 

*Pistas:  librería datetime* 

Vamos a organizar los backups según la hora. Obtén la hora actual y muestra: 

- "Backup de mañana" si hora < 12 
- "Backup de tarde" si 12 <= hora < 20 
- "Backup nocturno" si hora >= 20 

---

**Ejercicio 3:** Detectar SO y gestor recomendado 

*Pistas: librería platform*

Detecta e imprime el sistema operativo, la versión y el procesador del equipo en donde se ejecuta el script. A continuación, muestra el gestor de paquetes recomendado según las siguientes indicaciones: 

- Windows -> "winget" 
- Linux -> "apt" 
- macOS (Darwin) -> "brew"

Para otros sistemas, muestra "gestor no definido". 

---

**Ejercicio 4:** Validar hostname con ciertas características 

*Pistas: sys.argv*

Dado un hostname (que se pide como argumento), muestra:

- "VÁLIDO" si empieza por "PC-" y su longitud es al menos 7 
- "NO VÁLIDO" en caso contrario 

---

**Ejercicio 5:** Preparar carpeta de logs 

*Pistas: librería pathlib, librería os* 

Obtén el directorio actual con la clase Path de la librería pathlib e imprímelo por pantalla.  Obtén su contenido con la función listdir de la librería os e imprime por pantalla. A continuación,  comprueba si existe la carpeta "logs" en el directorio actual. Para ello, monta tú mismo la ruta para que sea de tipo Path. 

- Si no existe, créala y muestra "Carpeta creada". 
- Si existe, muestra "Carpeta ya existe". 

---

**Ejercicio 6:** Copiar fichero de configuración de ejemplo si falta 

*Pistas: librerías pathlib, shutil. Para trabajar con las rutas a los ficheros, utiliza la clase Path de pathlib. Para copiar ficheros, utilizar la función copy de shutil.* 

En el directorio actual, si NO existe un fichero llamado "config.ini", copia el fichero "config.example.ini" a "config.ini". Deberás comprobar también que el fichero "config.example.ini" exista, si no, muestra el mensaje “Falta el archivo de ejemplo”. Si ya existe "config.ini", muestra el mensaje "Config existente". 

---

**Ejercicio 7:** Mantenimiento en fin de semana 

*Pistas: librería datetime* 

Realiza un programa que averigue qué día de la semana es el día actual y muestre  
 "Ventana de mantenimiento" si es sábado (día 5) o domingo (día 6). En caso contrario, muestra "Operación normal". 

---

**Ejercicio 8:** Clasificar archivo según su tamaño 

*Pistas: librería sys y librería pathlib* 

Pide como argumento un nombre de archivo y averigua su tamaño. Si su tamaño es >= 1 MB muestra "GRANDE", en caso contrario "PEQUEÑO". (1 MB = 1_048_576 bytes)
