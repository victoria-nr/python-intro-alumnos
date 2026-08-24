# Pedir números hasta que se introduzca un 0 y sumarlos y hacer media
suma = 0
cont = 0

for _ in range(1000):
    num = int(input("Número (0 para salir): "))
    if num == 0:
        break
    suma += num
    cont += 1

if cont != 0:
    media = suma / cont
else:
    media = 0

print(f"Suma: {suma}")
print(f"Media: {media}")
