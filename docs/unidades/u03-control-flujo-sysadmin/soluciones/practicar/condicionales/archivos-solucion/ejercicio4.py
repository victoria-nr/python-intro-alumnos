# Algoritmo para realizar una división y manejar el caso de divisor igual a 0

dividendo = int(input("Dime el número 1: "))
divisor = int(input("Dime el número 2: "))

if divisor == 0:
    print("No puedes dividir por 0")
else:
    print("La división es", dividendo / divisor)
