# Ejer13 - Último modificado en carpeta (for, pathlib.stat)
# Enunciado:
# Recorre el directorio actual y muestra el archivo  con fecha de modificación más reciente.
# Si no hay archivos, muestra "Sin archivos".
# Librerías: from pathlib import Path
from pathlib import Path

base = Path.cwd()
ultimo_archivo = ""
ultimo_mtime = 0.0

for elem in base.iterdir():
    if elem.is_file():
        m = elem.stat().st_mtime
        print(elem.name, "fecha: ", m)
        #si el número m es mayor, el archivo es más reciente
        if m > ultimo_mtime:
            ultimo_mtime = m
            ultimo_archivo = elem.name

if ultimo_archivo != "":
    print("Archivo más reciente:", ultimo_archivo)
else:
    print("Sin archivos")
