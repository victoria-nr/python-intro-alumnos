# Copiar fichero de configuración de ejemplo si falta 
#Pistas: librerías pathlib, shutil. Para trabajar con las rutas a los ficheros,
#  utiliza la clase Path de pathlib. Para copiar ficheros, utilizar la función copy 
# de shutil. 
#En el directorio actual, si NO existe un fichero llamado "config.ini", 
# copia el fichero "config.example.ini" a "config.ini". Deberás comprobar también 
# que el fichero "config.example.ini" exista, si no, muestra el mensaje 
# “Falta el archivo de ejemplo”. 
#Si ya existe "config.ini", muestra el mensaje "Config existente".
#  
from pathlib import Path
import shutil

ejemplo = Path.cwd() / "config.example.ini"
destino = Path.cwd() / "config.ini"

if not destino.exists():
    if ejemplo.exists():
        shutil.copy(ejemplo, destino)
        print("Copiado:", destino.name)
    else:
        print("Falta el archivo de ejemplo:", ejemplo.name)
else:
    print("Config existente")
