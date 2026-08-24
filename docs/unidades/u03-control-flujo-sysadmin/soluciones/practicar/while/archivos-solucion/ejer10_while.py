import random

# Adivina un número en 10 intentos
intentos = 10
num_secreto = random.randint(1, 100)

print("Adivina el número (de 1 a 100):")

num = int(input("Introduce un número: "))

while num_secreto != num and intentos > 1:
    if num_secreto > num:
        print("Muy bajo")
    else:
        print("Muy alto")
    
    intentos -= 1
    print(f"Te quedan {intentos} intentos.")
    
    num = int(input("Introduce otro número: "))

if num_secreto == num:
    print(f"CORRECTO: era el {num_secreto} y lo has adivinado en {11 - intentos} intentos.")
else:
    print(f"¡Has perdido! El número era: {num_secreto}")
