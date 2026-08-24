# Enunciado: Crea service.conf con clave=valor, léelo a un diccionario y consulta una clave por teclado.


# Creamos una config de ejemplo
with open("service.conf", "w", encoding="utf-8") as f:
    conf="port=8080\nmode=prod\nuser=admin\n"
    f.write(conf)


config = {}

with open("service.conf", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea == "":
            continue
        clave, valor = linea.split("=", 1)
        config[clave] = valor

clave_buscada = input("Introduce una clave (port/mode/user): ").strip()

if clave_buscada in config:
    print("Valor:", config[clave_buscada])
else:
    print("La clave no existe en service.conf")

