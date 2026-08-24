# Ejer7 - Pedir archivo hasta que exista (while, pathlib)
# Enunciado:
# Pide al usuario un nombre de archivo hasta que exista en el directorio actual.
# Cuando exista, muestra su tamaño en bytes.
# Librerías: from pathlib import Path

from pathlib import Path

while True:
    nombre = input("Archivo en el directorio actual: ")
    p = Path.cwd() / nombre
    if p.exists() and p.is_file():
        tam = p.stat().st_size
        print("Tamaño (bytes):", tam)
        break
    else:
        print("No existe. Intenta de nuevo.")
