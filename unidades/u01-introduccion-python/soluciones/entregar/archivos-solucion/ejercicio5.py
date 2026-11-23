# Convertir un valor de grados Fahrenheit a grados Celsius

# Solicitar la temperatura en grados Fahrenheit
fahrenheit = float(input("Introduce la temperatura en °F: "))

# Calcular los grados Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Mostrar el resultado en grados Celsius
print(f"La temperatura es {celsius:.2f} °C.")
