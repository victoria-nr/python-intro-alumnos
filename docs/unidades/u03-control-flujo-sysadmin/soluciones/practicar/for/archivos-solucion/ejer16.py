# Programa para mostrar las tablas de multiplicar de los números 1, 2, 3, 4 y 5.

for tabla in range(1, 6): 
    print(f"Tabla del {tabla}:")
    
    for num in range(1, 11):
        print(f"{tabla} * {num} = {tabla * num}")
    
    input("Presiona Enter para continuar...\n")
