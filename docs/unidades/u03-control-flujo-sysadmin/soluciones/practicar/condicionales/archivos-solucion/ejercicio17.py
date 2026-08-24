# Programa para determinar la cara opuesta de un dado de seis caras

cara = int(input("Introduce el número de la cara: "))

if cara == 1:
    print("SEIS")
elif cara == 2:
    print("CINCO")
elif cara == 3:
    print("CUATRO")
elif cara == 4:
    print("TRES")
elif cara == 5:
    print("DOS")
elif cara == 6:
    print("UNO")
else:
    print("ERROR: número incorrecto.")
