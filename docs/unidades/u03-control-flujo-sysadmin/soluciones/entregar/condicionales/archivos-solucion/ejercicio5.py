# Preparar carpeta de logs 
#Pistas: librería pathlib, librería os 
#Obtén el directorio actual con la clase Path de la librería pathlib 
# e imprímelo por pantalla.  
# Obtén su contenido con la función listdir de la librería os 
# e imprime por pantalla. 
# A continuación,  comprueba si existe la carpeta "logs" en el directorio actual.
# Para ello, monta tú mismo la ruta para que sea de tipo Path. 
#- Si no existe, créala y muestra "Carpeta creada". 
#- Si existe, muestra "Carpeta ya existe". 

from pathlib import Path
import os

dir_actual = Path.cwd()
print("Directorio actual: ", dir_actual)

contenido = os.listdir(dir_actual)
print("Contenido: ", contenido)


ruta_logs = dir_actual / "logs"

if not ruta_logs.exists():
    ruta_logs.mkdir()
    print("Carpeta creada:", ruta_logs)
else:
    print("Carpeta ya existe:", ruta_logs)
