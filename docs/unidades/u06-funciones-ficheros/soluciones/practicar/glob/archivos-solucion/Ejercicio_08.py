# Enunciado: En `logs/`, busca ficheros rotados con el patrón `*.log.*` y cuenta cuántos hay.
from pathlib import Path

carpeta = Path("logs")

if not carpeta.exists():
    print("No existe la carpeta 'logs'.")
else:
    contador = 0
    for _ in carpeta.glob("*.log.*"):
        contador += 1
    print("Logs rotados encontrados:", contador)
