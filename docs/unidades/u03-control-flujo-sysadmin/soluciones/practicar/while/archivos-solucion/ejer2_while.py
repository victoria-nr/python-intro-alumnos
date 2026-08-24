# Pedir números hasta que se introduzca un 0 y sumarlos y hacer media
suma = 0
cont = 0

num = int(input("Número (0 para salir): "))

while num != 0:
    suma += num  
    cont += 1 
    num = int(input("Número (0 para salir): "))

if cont > 0:
    media = suma / cont
else:
    media = 0

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Media: {media}")
