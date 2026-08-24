# Enunciado: Crea un fichero llamado `saludo.txt` y escribe dentro la frase "Hola mundo".

with open("saludo.txt", "w", encoding="utf-8") as f:
    f.write("Hola mundo")

print("Creado saludo.txt")
