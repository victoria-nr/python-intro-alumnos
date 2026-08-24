# Ejercicios entregables de listas y diccionarios

## Ejercicio 1

Ejercicio 1: Muestra información del sistema operativo (sistema, versión, nodo y procesador) y almacena los datos en un diccionario. Crea una lista con los valores y muéstralos ordenados alfabéticamente.

## Ejercicio 2

Ejercicio 2: Solicita por teclado 3 nombres de usuario mediante un bucle y almacénalos en una lista. A continuación, almacena sus home directory en un diccionario usando `os.path.expanduser`. Muestra el contenido del diccionario recorriendo sus elementos.


## Ejercicio 3

Ejercicio 3: Pide al usuario 4 nombres de archivo o directorio. Usa la librería `pathlib` para determinar si existen y su tipo (fichero o directorio) y almacena esa información en un diccionario. Es decir, el diccionario debe contener para cada ruta si es archivo, directorio o si no existe. Muestra el contenido del diccionario recorriendo sus elementos.


## Ejercicio 4
Ejercicio 4: Usa `pathlib` para listar los archivos y carpetas del directorio actual y guarda esa información (si son archivo o directorio) en un diccionario, tal y como se ha hecho en el ejercicio anterior.

## Ejercicio 5
Ejercicio 5: Crea 3 nombres de carpeta que se situarán en el directorio actual en una lista y convierte a tipo `Path`. A continuación, para cada carpeta, si no existe, la creas y guarda en un diccionario si las carpetas fueron creadas o ya existían. Muestra el contenido del diccionario recorriendo sus elementos.

## Ejercicio 6
Ejercicio 6: Usa `shutil.disk_usage` para mostrar en un diccionario el espacio total, usado y libre en GB (redondeando a un decimal) de tres rutas del sistema que pedirás por teclado. Muestra el contenido del diccionario recorriendo sus elementos.


## Ejercicio 7
Ejercicio 7: Usa la librería `pathlib` para listar los usuarios en `/home`. Crea un diccionario con los nombres de cada usuario y cuántos archivos tienen en su carpeta de usuario. Muestra el contenido del diccionario recorriendo sus elementos. 

## Ejercicio 8
Ejercicio 8: Vamos a realizar un análisis de las siguientes rutas críticas del sistema:

```python
rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
```

Guarda en un diccionario si cada una existe y si es un archivo, un directorio o no existe. Muestra un informe con el sistema operativo, número de CPUs, fecha actual y el estado de cada ruta. Usa las librerías `pathlib`, `platform`, `os` y `datetime`.

## Ejercicio 9

Vas a simular la gestión de la variable de entorno PATH, que contiene varias rutas separadas por : (dos puntos). A partir de un string que representa un PATH, por ejemplo, `"/usr/local/bin:/usr/bin:/bin"` conviértelo en una lista, añade una nueva ruta al final (pídela por teclado), otra al inicio (pídela por teclado), y luego vuelve a unirlo en un solo string. Muestra cada una en una línea  y luego muestra el resultado final.

## Ejercicio 10

Un administrador de sistemas quiere automatizar la instalación de paquetes con un comando tipo:
`apt install paquete1 paquete2 paquete3`. Crea una lista con varios nombres de paquetes, por ejemplo, `["vim", "curl", "htop"]`, simula que el usuario añade uno más por teclado, y construye la cadena completa del comando `apt install ... ` a partir de la lista.
