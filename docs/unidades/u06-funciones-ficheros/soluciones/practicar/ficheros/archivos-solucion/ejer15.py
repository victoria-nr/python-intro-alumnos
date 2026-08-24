# Enunciado: Lee `datos.csv` y crea un diccionario {nombre: edad}. Muéstralo.

personas = {}

with open("datos.csv", "r", encoding="utf-8") as f:
    for linea in f:
        nombre, edad = linea.strip().split(",")
        personas[nombre] = int(edad)

print(personas)
