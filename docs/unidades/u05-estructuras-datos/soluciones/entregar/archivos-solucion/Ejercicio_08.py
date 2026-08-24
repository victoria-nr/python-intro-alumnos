# Ejercicio 8

'''
Vamos a realizar un análisis de las siguientes rutas críticas del sistema:
rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]
Guarda en un diccionario si cada una existe y si es un archivo, un directorio 
o no existe. Muestra un informe con el sistema operativo, número de CPUs, 
fecha actual y el estado de cada ruta. Usa las librerías `pathlib`, `platform`, 
`os` y `datetime`.'''

from pathlib import Path
import platform
import os
from datetime import datetime

rutas = ["/", "/home", "/var", "/tmp", "/usr", "/bin", "/opt", "/noexiste"]

estado_rutas = {}

for ruta_str in rutas:
    ruta = Path(ruta_str)
    if ruta.exists():
        if ruta.is_dir():
            estado_rutas[ruta_str] = "Directorio"
        elif ruta.is_file():
            estado_rutas[ruta_str] = "Archivo"
        else:
            estado_rutas[ruta_str] = "Otro tipo"
    else:
        estado_rutas[ruta_str] = "No existe"

print(f"Análisis del sistema ({platform.system()}, CPUs: {os.cpu_count()})")
print(f"Fecha del informe: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Estado rutas: ")
for ruta, estado in estado_rutas.items():
    print(f"{ruta}: {estado}")
