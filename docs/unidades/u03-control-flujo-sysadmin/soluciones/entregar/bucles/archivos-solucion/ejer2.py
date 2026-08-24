# Ejer2 - Tamaño total de logs (for, pathlib, condicional)
# Enunciado:
# Suma el tamaño (en bytes) de todos los ficheros '.log' del directorio actual.
# Muestra la suma y, si es mayor o igual que 1 MB, imprime 'ALTO VOLUMEN', si no, 'OK'.
# Librerías: from pathlib import Path

from pathlib import Path

carpeta = Path.cwd()
suma = 0

for elemento in carpeta.iterdir():
    if elemento.is_file():
        if str(elemento.name).endswith(".log"):
            suma = suma + elemento.stat().st_size

print("Suma de .log (bytes):", suma)
if suma >= 1_048_576:
    print("ALTO VOLUMEN")
else:
    print("OK")
