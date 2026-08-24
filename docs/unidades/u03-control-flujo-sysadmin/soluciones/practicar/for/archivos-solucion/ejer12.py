# Calcular ahorro en un año
ahorro_acum = 0.0

# Bucle para calcular el ahorro de cada mes
for mes in range(1, 13):
    ahorro_mes = float(input(f"¿Cuánto has ahorrado en el mes {mes}?: "))
    ahorro_acum += ahorro_mes
    print(f"En el mes {mes} llevas ahorrado {ahorro_acum:.2f} euros.")
