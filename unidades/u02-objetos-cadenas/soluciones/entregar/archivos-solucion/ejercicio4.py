#Analizar y trocear IP v4 (strip, count, find, [:]])
ip_texto = "  192.168.001.010  "

print("IP: ", ip_texto)

ip = ip_texto.strip()
num_puntos = ip.count(".")
print("Num puntos: ", num_puntos)

p1 = ip.find(".")
primer_octeto = ip[:p1]

resto1 = ip[p1 + 1:]
p2_rel = resto1.find(".")
resto2 = resto1[p2_rel + 1:]
p3_rel = resto2.find(".")
ultimo_octeto = resto2[p3_rel + 1:]

print("Primer octeto: ", primer_octeto)
print("Último octeto: ", ultimo_octeto)
