# Enunciado: Lee admin_log.txt y muestra cuántas líneas contiene y cuál es la última.

from pathlib import Path

ruta = Path("admin_log.txt")

if not ruta.exists():
    print("No existe admin_log.txt. Ejecuta antes el ejercicio 2.")
else:

    with open('admin_log.txt', 'r') as f:
        lineas= f.readlines()

    print("Número de líneas:", len(lineas))

    if len(lineas) > 0:
        print("Última línea:", lineas[-1])
    else:
        print("El fichero está vacío.")

