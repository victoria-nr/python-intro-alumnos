import random

# Adivina un número en 10 intentos
num_secreto = random.randint(1, 100)

print("Adivina el número (de 1 a 100):")

for intento in range(1,11):
    num = int(input("Introduce un número: "))

    if num_secreto == num:
        print(f"CORRECTO: era el {num_secreto} y lo has adivinado en {intento} intentos.")
        break
    elif num < num_secreto:
        print("Muy bajo")
    else:
         print("Muy alto")

    print(f"Te quedan {10-intento} intentos.")
    
   
else:
    print(f"¡Has perdido! El número era: {num_secreto}")
