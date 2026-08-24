# Enunciado: Crea `datos.csv` con 3 líneas `nombre,edad` y luego muestra cada par.

with open("datos.csv", "w", encoding="utf-8") as f:
    for _ in range(3):
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        f.write(nombre + "," + edad + "\n")

print("\nFichero creado")
print("Contenido: ")
with open("datos.csv", "r", encoding="utf-8") as f:
    for linea in f:
        nombre, edad = linea.strip().split(",")
        print("Nombre:", nombre, "- Edad:", edad)
