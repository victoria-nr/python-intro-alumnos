# Ejer15 - Contar logs por aula y PC (for anidado, pathlib)
# Enunciado:
# Pide cuántas aulas (A) y cuántos PCs por aula (P). Estructura esperada: AULA-01/PC-01 ... AULA-0A/PC-0P
# Para cada PC, si existe la carpeta, cuenta cuántos archivos .log tiene (solo nivel actual).
# Muestra total por aula y total general.
from pathlib import Path

A = int(input("Número de aulas: "))
P = int(input("PCs por aula: "))

base = Path.cwd()
total_general = 0

for a in range(1, A + 1):
    aula_nombre = "AULA-" + str(a).zfill(2)
    aula_dir = base / aula_nombre
    total_aula = 0
    for p in range(1, P + 1):
        pc_nombre = "PC-" + str(p).zfill(2)
        pc_dir = aula_dir / pc_nombre
        print("Carpeta: ", pc_dir)
        if pc_dir.exists() and pc_dir.is_dir():
            contador = 0
            for e in pc_dir.iterdir():
                if e.is_file():
                    if str(e.name).endswith(".log"):
                        contador = contador + 1
            total_aula = total_aula + contador
    print("Aula:", aula_nombre, "-> logs:", total_aula)
    total_general = total_general + total_aula

print("Total general de .log:", total_general)
