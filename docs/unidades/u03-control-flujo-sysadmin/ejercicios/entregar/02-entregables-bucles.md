# Ejercicios entregables: bucles con enfoque sysadmin

## Ejercicio 1: Contar logs en el directorio

Recorre el directorio actual y cuenta cuántos archivos terminan en `.log`.

Muestra el total encontrado.

*Librerías:* `from pathlib import Path`

## Ejercicio 2: Tamaño total de logs

Recorre el directorio actual y suma el tamaño (en bytes) de todos los ficheros `.log`.

Muestra la suma y, si es mayor o igual que 1 MB, imprime `ALTO VOLUMEN`, si no, imprime `OK`.

*Librerías:* `from pathlib import Path`

## Ejercicio 3: Entrada de hostnames hasta FIN

Pide mediante un bucle `while` hostnames al usuario hasta que escriba `FIN`.

Cuenta cuántos has introducido y muestra el total al final.

No uses listas; solo un contador y cadenas.

## Ejercicio 4: Nombres de backup para los próximos 7 días

Genera mediante un bucle 7 nombres de ficheros backup a partir de hoy en formato `backup_AAAA_MM_DD.zip` e imprímelos.

Es decir, `backup_2025_11_15.zip`, `backup_2025_11_16.zip`, etc.

*Librerías:* `from datetime import datetime, timedelta`

## Ejercicio 5: Umbral de disco con intentos

Pide por teclado un umbral de uso de disco (entre 0 y 100).

Si no es válido, vuelve a pedirlo (máximo 3 intentos).

A continuación, muestra el porcentaje real de uso de la raíz `/` y dí si supera o no el umbral.

*Librerías:* `import shutil`

## Ejercicio 6: Crear carpetas de backup numeradas

Pide un número N por teclado y crea carpetas `backup_1` ... `backup_N` en el directorio actual.

Si alguna ya existe, no pasa nada. Indica para cada carpeta si la creas o si ya existía.

*Librerías:* `from pathlib import Path`

## Ejercicio 7: Pedir archivo hasta que exista

Pide al usuario un nombre de archivo hasta que exista en el directorio actual.

Cuando exista, muestra su tamaño en bytes y termina el programa.

*Librerías:* `from pathlib import Path`

## Ejercicio 8: Menú simple de administración

Muestra un menú en bucle con opciones:

1) Listar archivos del directorio actual
2) Crear carpeta 'logs'
3) Salir

Usa `while True` y condicionales para implementar cada una de las opciones.

*Librerías:* `from pathlib import Path`

## Ejercicio 9: Estructura de PCs por aula

Vamos a crear una carpeta para un aula determinada, y dentro de esa carpeta, crearemos una carpeta para cada PC.

Pide el nombre del aula (texto cualquiera) y un número de equipos M.

Crea las carpetas: `<AULA>/PC-01`, `<AULA>/PC-02` ... `<AULA>/PC-0M` utilizando la librería `pathlib`.

Usa un bucle `for` para generar los números de los PCs formateados con dos dígitos mediante la función `zfill`. 

Tanto si ya existe la carpeta como si no, debes indicarlo. En caso de que la carpeta no exista la creas.

*Librerías:* `from pathlib import Path`

## Ejercicio 10: Clasificar nombres de backup introducidos por su extensión

Pide por teclado nombres de archivos de backup hasta que el usuario introduzca `FIN`.

Cuenta cuántos terminan en `.zip` y cuántos en `.tar.gz` o `.tgz` y muéstralo al final. Cuenta también los archivos introducidos con cualquier otra extensión.

*Librerías:* `from pathlib import Path`

## Ejercicio 11: Rango de IPs pares

Pide una IP base, por ejemplo '192.168.1.' (debes incluir el punto final),  y dos números: *inicio* y *fin* del último octeto.

Muestra por pantalla las IPs con último octeto *par* entre ese rango (incluidos).


## Ejercicio 12: Validar contraseña simple con bucles

Pide una contraseña repetidamente hasta que cumpla los siguientes criterios:
- Tiene al menos 6 caracteres
- Contiene al menos un dígito

Usa un bucle `while`para repetir la contraseña y un `for` para comprobar si algún carácter es dígito.

## Ejercicio 13: Último modificado en carpeta

Recorre el directorio actual y muestra el archivo con fecha de modificación más reciente. Para ello, investiga la función `stat()` que puedes aplicar sobre los archivos.

Si no hay archivos, muestra "Sin archivos".

*Librerías:* `from pathlib import Path`

## Ejercicio 14: Árbol de backups por mes y día 

Pide el año (ej. 2025), el mes inicial y final (números del 1 al 12) y el número de días a crear por mes (ej. 5). Crea con `pathlib` la estructura de carpetas siguiente:
```
backups/<AÑO>/<MM>/dia_<DD>
``` 
Si una carpeta ya existe no pasa nada. 

Muestra por pantalla cada ruta creada.

Ejemplo de ejecución: año=2025, mes_inicial=2, mes_final=4, num_días=3 generaría la siguiente estructura de carpetas:
```
backups/2025/02/dia_01
backups/2025/02/dia_02
backups/2025/02/dia_03
backups/2025/03/dia_01
backups/2025/03/dia_02
backups/2025/03/dia_03
backups/2025/04/dia_01
backups/2025/04/dia_02
backups/2025/04/dia_03
``` 
*Librerías:* `from pathlib import Path`

## Ejercicio 15: Contar logs por aula y PC

Pide el número de aulas (A) y el número de PCs por aula (P). Las carpetas esperadas en el sistema son (es decir, ya deben existir en el sistema, no las creamos):
```
AULA-01/PC-01, AULA-01/PC-02, ..., AULA-0A/PC-0P
```

Recorre la estructura de carpetas anterior y, para cada PC, si la carpeta existe, cuenta cuántos archivos `.log` hay dentro.  

Muestra para **cada aula** el total de `.log` encontrados y el **total general** al final.

*Librerías:* `from pathlib import Path`

## Ejercicio 16: Plan de IPs por subred y host

Pide una IP base tipo `192.168.` (incluye el punto final). 

Pide el rango de subred (tercer octeto) *inicio* y *fin*, y el máximo *host* (último octeto).  

Para **cada subred**, muestra primero la **gateway** (`x.x.<subred>.1`) y luego los **hosts del 2 al máximo**, **saltando los múltiplos de 5** (no asignables).
