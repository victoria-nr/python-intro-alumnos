# Enunciado: Crea `contador.txt` con un número inicial, léelo, suma 1 y vuelve a guardarlo.

from pathlib import Path

ruta = Path("contador.txt")

# Si no existe, lo inicializamos a 0
if not ruta.exists():
    with open("contador.txt", "w", encoding="utf-8") as f:
        f.write("0")


with open("contador.txt", "r", encoding="utf-8") as f:
    valor = int(f.read().strip())


valor += 1


with open("contador.txt", "w", encoding="utf-8") as f:
    f.write(str(valor))

print("Nuevo valor:", valor)
