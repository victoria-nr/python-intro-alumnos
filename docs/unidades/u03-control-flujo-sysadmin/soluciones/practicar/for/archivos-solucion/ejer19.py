# Programa para mostrar las tablas de multiplicar de los números 1, 2, 3, 4 y 5 sin los múltiplos de 3.

for tabla in range(1, 6): 
    print(f"Tabla del {tabla}:")
    
    for num in range(1, 11):
        res = tabla * num
        if res % 3 == 0:
            continue
        print(f"{tabla} * {num} = {res}")
    
    input("Presiona Enter para continuar...\n")

