#Normalizar hostname de aula (strip, replace)
# Enunciado:
# De '   pc -- aula -  07  \n' obtener 'PC-AULA-07' sin bucles ni condicionales.

texto = "   pc -- aula -  07  \n"
print("Texto inicial: ", texto)

limpio = texto.strip()
sin_espacios = limpio.replace(" ", "")
sin_doble = sin_espacios.replace("--", "-")

normalizado = sin_doble.upper()

print("Texto normalizado: ", normalizado)
