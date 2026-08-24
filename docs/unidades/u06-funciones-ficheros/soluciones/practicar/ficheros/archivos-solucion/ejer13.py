# Enunciado: Lee `frases.txt` y muestra solo las frases que contienen la letra 'a'.

with open("frases.txt", "r", encoding="utf-8") as f:
    for linea in f:
        frase = linea.strip()
        if "a" in frase.lower():
            print(frase)
