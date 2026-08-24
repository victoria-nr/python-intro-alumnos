# Enunciado: En `shared/`, encuentra ficheros cuyo nombre contenga espacios y muestra un aviso por pantalla.
from pathlib import Path

carpeta = Path("shared")

if not carpeta.exists():
    print("No existe la carpeta 'shared'. Créala y añade ficheros con espacios para probar.")
else:
    encontrados = 0
    for p in carpeta.glob("*"):
        if " " in p.name:
            print("Nombre con espacios:", p.name)
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron nombres con espacios.")
