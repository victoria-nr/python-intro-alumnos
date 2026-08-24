# Alerta por uso de disco
# Pistas: shutil.disk_usage, sys.argv
# Pide (por argumento) un umbral de uso de disco en porcentaje (por ejemplo, 85).
# Obtén el uso de disco de la partición raíz y muestra:
# - "ALERTA" si el porcentaje es mayor o igual que el umbral
# - "OK" en caso contrario.

import sys
import shutil

if len(sys.argv) >= 2:
    umbral = int(sys.argv[1])
else:
    umbral = 85


total, usado, libre = shutil.disk_usage("/")

porcentaje = int((usado * 100) / total)

print("Uso:", porcentaje, "%", "| Umbral:", umbral, "%")
if porcentaje >= umbral:
    print("ALERTA: uso alto de disco")
else:
    print("OK: dentro de límites")
