# Enunciado: En la carpeta `logs/`, muestra por pantalla el nombre de todos los ficheros que terminen en `*.log` usando `Path.glob()`.
from pathlib import Path

carpeta = Path("logs")

if not carpeta.exists():
    print("No existe la carpeta 'logs'. Créala y añade algunos .log para probar.")
else:
    for fichero in carpeta.glob("*.log"):
        print(fichero.name)
