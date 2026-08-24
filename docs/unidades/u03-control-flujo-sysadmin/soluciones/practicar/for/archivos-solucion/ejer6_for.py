# Programa para mostrar la tabla de multiplicar de un número ingresado por el usuario

num_tabla = int(input("¿De qué número quieres mostrar la tabla de multiplicar?: "))

for num in range(1, 11):
    print(f"{num} * {num_tabla} = {num * num_tabla}")
