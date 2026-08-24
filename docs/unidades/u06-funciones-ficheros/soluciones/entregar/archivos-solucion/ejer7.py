# Enunciado: Lee users.txt y crea homes_check.txt indicando si el home existe.

from pathlib import Path

ruta = Path("users.txt")

if not ruta.exists():
    print("No existe users.txt. Ejecuta antes el ejercicio 6.")
else:
    salida = []

    with open('users.txt' , 'r') as f:

        for linea in f:
            usuario, home = linea.strip().split(",", 1)
            home_path = Path(home.strip())

            if home_path.exists() and home_path.is_dir():
                estado = "OK"
            else:
                estado = "NO existe"

            salida.append(f"{usuario.strip()} -> {home_path} -> {estado}")

    with open('homes_check.txt' , 'w') as f:
        for linea in salida:
            f.write(f'{linea}\n')
            
    
    print("Generado homes_check.txt")

