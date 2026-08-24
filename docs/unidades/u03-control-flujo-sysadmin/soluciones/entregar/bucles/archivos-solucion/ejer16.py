# Ejer16 - Plan de IPs por subred y host (for anidado, cadenas)
# Enunciado:
# Pide base tipo '192.168.'; rango subred (tercer octeto) inicio y fin; y máximo host (último octeto).
# Para cada subred: muestra gateway x.x.<subred>.1 y luego hosts del 2 al máximo, saltando múltiplos de 5.

base = input("Base (ej. 192.168.): ")
sub_ini = int(input("Subred inicio (tercer octeto): "))
sub_fin = int(input("Subred fin (tercer octeto): "))
max_host = int(input("Máximo host (último octeto): "))

for subred in range(sub_ini, sub_fin + 1):
    print("Subred:", base + str(subred) + ".0/24")
    print("Gateway:", base + str(subred) + ".1")
    for host in range(2, max_host + 1):
        if host % 5 == 0:
            continue
        print("Host:", base + str(subred) + "." + str(host))