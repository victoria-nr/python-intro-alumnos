# Enunciado: Comprueba en `proyecto/` si existe al menos un `*.py`, un `*.txt` y la carpeta `data/`.
from pathlib import Path

base = Path("proyecto")

tiene_py = False
tiene_txt = False
tiene_data = False

if not base.exists():
    print("No existe la carpeta 'proyecto'.")
else:
    for _ in base.glob("*.py"):
        tiene_py = True
        break

    for _ in base.glob("*.txt"):
        tiene_txt = True
        break

    data_dir = base / "data"
    if data_dir.exists() and data_dir.is_dir():
        tiene_data = True

    if tiene_py and tiene_txt and tiene_data:
        print("OK: estructura mínima encontrada.")
    else:
        if not tiene_py:
            print("Falta: al menos un fichero .py en proyecto/")
        if not tiene_txt:
            print("Falta: al menos un fichero .txt en proyecto/")
        if not tiene_data:
            print("Falta: la carpeta proyecto/data/")
