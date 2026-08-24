# Programa para calcular la potencia de un número sin usar el operador de potencia.

base = float(input("Dame la base de la potencia: "))

for _ in range(1000):
    exponente = int(input("Dame el exponente de la potencia: "))
    if exponente >= 0:
        break
    print("ERROR: El exponente debe ser positivo")

potencia = 1.0

for i in range(1, exponente + 1):
    potencia *= base

print("Potencia:", potencia)
