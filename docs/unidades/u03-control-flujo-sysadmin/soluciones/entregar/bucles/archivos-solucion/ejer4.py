# Ejer4 - Nombres de backup para los próximos 7 días (for, datetime)
# Enunciado:
# Muestra 7 nombres de backup a partir de hoy en formato 'backup_AAAA_MM_DD.zip'.
# Librerías: from datetime import datetime, timedelta

from datetime import datetime, timedelta

hoy = datetime.now()
for i in range(0, 7):
    fecha = hoy + timedelta(days=i)
    nombre = "backup_" + fecha.strftime("%Y_%m_%d") + ".zip"
    print(nombre)
