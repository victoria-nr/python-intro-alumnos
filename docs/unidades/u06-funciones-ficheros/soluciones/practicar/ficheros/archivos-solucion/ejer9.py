# Enunciado: Crea un fichero `log.txt` y añade (append) una línea con un mensaje y la hora actual.

from datetime import datetime

mensaje = input("Mensaje para el log: ")
hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"[{hora}] {mensaje}\n")

print(f"Añadido a log.txt [{hora}] {mensaje}")
