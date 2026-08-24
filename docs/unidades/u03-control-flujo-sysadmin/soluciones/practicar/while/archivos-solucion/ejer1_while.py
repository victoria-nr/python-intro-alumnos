# Calcular el factorial
resultado = 1
contador = 2

num = int(input("Dime un número: "))

while contador <= num:
    resultado *= contador
    contador += 1

print(f"El resultado es {resultado}")