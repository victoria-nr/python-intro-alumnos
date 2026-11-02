# Calcular el total de dinero en euros y céntimos según las monedas ingresadas

# Solicitar la cantidad de monedas de cada tipo
euro2 = int(input("Monedas de 2 euros: "))
euro1 = int(input("Monedas de 1 euro: "))
cent50 = int(input("Monedas de 50 céntimos: "))
cent20 = int(input("Monedas de 20 céntimos: "))
cent10 = int(input("Monedas de 10 céntimos: "))

# Calcular el total de euros y céntimos
total_euros = euro2 * 2 + euro1
total_centimos = cent50 * 50 + cent20 * 20 + cent10 * 10

# Convertir céntimos adicionales en euros
total_euros += total_centimos // 100
total_centimos = total_centimos % 100

# Mostrar el total en euros y céntimos
print(f"{total_euros} euros y {total_centimos} céntimos.")
