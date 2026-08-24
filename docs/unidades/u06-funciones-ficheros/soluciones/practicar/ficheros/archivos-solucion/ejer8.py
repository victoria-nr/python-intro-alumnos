# Enunciado: Lee `nombres.txt` y muestra el nombre más largo.

mas_largo = ""

with open("nombres.txt", "r", encoding="utf-8") as f:
    for linea in f:
        nombre = linea.strip()
        if len(nombre) > len(mas_largo):
            mas_largo = nombre

print("Nombre más largo:", mas_largo)
