# Enunciado: Busca en `temp/` ficheros `.tmp` o `.bak` y genera `cleanup_plan.txt` con las rutas (una por línea). No borres nada.
from pathlib import Path

carpeta = Path("temp")
salida = []

if not carpeta.exists():
    print("No existe la carpeta 'temp'. Créala y añade ficheros .tmp/.bak para probar.")
else:
    for fichero in carpeta.glob("*.tmp"):
        salida.append(str(fichero))
    for fichero in carpeta.glob("*.bak"):
        salida.append(str(fichero))

    with open("cleanup_plan.txt", "w", encoding="utf-8") as f:
        for ruta in salida:
            f.write(ruta + "\n")

    print("Generado cleanup_plan.txt con", len(salida), "rutas.")
