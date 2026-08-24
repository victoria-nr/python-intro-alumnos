# Programa para calcular la potencia de un número sin usar el operador de potencia.

base = float(input("Dame la base de la potencia: "))

while True:
    exponente = int(input("Dame el exponente de la potencia: "))
    if exponente >= 0:
        break
    
    print("ERROR: El exponente debe ser positivo")

potencia = 1.0

i = 1
while i <= exponente:
    potencia *= base
    i+=1

print("Potencia:", potencia)
