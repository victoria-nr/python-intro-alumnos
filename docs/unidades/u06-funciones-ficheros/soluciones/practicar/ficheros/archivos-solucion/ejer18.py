# Enunciado: Lee `config.txt` y pregunta una clave. Si existe, muestra el valor.

config = {}

with open("config.txt", "r", encoding="utf-8") as f:
    for linea in f:
        clave, valor = linea.strip().split("=")
        config[clave] = valor

clave_buscada = input("Introduce una clave: ")

if clave_buscada in config:
    print("Valor:", config[clave_buscada])
else:
    print("La clave no existe.")
