# Calcular la hora de llegada a partir de la hora de salida y el tiempo de viaje en segundos

# Solicitar la hora de salida
horapartida = int(input("Hora de salida (HH): "))
minpartida = int(input("Minutos de salida (MM): "))
segpartida = int(input("Segundos de salida (SS): "))

# Solicitar el tiempo de viaje en segundos
segviaje = int(input("Tiempo que has tardado en segundos: "))

# Convertir la hora de salida a segundos
seginicial = horapartida * 3600 + minpartida * 60 + segpartida

# Sumar el tiempo del viaje en segundos
segfinal = seginicial + segviaje

# Calcular la hora, minutos y segundos de llegada
horallegada = (segfinal // 3600) % 24  # Usamos módulo 24 para mantener un formato de 24 horas
minllegada = (segfinal % 3600) // 60
segllegada = (segfinal % 3600) % 60

# Mostrar la hora de llegada
print(f"Hora de llegada: {horallegada:02}:{minllegada:02}:{segllegada:02}")
