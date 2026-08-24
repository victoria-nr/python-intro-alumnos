# Programa para calcular el coste de transporte según el peso y la zona

peso = int(input("¿Qué peso tiene el paquete (en gramos)?: "))

if peso > 0 and peso <= 5000:
    print("1.- América del Norte")
    print("2.- América Central")
    print("3.- América del Sur")
    print("4.- Europa")
    print("5.- Asia")
    
    zona = int(input("¿A qué zona se reparte (1-5)?: "))
    
    if zona == 1:
        print(f"Coste: {peso * 24 / 100:.2f} euros.")
    elif zona == 2:
        print(f"Coste: {peso * 20 / 100:.2f} euros.")
    elif zona == 3:
        print(f"Coste: {peso * 21 / 100:.2f} euros.")
    elif zona == 4:
        print(f"Coste: {peso * 10 / 100:.2f} euros.")
    elif zona == 5:
        print(f"Coste: {peso * 18 / 100:.2f} euros.")
    else:
        print("Zona incorrecta.")
else:
    print("Peso incorrecto (no podemos transportar paquetes de más de 5Kg).")
