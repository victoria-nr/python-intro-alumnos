# Ejer5 - Umbral de disco con intentos (while, shutil.disk_usage, sys.argv)
# Enunciado:
# Pide un umbral de uso de disco (0-100). Si no es válido, vuelve a pedir (máximo 3 intentos).
# Luego muestra el porcentaje real de uso del '/' y di si supera o no el umbral.
# Librerías: import shutil
import shutil

intentos = 0
umbral = -1

while intentos < 3:
    texto = input("Umbral 0-100: ")
    if texto.isdigit():
        valor = int(texto)
        if valor >= 0 and valor <= 100:
            umbral = valor
            break
    intentos = intentos + 1

total, usado, libre = shutil.disk_usage("/")
porcentaje = int((usado * 100) / total)
print("Uso:", porcentaje, "%")

if umbral >= 0 and porcentaje >= umbral:
    print("ALERTA")
elif umbral >= 0:
    print("OK")
else:
    print("Umbral no válido")
