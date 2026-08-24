# E04 - Validar hostname con ciertas características
#Pistas: sys.argv 
#Dado un hostname (que se pide como argumento), muestra: 
#- "VÁLIDO" si empieza por "PC-" y su longitud es al menos 7 
#- "NO VÁLIDO" en caso contrario 
import sys

if len(sys.argv) >= 2:
    hostname = sys.argv[1].strip() #"PC-AULA-23"
else:
    print("Hostname no introducido")
    sys.exit()

print("Hostname:", hostname)

if hostname.startswith("PC-") and len(hostname) >= 7:
    print("VÁLIDO")
else:
    print("NO VÁLIDO")
