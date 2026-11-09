#Analizar y trocear IP v4 (strip, count, find, [:]])
ip_texto = "  192.168.001.010  "

print("IP: ", ip_texto)

ip = ip_texto.strip()
num_puntos = ip.count(".")
print("Num puntos: ", num_puntos)

p1 = ip.find(".")
primer_octeto = ip[:p1]


p2 = ip.find(".", p1+1)
p3 = ip.find(".", p2+1)


ultimo_octeto = ip[p3 + 1:]

print("Primer octeto: ", primer_octeto)
print("Último octeto: ", ultimo_octeto)
