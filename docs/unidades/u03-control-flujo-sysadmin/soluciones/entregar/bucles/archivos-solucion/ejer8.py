# Ejer8 - Menú simple de administración (while, pathlib)
# Enunciado:
# Muestra un menú en bucle con opciones:
# 1) Listar archivos del directorio actual
# 2) Crear carpeta 'logs'
# 3) Salir
# Usa while True y condicionales.
from pathlib import Path

while True:
    print("1) Listar archivos del directorio actual")
    print("2) Crear carpeta 'logs'")
    print("3) Salir")
    op = input("Opción: ")
    if op == "1":
        for e in Path.cwd().iterdir():
            print(e.name)
    elif op == "2":
        logs = Path.cwd() / "logs"
        if not logs.exists():
            logs.mkdir()
            print("Creada carpeta 'logs'")
        else:
            print("Ya existe 'logs'")
    elif op == "3":
        print("Adiós")
        break
    else:
        print("Opción no válida")
