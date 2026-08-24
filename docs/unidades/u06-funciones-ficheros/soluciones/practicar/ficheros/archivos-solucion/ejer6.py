# Enunciado: Crea un fichero `nombres.txt` y guarda 5 nombres pedidos por teclado, uno por línea.

with open("nombres.txt", "w", encoding="utf-8") as f:
    for i in range(5):
        nombre = input(f"Nombre {i+1}: ")
        f.write(nombre + "\n")

print("Creado nombres.txt")
