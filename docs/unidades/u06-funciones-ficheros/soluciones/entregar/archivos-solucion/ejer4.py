# Enunciado: Crea paths.txt con rutas y genera paths_status.txt indicando si cada ruta existe y su tipo.

from pathlib import Path

# Rutas de ejemplo (puedes cambiarlas)
rutas = ["/", "/home", "/var", "/tmp", "/noexiste"]

with open("paths.txt", "w", encoding="utf-8") as f:
    for r in rutas:
        f.write(r + "\n")

salida = []

with open("paths.txt", "r", encoding="utf-8") as f:
    for linea in f:
        r = linea.strip()
        p = Path(r)

        if p.exists():
            if p.is_dir():
                estado = "Directorio"
            elif p.is_file():
                estado = "Archivo"
            else:
                estado = "Otro"
        else:
            estado = "No existe"

        salida.append(f"{r} -> {estado}")

with open("paths_status.txt", "w", encoding="utf-8") as f:
    for linea in salida:
        f.write(linea + "\n")

print("Generado paths_status.txt")

