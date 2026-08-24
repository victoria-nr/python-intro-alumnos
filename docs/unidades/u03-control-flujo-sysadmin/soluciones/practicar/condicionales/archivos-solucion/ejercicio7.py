# Algoritmo para calcular la potencia de un número considerando casos especiales

base = float(input("Dime la base: "))
exponente = int(input("Dime el exponente: "))

if exponente > 0:
    print("La potencia es", base ** exponente)
elif exponente == 0:
    print("La potencia es 1")
else:
    print("La potencia es", 1 / (base ** abs(exponente)))
