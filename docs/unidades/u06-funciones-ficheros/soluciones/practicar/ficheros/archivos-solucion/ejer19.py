# Enunciado: Crea `backup.txt` copiando el contenido de `saludo.txt`.

with open("saludo.txt", "r", encoding="utf-8") as origen:
    contenido = origen.read()

with open("backup.txt", "w", encoding="utf-8") as destino:
    destino.write(contenido)

print("Copia creada en backup.txt")
