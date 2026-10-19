# Prefijo y extracción de aula y número (startswith, find, [:]])
hostname = "PC-AULA-23"
print("Hostname: ", hostname)

tiene_prefijo = hostname.startswith("PC-")
print("Tiene el prefijo 'PC-'?: ",  tiene_prefijo)

pos1 = hostname.find("-")
resto = hostname[pos1 + 1:]
pos2_rel = resto.find("-")
aula = resto[:pos2_rel]
numero = resto[pos2_rel + 1:]

print("Aula: ", aula)
print("Número: ", numero)
