# Invertir un número de dos cifras y descomponerlo en decenas y unidades

# Solicitar un número de dos cifras
num = int(input("Dime un número de dos cifras: "))

# Calcular decenas y unidades
decenas = num // 10  # División entera para obtener las decenas
unidades = num % 10  # Resto para obtener las unidades

# Mostrar las cifras descompuestas
print(f"Primera cifra (decenas): {decenas}")
print(f"Segunda cifra (unidades): {unidades}")

# Construir el número invertido
num_invertido = unidades * 10 + decenas
print(f"Número invertido: {num_invertido}")
