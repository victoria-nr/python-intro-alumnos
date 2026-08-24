# Programa para mostrar la tabla de multiplicar de un número ingresado por el usuario

num_tabla = int(input("¿De qué número quieres mostrar la tabla de multiplicar?: "))

num=1
while num<=10:
    print(f" {num_tabla} * {num} = {num * num_tabla}")
    num+=1
