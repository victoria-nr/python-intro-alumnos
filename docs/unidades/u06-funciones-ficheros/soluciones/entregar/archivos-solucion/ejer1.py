# Enunciado: Genera un informe system_report.txt con fecha/hora, SO (platform) y CPUs (os.cpu_count()).

import platform
import os
from datetime import datetime

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
so = platform.system()
version = platform.version()
cpus = os.cpu_count()

with open("system_report.txt", "w", encoding="utf-8") as f:
    f.write("SYSTEM REPORT\n")
    f.write(f"Fecha: {fecha}\n")
    f.write(f"Sistema: {so}\n")
    f.write(f"CPUs: {cpus}\n")

print("Informe creado: system_report.txt")

