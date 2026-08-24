# Enunciado: Cuenta cuántos ficheros `*.txt` hay dentro de `datos/` (solo esa carpeta) y muestra el total.
from pathlib import Path

carpeta = Path("datos")

if not carpeta.exists():
    print("No existe la carpeta 'datos'. Créala y añade algunos .txt para probar.")
else:
    contador = 0
    for _ in carpeta.glob("*.txt"):
        contador += 1
    print("Total .txt:", contador)
