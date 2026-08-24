# Enunciado: Lee un fichero indicado por el usuario y controla si no existe.

nombre = input("Introduce el nombre del fichero a leer: ")

try:
    with open(nombre, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El fichero no existe. Revisa el nombre y la ruta.")
