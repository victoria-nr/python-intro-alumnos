# Convertir una cantidad de minutos en horas y minutos

# Solicitar la cantidad de minutos
minutos = int(input("Dime la cantidad de minutos: "))

# Calcular las horas y los minutos restantes
res_horas = minutos // 60  # División entera para obtener las horas
res_min = minutos % 60     # Resto para obtener los minutos sobrantes

# Mostrar el resultado
print(f"{res_horas} horas y {res_min} minutos.")
