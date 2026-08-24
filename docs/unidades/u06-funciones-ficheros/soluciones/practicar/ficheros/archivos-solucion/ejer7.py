# Enunciado: Lee `nombres.txt` y muestra cuántos nombres hay.

num = 0

with open("nombres.txt", "r", encoding="utf-8") as f:
    for _ in f:
        num += 1

    #alternativa
    #num = len(f.readlines())
print("Cantidad de nombres:", num)
