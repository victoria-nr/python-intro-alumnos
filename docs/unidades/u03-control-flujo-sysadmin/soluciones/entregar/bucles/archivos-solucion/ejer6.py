# Ejer6 - Crear carpetas de backup numeradas (for, pathlib)
# Enunciado:
# Pide un número N y crea carpetas 'backup_1' ... 'backup_N' en el directorio actual.
# Si alguna ya existe, no pasa nada.
# Librerías: from pathlib import Path

from pathlib import Path

n = int(input("¿Cuántas carpetas quieres crear? "))

base = Path.cwd()
print("Directorio base: ", base)
for i in range(1, n + 1):
    carpeta = base / ("backup_" + str(i))
    if not carpeta.exists():
        carpeta.mkdir()
        print("Creada:", carpeta.name)
    else:
        print("Ya existe:", carpeta.name)
