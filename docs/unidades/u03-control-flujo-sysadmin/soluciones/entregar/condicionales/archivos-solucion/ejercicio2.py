# Turno de backup según hora 
# Pistas: datetime
# Obtén la hora actual y muestra:
# - "Backup de mañana" si hora < 12
# - "Backup de tarde" si 12 <= hora < 20
# - "Backup nocturno" si hora >= 20
from datetime import datetime

ahora = datetime.now()
print(ahora)
hora = ahora.hour

print("Hora actual:", hora)
if hora < 12:
    print("Backup de mañana")
elif hora < 20:
    print("Backup de tarde")
else:
    print("Backup nocturno")
