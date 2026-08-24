# Programa para calcular el precio final de venta de la uva

precio_inicial = float(input("Introduce el precio inicial por kilo de la UVA (en céntimos): "))
kilos = int(input("Introduce cuántos kilos has vendido: "))
tipo = input("Introduce el tipo de la UVA (A/B): ").upper()

#if tipo not in ["A", "B"]:
if tipo != "A" and tipo != "B":
    print("Tipo incorrecto")
else:
    tamano = input("Introduce el tamaño de la UVA (1/2): ")

    #if tamano not in ["1", "2"]:
    if tamano != "1" and tamano != "2":
        print("Tamaño incorrecto")
    else:
        if tipo == "A":
            if tamano == "1":
                precio_inicial += 20
            else:  # Tamaño "2"
                precio_inicial += 30
        elif tipo == "B":
            if tamano == "1":
                precio_inicial -= 30
            else:  # Tamaño "2"
                precio_inicial -= 50

        precio_final = precio_inicial * kilos

        print(f"La ganancia es {precio_final / 100:.2f} euros.")
