# Calcular el tiempo en minutos en que un vehículo más rápido alcanzará a otro

# Solicitar las velocidades de los vehículos y la distancia entre ellos
velocidad1 = float(input("Dime la velocidad del coche 1 (km/h): "))
velocidad2 = float(input("Dime la velocidad del coche 2 (más pequeña) (km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

# Calcular el tiempo en horas para que el vehículo más rápido alcance al otro
tiempo_horas = distancia / (velocidad1 - velocidad2)

# Convertir el tiempo a minutos
tiempo_minutos = tiempo_horas * 60

# Mostrar el resultado
print(f"Lo alcanza en {tiempo_minutos:.2f} minutos.")
