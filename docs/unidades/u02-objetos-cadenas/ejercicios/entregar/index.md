# Ejercicios entregables de cadenas

**Ejercicio 1:** Normalizar hostname de aula 

*Pista: strip y replace* 

Dado el texto  `'   pc -- aula -  07  \n'` debes convertirlo a `'PC-AULA-07'` sin usar condicionales ni bucles. Imprime el resultado. 

---

**Ejercicio 2:** Prefijo y extracción de aula y número 

*Pista: startswith, find y [:]*

Dada la etiqueta `'PC-AULA-23'`, verifica si empieza por `'PC-'` (solo muestra True o False) y extrae `'AULA'` y `'23'` usando `find` y `[:]` (troceado de cadenas). No uses condicionales; solo imprime las partes obtenidas. 

---

**Ejercicio 3:** Partes de una ruta Windows  

*Pista:  find o index y [:]* 

Dada una ruta como `'C:\\Users\\alumno\\Desktop\\proyecto'`, extrae: unidad `'C'`, usuario `'alumno'` y carpeta `'Desktop'` usando `find/index` y `[:]`. Imprime cada uno de los valores. 

---

**Ejercicio 4:** Analizar y trocear IP v4 

*Pista: strip, count, find y [:]*

Dada la IP  `'  192.168.001.010  '`: limpia bordes, cuenta puntos, extrae el primer octeto (hasta primer '.') y último octeto (desde último '.'). Imprime estos 2 octetos. 

---

**Ejercicio 5:** Fecha desde nombre de backup 

*Pista: find, [:] y replace* 

Dado un nombre de archivo llamado `'backup_2025_09_03.tar.gz'` extrae la fecha en formato `'03-09-2025'` (puedes extraer el año, mes y día y luego unirlos con guiones) e imprímela. Luego cambia a `'.zip'` el nombre del archivo original y muéstralo. 

---

**Ejercicio 6:** Partes de un email institucional 

*Pista: index/find y [:]*  

Dado el email  `'admin.redes@centro.edu'`, extrae el usuario (antes de '@'), el dominio (entre '@' y primer '.') y el tld (después del '.'). No uses bucles. 

---

**Ejercicio 7**: Password con patrón simple 

*Pista: librería string, librería random*

Genera una contraseña de 10 caracteres: 4 letras + 4 dígitos + 2 símbolos de los siguientes '!#$%&*'. Sin bucles ni condicionales. Utiliza la librería `string` para obtener las letras y los dígitos. Utiliza la librería `random` para seleccionar aleatoriamente un elemento de los anteriores (de las letras, de los números y de los símbolos especiales). 

---

**Ejercicio 8:** Username a partir de nombre y apellido 

*Pista: librería string, librería random, strip, replace, [:]* 

Vamos a generar un nombre de usuario. Dado un nombre='  Ana  ' y un apellido='  López ' genera su usuario con las primeras 3 letras del nombre + las 3 primeras letras de su apellido + dos dígitos aleatorios. Ten en cuenta que el nombre de usuario no puede tener vocales con acentos. Suponemos que sólo existen acentos en español.
