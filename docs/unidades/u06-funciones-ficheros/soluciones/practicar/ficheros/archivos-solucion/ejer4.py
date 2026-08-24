# Enunciado: Lee `numeros.txt` y calcula la suma de todos los números.

suma = 0

with open("numeros.txt", "r", encoding="utf-8") as f:
    for linea in f:
        numero = int(linea.strip())
        suma += numero

print("Suma:", suma)
