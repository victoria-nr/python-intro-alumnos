import random

lista_numeros = [0]*10

for i in range(10):
    lista_numeros[i]=random.randint(1, 10)

for numero in lista_numeros:
    cuadrado = numero ** 2
    cubo = numero ** 3
    print(f"Número: {numero}, Cuadrado: {cuadrado}, Cubo: {cubo}")
