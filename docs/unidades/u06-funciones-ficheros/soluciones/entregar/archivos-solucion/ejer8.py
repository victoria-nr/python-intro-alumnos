# Enunciado: Crea commands.txt y genera commands_numbered.txt numerando cada línea.

from pathlib import Path

# Comandos de ejemplo 
comandos = [
    "ls -la",
    "df -h",
    "uname -a",
    "ps aux"
]

Path("commands.txt").write_text("\n".join(comandos) + "\n", encoding="utf-8")

salida = []

with open("commands.txt", "r", encoding="utf-8") as f:
    for i, linea in enumerate(f, start=1):
        salida.append(f"{i}: {linea.rstrip()}")

with open("commands_numbered.txt", "w", encoding="utf-8") as f:
    for linea in salida:
        f.write(linea + "\n")
        
# Forma alternativa de escribir el fichero
# Path("commands_numbered.txt").write_text("\n".join(salida) + "\n", encoding="utf-8")
print("Generado commands_numbered.txt")

