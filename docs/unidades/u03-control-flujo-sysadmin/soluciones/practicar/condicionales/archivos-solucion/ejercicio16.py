# Programa para calcular el coste de una llamada telefónica

tiempo = int(input("¿Cuánto tiempo es la llamada (en minutos)?: "))
es_domingo = input("¿Es Domingo? (S/N): ").strip().upper()

coste = 0.0 #tipo float

if es_domingo == "N":
    turno = input("¿Qué turno: Mañana o Tarde? (M/T): ").strip().upper()

if tiempo <= 5:
    coste = tiempo * 100
elif tiempo <= 8: #minuto 6, 7 y 8 a 80 céntimos
    coste = (tiempo - 5) * 80 + 500
elif tiempo <= 10: #minuto 9 y 10 a 70 céntimos
    coste = (tiempo - 8) * 70 + 240 + 500
else: #minutos 11 y sucesivos a 50 
    coste = (tiempo - 10) * 50 + 140 + 240 + 500

if es_domingo == "S":
    coste += coste * 0.03  # 3% adicional
else:
    if turno == "M":
        coste += coste * 0.15  # 15% adicional
    elif turno == "T":
        coste += coste * 0.10  # 10% adicional

print(f"El coste de la llamada es: {coste / 100:.2f} euros.")
