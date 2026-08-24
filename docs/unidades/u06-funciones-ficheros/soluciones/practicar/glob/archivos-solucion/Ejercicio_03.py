# Enunciado: Busca `*.log` en `logs/` y muestra por pantalla: `nombre - tamaño_en_bytes` usando `path.stat().st_size`.
from pathlib import Path

carpeta = Path("logs")

if not carpeta.exists():
    print("No existe la carpeta 'logs'.")
else:
    for fichero in carpeta.glob("*.log"):
        tam = fichero.stat().st_size
        print(fichero.name, "-", tam, "bytes")
