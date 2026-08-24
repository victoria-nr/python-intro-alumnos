# Enunciado: Crea `frases.txt` con 3 frases y luego muéstralas sin saltos de línea.

with open("frases.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        frase = input(f"Frase {i+1}: ")
        f.write(frase + "\n")

print("\nFrasess:")
with open("frases.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
