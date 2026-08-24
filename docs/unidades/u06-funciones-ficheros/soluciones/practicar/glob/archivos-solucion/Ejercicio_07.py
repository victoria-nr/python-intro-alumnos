# Enunciado: En `inventario/`, crea un diccionario {extension: cantidad} usando `glob('*')`.
from pathlib import Path

carpeta = Path("inventario")

if not carpeta.exists():
    print("No existe la carpeta 'inventario'. Créala y añade ficheros de distintos tipos.")
else:
    conteo = {}

    for p in carpeta.glob("*"):
        if p.is_file():
            ext = p.suffix
            if ext == "":
                ext = "(sin_ext)"
            if ext not in conteo:
                conteo[ext] = 0
            conteo[ext] += 1

    print(conteo)
