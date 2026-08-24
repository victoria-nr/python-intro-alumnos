# Ejer1 - Contar logs en el directorio (for, pathlib)
# Enunciado:
# Recorre el directorio actual y cuenta cuántos archivos terminan en '.log'.
# Muestra el total encontrado.
# Librerías: from pathlib import Path

from pathlib import Path

carpeta = Path.cwd()
contador = 0

for elemento in carpeta.iterdir():
    if elemento.is_file():
        nombre = str(elemento.name)
        if nombre.endswith(".log"):
            contador = contador + 1

print("Total de .log:", contador)
