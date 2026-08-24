# 3 La calculadora sencilla
# Pide al usuario dos números.
# Muestra la suma, la resta, la multiplicación y la división.

a_texto = input("Primer número: ")
b_texto = input("Segundo número: ")

a = float(a_texto)
b = float(b_texto)

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)