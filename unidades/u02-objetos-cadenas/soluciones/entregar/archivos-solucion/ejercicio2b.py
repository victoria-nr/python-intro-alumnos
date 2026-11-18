# Prefijo y extracción de aula y número (startswith, find, [:]])
hostname = "PC-AULA-23"
print("Hostname: ", hostname)

tiene_prefijo = hostname.startswith("PC-")
print("Tiene el prefijo 'PC-'?: ",  tiene_prefijo)

pos1 = hostname.find("-")
pos2 = hostname.find("-", pos1+1)
aula = hostname[pos1+1:pos2]
numero = hostname[pos2+1:]


print("Aula:", aula)
print("Número:", numero)
