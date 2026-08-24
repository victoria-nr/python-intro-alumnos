# Enunciado: Pide un usuario y guarda en users.txt el nombre y /home/<usuario>. Si ya existe, no lo repitas.

from pathlib import Path

usuario = input("Nombre de usuario: ").strip()

# Home "estimada" 
home = str(Path("/home") / usuario)

ruta = Path("users.txt")
usuarios_guardados = {}

if ruta.exists():
    with open('users.txt' , 'r') as f:
        for linea in f:
            partes = linea.split(",", 1)
            if len(partes) >= 1:
                usuarios_guardados[partes[0].strip()]=partes[1].strip()

if usuario in usuarios_guardados:
    print("Ese usuario ya estaba en users.txt")
else:
    with open("users.txt", "a", encoding="utf-8") as f:
        f.write(f"{usuario},{home}\n")
    print("Usuario añadido a users.txt")

