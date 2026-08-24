# Enunciado: Crea daily_backup_list.txt y genera backup_commands.txt simulando comandos cp (solo texto).

from pathlib import Path

# Lista de ejemplo (puedes editarla)
ficheros = ["saludo.txt", "numeros.txt", "config.txt"]
Path("daily_backup_list.txt").write_text("\n".join(ficheros) + "\n", encoding="utf-8")

destino = "/backup"
comandos = []

with open("daily_backup_list.txt", "r", encoding="utf-8") as f:
    for linea in f:
        nombre = linea.strip()
        if nombre != "":
            comandos.append(f"cp {nombre} {destino}/")

with open("backup_commands.txt", "w", encoding="utf-8") as f:
    for linea in comandos:
        f.write(linea + "\n")
        
#Alternativa
#Path("backup_commands.txt").write_text("\n".join(comandos) + "\n", encoding="utf-8")
print("Generado backup_commands.txt")

