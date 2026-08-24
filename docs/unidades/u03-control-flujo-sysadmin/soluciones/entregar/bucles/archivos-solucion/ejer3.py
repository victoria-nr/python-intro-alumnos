# Ejer3 - Entrada de hostnames hasta FIN (while, cadenas)
# Enunciado:
# Pide hostnames al usuario hasta que escriba 'FIN'.
# Cuenta cuántos has introducido y muestra el total al final.
# No uses listas; solo un contador y cadenas.

contador = 0
while True:
    texto = input("Hostname (FIN para terminar): ")
    if texto == "FIN":
        break
    if len(texto) > 0:
        contador = contador + 1

print("Total hostnames:", contador)
