# Enunciado: Lee el contenido de `saludo.txt` y muéstralo por pantalla.

with open("saludo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

print(contenido)
