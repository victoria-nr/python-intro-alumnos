# Mantenimiento fin de semana 
#Pistas: librería datetime 
#Realiza un programa que averigue qué día de la semana es el día actual y
#  muestre  "Ventana de mantenimiento" si es sábado (día 5) o domingo (día 6). 
# En caso contrario, muestra "Operación normal". 
from datetime import datetime

dia_semana = datetime.now().weekday()  # 0=lunes ... 6=domingo

print("Día de la semana:", dia_semana)
if dia_semana >= 5:
    print("Ventana de mantenimiento")
else:
    print("Operación normal")
