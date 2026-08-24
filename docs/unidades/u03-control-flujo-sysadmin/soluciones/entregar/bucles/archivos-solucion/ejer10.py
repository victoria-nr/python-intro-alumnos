# Ejer10 - Clasificar nombres de backup introducidos (while, pathlib.suffix)
# Enunciado:
# Pide nombres de archivos hasta 'FIN'.
# Cuenta cuántos terminan en '.zip' y cuántos en '.tar.gz' o '.tgz' y muéstralo al final.
# Librerías: from pathlib import Path
from pathlib import Path

zip_count = 0
tar_count = 0
otros_count = 0

while True:
    nombre = input("Archivo (FIN para terminar): ")
    if nombre == "FIN":
        break
    p = Path(nombre)
    # se puede utilizar también:  p.suffix
    if str(p.name).endswith(".tar.gz") or str(p.name).endswith(".tgz"):
        tar_count = tar_count + 1
    elif str(p.name).endswith(".zip"):
        zip_count = zip_count + 1
    else:
        otros_count += 1

print("ZIP:", zip_count)
print("TAR.GZ:", tar_count)
print("OTROS:", otros_count)
