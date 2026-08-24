# Enunciado: Cuenta cuántos ficheros `*.txt` hay dentro de `datos/` (solo esa carpeta) y muestra el total.
from pathlib import Path


carpeta = Path("logs")
if not carpeta.exists():
    print("No existe la carpeta 'logs'. Créala y añade algunos .txt para probar.")
else:
    contador = 0
    for _ in carpeta.glob("*.txt"):
        contador += 1
    print("Total .txt:", contador)
