# Programa que imprime todos los números pares entre dos números dados por el usuario.

# Leer los números
num1 = int(input("Introduce el número 1: "))
num2 = int(input("Introduce el número 2: "))

if num1 % 2 == 1:
    num1 += 1

for num in range(num1, num2 + 1, 2):
    print(f"{num}")
