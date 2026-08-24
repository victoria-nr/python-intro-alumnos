# Ejer14 - Árbol de backups por mes y día (for anidado, pathlib)
# Enunciado:
# Pide el año (ej. 2025), el mes inicial y final (números) y el número de días a crear por mes (ej. 5).
# Crea con pathlib la estructura: backups/<AÑO>/<MM>/dia_<DD>
# Usa dos bucles for anidados (meses y días). Si existe, no pasa nada. Muestra cada ruta creada.
from pathlib import Path

año = input("Año (ej. 2025): ")
mes_ini = int(input("Mes inicial (1-12): "))
mes_fin = int(input("Mes final (1-12): "))
dias = int(input("Días a crear por mes (ej. 5): "))


base = Path.cwd() / "backups" / año

for mes in range(mes_ini, mes_fin + 1):
    mes_str = str(mes).zfill(2)
    carpeta_mes = base / mes_str
    if not carpeta_mes.exists():
        carpeta_mes.mkdir(parents=True) #parents=True significa que si las carpetas padres no están creadas se crean
    for dia in range(1, dias + 1):
        dia_str = str(dia).zfill(2)
        carpeta_dia = carpeta_mes / ("dia_" + dia_str)
        if not carpeta_dia.exists():
            carpeta_dia.mkdir()
        print("Creada:", carpeta_dia)
