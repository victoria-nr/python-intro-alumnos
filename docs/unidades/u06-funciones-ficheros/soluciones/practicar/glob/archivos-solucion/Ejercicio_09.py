# Enunciado: Copia todos los `*.conf` encontrados en `configs/` (recursivo) a `backup_configs/` usando `shutil.copy2`.
from pathlib import Path
import shutil

origen = Path("configs")
destino = Path("backup_configs")

if not origen.exists():
    print("No existe la carpeta 'configs'.")
else:
    destino.mkdir(exist_ok=True)

    copiados = 0
    for fichero in origen.rglob("*.conf"):
        destino_fichero = destino / fichero.name
        shutil.copy2(fichero, destino_fichero)
        copiados += 1

    print("Copiados", copiados, "ficheros .conf a", destino)
