# Enunciado: Crea (si no existe) admin_log.txt y añade una línea con fecha/hora y un mensaje del usuario.

from datetime import datetime

mensaje = input("Mensaje para el log: ").strip()
fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("admin_log.txt", "a", encoding="utf-8") as f:
    f.write(f"[{fecha}] {mensaje}\n")

print("Mensaje añadido a admin_log.txt")

