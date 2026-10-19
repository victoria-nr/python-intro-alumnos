# Solicitar el nombre completo
nombre_completo = input("Escribe tu nombre completo: ")

# Imprimir en mayúsculas, minúsculas y formato título
print("Nombre en mayúsculas:", nombre_completo.upper())
print("Nombre en minúsculas:", nombre_completo.lower())
print("Nombre en formato título:", nombre_completo.title())

# Contar caracteres excluyendo espacios
caracteres_sin_espacios = len(nombre_completo.replace(" ", ""))
print("Número de caracteres (sin espacios):", caracteres_sin_espacios)
