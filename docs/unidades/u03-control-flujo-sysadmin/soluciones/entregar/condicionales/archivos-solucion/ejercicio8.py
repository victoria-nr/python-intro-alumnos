# Clasificar archivo según su tamaño 
#Pistas: librería sys y librería pathlib 
#Pide como argumento un nombre de archivo y averigua su tamaño. 
# Si su tamaño es >= 1 MB muestra "GRANDE", 
# en caso contrario "PEQUEÑO". (1 MB = 1_048_576 bytes) 

import sys
from pathlib import Path

if len(sys.argv) >= 2:
    archivo = Path(sys.argv[1].strip())
else: 
    print("No se ha dado el nombre del archivo")
    sys.exit()


size = 0
print(Path.cwd())
if archivo.exists():
    size = archivo.stat().st_size
else:
    print("El archivo ", archivo, "no existe")
    sys.exit()

print("Archivo: ", archivo) 
print("Tamaño (bytes):", size)
if size >= 1_048_576:
    print("GRANDE")
else:
    print("PEQUEÑO")
