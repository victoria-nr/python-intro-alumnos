# Enunciado: Lee `numeros.txt` y muestra solo los números pares.

with open("numeros.txt", "r", encoding="utf-8") as f:
    for linea in f:
        numero = int(linea.strip())
        if numero % 2 == 0:
            print(numero)
