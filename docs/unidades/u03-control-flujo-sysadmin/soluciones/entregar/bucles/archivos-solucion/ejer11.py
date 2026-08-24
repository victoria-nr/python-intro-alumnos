# Ejer11 - Rango de IPs pares (for, condicional)
# Enunciado:
# Pide una IP base (por ejemplo '192.168.1.') y dos números: inicio y fin del último octeto.
# Muestra por pantalla las IPs con último octeto par entre ese rango (incluidos).
base = input("IP base (ej: 192.168.1.): ")
ini = int(input("Inicio: "))
fin = int(input("Fin: "))

for x in range(ini, fin + 1):
    if x % 2 == 0:
        print(base + str(x))
