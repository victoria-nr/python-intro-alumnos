# Enunciado: Crea `config.txt` con `clave=valor`, léelo y crea un diccionario con esa configuración.

# Creamos un ejemplo de config (si ya existe, se sobrescribe)
with open("config.txt", "w", encoding="utf-8") as f:
    f.write("usuario=admin\n")
    f.write("modo=produccion\n")
    f.write("puerto=8080\n")

config = {}

with open("config.txt", "r", encoding="utf-8") as f:
    for linea in f:
        clave, valor = linea.strip().split("=")
        config[clave] = valor

print(config)
