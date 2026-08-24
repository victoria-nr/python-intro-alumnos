# Enunciado: Lee `palabras.txt` y cuenta cuántas líneas tiene.

lineas = 0

with open("palabras.txt", "r", encoding="utf-8") as f:
    for _ in f:
        lineas += 1

print("Número de líneas:", lineas)
