import math

es_primo = True

num = int(input("Introduce un número para comprobar si es primo: "))

if num <= 1:
    es_primo = False
else:
    # Comprobación de divisibilidad desde 2 hasta la raíz cuadrada del número
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            es_primo = False
            print("No es primo")
            break 
        
    else: #solo se ejecuta si no se ejecuta el break
        print("Es primo")

