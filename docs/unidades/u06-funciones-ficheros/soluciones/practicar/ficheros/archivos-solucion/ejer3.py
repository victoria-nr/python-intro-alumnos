# Enunciado: Crea un fichero `numeros.txt` y escribe los números del 1 al 10, uno por línea.

with open("numeros.txt", "w", encoding="utf-8") as f:
    for num in range(1, 11):
        f.write(str(num) + "\n")

print("Creado numeros.txt")
