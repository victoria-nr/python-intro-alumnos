# Mostrar los N primeros primos
N = int(input("Ingresa la cantidad de números primos que quieres mostrar: "))

contador_primos = 0  
numero = 2          

while contador_primos < N:
    es_primo = True

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break

    if es_primo:
        print(numero)
        contador_primos += 1

    numero += 1
