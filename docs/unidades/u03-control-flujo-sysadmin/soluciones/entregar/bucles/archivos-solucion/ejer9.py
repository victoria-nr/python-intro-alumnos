# Ejer9 - Estructura de PCs por aula  (pathlib)
# Enunciado:
# Pide el nombre del aula (texto) y un número de equipos M.
# Crea carpetas: <AULA>/PC-01, <AULA>/PC-02 ... <AULA>/PC-0M con pathlib.
# Usa un for con range y formatea con dos dígitos.

from pathlib import Path

aula = input("Nombre del aula: ")
num = int(input("Número de PCs: "))


base = Path.cwd() / aula
if not base.exists():
    base.mkdir()

for i in range(1, num + 1):
    nombre = "PC-" + str(i).zfill(2)
    carpeta = base / nombre
    if not carpeta.exists():
        carpeta.mkdir()
        print("Creada:", carpeta)
    else:
        print("Ya existe:", carpeta)
